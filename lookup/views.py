from django.shortcuts import render
from pathlib import Path
import re
import yaml
import json
from mitreattack.stix20 import MitreAttackData

# Path to the:
# MITRE ATT&CK database, Sigma rules folder and Atomic Red Team tests folder
STIX_PATH = Path("enterprise-attack.json")
SIGMA_ROOT = Path("sigma")
ATOMICS_ROOT = Path("atomic-red-team/atomics")

# Load the ATT&CK database once when Djano starts
mitre_data = MitreAttackData(str(STIX_PATH)) if STIX_PATH.exists() else None
ATTACK_ID_RE = re.compile(r"T\d{4}(?:\.\d{3})?", re.IGNORECASE)

# Searches MITRE ATT&CK (by ID or name)
"""
Example input:
T1059
PowerShell
Command and Scripting Interpreter
"""
def find_technique(query):
    if not mitre_data: return None
    m = ATTACK_ID_RE.search(query)
    if m:
        return mitre_data.get_object_by_attack_id(m.group(0), "attack-pattern")
    matches = mitre_data.get_objects_by_name(query, "attack-pattern")
    return matches[0] if matches else None

# Given a technique, return the mitigations
def get_mitigations(technique):
    cleaned_mitigations = []
    try:
        tech_stix_id = technique["id"]
        mitigations = mitre_data.get_mitigations_mitigating_technique(tech_stix_id)
        
        # Normalize formatting discrepancies from the raw STIX bundle mapper
        if isinstance(mitigations, dict):
            mitigations = [entry["object"] for entries in mitigations.values() for entry in entries]
            
        for m in mitigations:
            obj = m.get("object") if isinstance(m, dict) and "object" in m else m
            
            # Extract mitigation's ATT&CK ID (Example: M1047) and its name, 
            # then save in a clean format
            ext_refs = obj.get("external_references", [])
            mitigation_id = ext_refs[0].get("external_id") if ext_refs else obj.get("id")
            
            cleaned_mitigations.append({
                'name': obj.get("name", "(no name)"),
                'id': mitigation_id
            })
    except Exception:
        # Backup to secondary library mapping if the primary lookup method fails
        try:
            mapping = mitre_data.get_all_techniques_mitigated_by_all_mitigations()
            fallback_list = mapping.get(technique["id"], [])
            for obj in fallback_list:
                ext_refs = obj.get("external_references", [])
                mitigation_id = ext_refs[0].get("external_id") if ext_refs else obj.get("id")
                cleaned_mitigations.append({
                    'name': obj.get("name", "(no name)"),
                    'id': mitigation_id
                })
        except Exception:
            pass
            
    return cleaned_mitigations

# Searches all Sigma rule files and returns the ones that 
# mention a specific ATT&CK technique ID (Example: T1059)
def scan_sigma(attack_id):
    if not SIGMA_ROOT.exists(): return []
    pattern = re.compile(re.escape(attack_id), re.IGNORECASE)
    matches = []
    for p in SIGMA_ROOT.rglob("*"):
        if p.is_dir() or p.suffix.lower() not in (".yml", ".yaml", ".json"): continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
            if not pattern.search(text): continue
            
            title, tags = "(no title)", None
            if p.suffix.lower() in (".yml", ".yaml"):
                doc = yaml.safe_load(text)
                if isinstance(doc, dict):
                    title = doc.get("title", title)
                    tags = doc.get("tags", tags)
            matches.append({"file": str(p), "title": title, "tags": tags})
        except Exception:
            continue
    return matches

# Finds and loads the Atomic Red Team tests for a given ATT&CK 
# technique ID (Example: as T1059) from its YAML file
def get_atomic_tests(attack_id):
    yaml_path = ATOMICS_ROOT / attack_id / f"{attack_id}.yaml"
    if not yaml_path.exists(): return []
    try:
        with open(yaml_path, "r") as f:
            return yaml.safe_load(f).get("atomic_tests", [])
    except Exception:
        return []

"""
Main Django view that receives a user's search, finds the ATT&CK technique, 
gathers related data (mitigations, Sigma rules, Atomic tests), 
and sends everything to the webpage for display
"""
def search_dashboard(request):
    # Gets the search term (q) from the URL and removes extra spaces
    # Example: /search?q=powershell so query = powershell
    query = request.GET.get('q', '').strip()
    context = {'query': query}

    if query:
        tech = find_technique(query)
        if tech:
            # Extracts the technique name, external ATT&CK ID, and description 
            # from the `tech` dictionary, using default fallback values 
            # if any of them are missing
            name = tech.get("name", "Unknown")
            ext_refs = tech.get("external_references", [{}])
            attack_id = ext_refs[0].get("external_id") if ext_refs else "Unknown"
            description = tech.get("description", "(no description)")

            # Collects mitigations, Sigma rules, and Atomic tests related to the technique
            mitigations_raw = get_mitigations(tech)
            sigma_matches = scan_sigma(attack_id) if attack_id else []
            atomic_tests = get_atomic_tests(attack_id) if attack_id else []

            # Adds technique data to the page context if found
            context.update({
                'technique_found': True,
                'name': name,
                'attack_id': attack_id,
                'stix_id': tech.get("id"),
                'description': description,
                'mitigations': mitigations_raw,
                'sigma_matches': sigma_matches,
                'atomic_tests': atomic_tests,
            })
        else:
            context['error'] = f"Technique '{query}' not found."

    # Send the context data to the lookup/index.html template and returns the rendered web page
    return render(request, 'lookup/index.html', context)