#  MITRE-Sigma Lookup Tool

CLI tool to lookup the MITRE mitigations and the Sigma detections for any technique
## Project Background

**MITRE ATT&CK** is a globally accessible knowledge base of adversary tactics and techniques. Security teams use it to understand attacker behaviors, plan defenses, and map observed activity in their networks.

**Sigma** is a generic and open signature format for SIEM (Security Information and Event Management) systems. It allows security teams to define detection rules once and convert them to different SIEM formats. By linking ATT&CK techniques to Sigma rules, analysts can quickly translate threat intelligence into actionable detection logic.

Through this project, I will interact with ATT&CK data, extract useful information, and gain hands-on exposure to practical cybersecurity workflows while developing my Python and Linux skills.

## Project Specifications

Input: an ATT&CK technique ID (`T1564`) or technique name.

Output:
	- Basic technique info (name, description)
	- ATT&CK mitigations related to that technique
	- Sigma rules that mention the technique ID

### Dependencies
Python 3.9+

A Linux environment with Internet access

*Note this project can be done in other systems, however all instructions are intended for Linux and may need to be modified for other environments.*
	
## Setup Environment

The setup process has been automated with `setup.sh`, or you can follow these steps:

### 1. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate
```
### 2. Install libraries
```bash
pip install mitreattack-python pyyaml rich
```

https://mitreattack-python.readthedocs.io/en/latest/
### 3. Download an ATT&CK STIX bundle file (enterprise)
```bash
curl https://raw.githubusercontent.com/mitre-attack/attack-stix-data/refs/heads/master/enterprise-attack/enterprise-attack.json -o enterprise-attack.json
```
### 4. Clone SigmaHQ/sigma locally
```bash
git clone https://github.com/SigmaHQ/sigma.git
```
### 5. Create a hello world program in `lookup.py`
```bash
echo -e '#!/usr/bin/env python3\nprint("hello world")' > lookup.py
```

## Example Usage
### Searching by Technique ID

Below we can see the successful run for Technique ID `T15661`. This printed out a comprehensive description of what phishing is (adversaries sending malicious messages to gain access to victim systems, utilizing social engineering, spearphishing, malicious attachments, or links). It also displayed a mitigation table of how to defend against phising such as `Audit (M1047)`, `Network Intrusion Prevention (M1031)`, `Software Configuration (M1054)`, `Restrict Web-Based Content (M1021)`, `Antivirus/Antimalware (M1049)`, and `User Training (M1017)`. 

The Sigma rules tables describes the attempt to find code that can detect phishing attempts. For example, the script found files in the local folders, `proc_creation_win_office_outlook_execution_from_temp.yml and iso_phishing.yml` that contain the text `T15661`. There are also many `no titles` and this is because the script had trouble reading some of the internal YAML fields and so it could not extract the rule titles and instead showed the default placeholders. However, we see one rule parsed correct named `Search-ms and WebDAV Suspicious Indicators in URL`

This is a name of a Sigma detection rule that is designed to detect phising links that abuse Windows feature such as `search-ms` and `WebDAV`. Attackers sometimes use these technologies to trick users into opening malicious files or connecting to attacker-controlled servers. 

`search-ms` is a Windows protocol that opens the Windows Search feature.
Attackers can craft malicious links that look harmless but actually open remote content. `WedDAV` is a protocol that lets remote web servers behave like shared network drives.
Attackers can host malware on a WebDAV server so the victim’s computer treats it like a normal file share. For example, a phising email might contain `search-ms:query=invoice` or connect to a remote WebDAV location. The Sigma rule watches logs for these suspicious URL patterns because they are commonly used in phishing and malware delivery campaigns

<img width="6412" height="10076" alt="mitre_ID" src="https://github.com/user-attachments/assets/e95e816f-8da4-4d50-b89d-1f8c3edd9075" />

### Searching by Technique name

Instead of searching by Technique ID, we can also search by technique name. I chose `Masquerading (T1036)` where hackers disguise malicious files or activity as something completely harmless (like renaming a piece of malware to svchost.exe so it looks like a built-in Windows service). The mitigations and sigma rules are outputted as well and describe the ways to defend and detect these attacks

For example, we can see that one mitigation technique is `Code Signing (M1045)` where we ensure files have a valid digital signature so hackers can't easily fake standard system utilities

The sigma output shows us ways to detect this attack. In these rules `proc_creation_win_renamed_powershell.yml` and `proc_creation_win_renamed_psexec.yml` monitor Windows event logs to see if a process has been renamed to hide its identity

<img width="5367" height="16384" alt="mitre_name" src="https://github.com/user-attachments/assets/e3ebc8cc-aefc-4253-b852-c2c4aa461d4d" />

## Post Project Ideas

- ~~Alias the program to create a custom command that is accessible anywhere~~
- ~~Handle outputting to files~~
- Handle bulk searches and outputs
- Integrate another open-source library mapped to MITRE ATT&CK
- Use Django to create a web interface
	- Search bar for searching, rather than command line argument
	- Host static site via cloud technology or physical server
- Improve the speed of Sigma searches 
	- maybe by applying particular data structures & algorithms
- Automatically update MITRE and Sigma (which are only accessed locally)
- Make searching by name or description “smarter” 
	- Output all techniques that partially map to description and let user choose
- Interface directly with other professional cybersecurity tools
	- MITRE Caldera - Attack platform for launching TTPs in MITRE ATT&CK
	- Metasploit - Tool for emulating attacker’s TTPs
	- Splunk - Open-source SIEM (could implement Sigma rules directly)

## Post Project Implmentation #1: Alias
- I decided to add this improvement as the first one. Creating an alias is very helpful instead of typing out long commands in the terminal
	- To make it a standalone command, we need to give the file execute permissions. This is because Unix systems require execute permissions before a script 	  can be run directly from the terminal
 ```bash
chmod +x mitre-attack-sigma.py
```
 - Next, I opened my configuration file via `nano ~/.zshrc` and added my alias
```bash
alias mitre="~/path/to/your/folder/mitre-attack-sigma.py"
```
  Since I am in a 	virtual environment and my 		script relies on packages such as `rich` and `yaml` inside my `venv`, a standard alias 		might fail if the virtual environment isn't active.
  - I fixed this by pointing the alias 		directly to the Python interpreter inside my venv 
```bash
alias mitre="~/path/to/your/folder/venv/bin/python3"
```
- The full alias
```bash
alias mitre="~/path/to/your/folder/venv/bin/python3 ~/path/to/your/folder/mitre-attack-sigma.py"
```
  - Then, I saved it via `source ~/.zshrc` and 	tested it with `mitre Masquerading`. Below are the results and it worked. As you can see instead of having to `cd` inside folders and provide a long command, I can just type `mitre` which is the alias and it works the same way as it did before. Note that I also do not need to be inside the `venv` folder and can deactivate it and it still works
<img width="5192" height="6508" alt="image" src="https://github.com/user-attachments/assets/afff9932-114d-4515-b1d2-c543568f4c9d" />

## Post Project Implmentation #2: Handle outputting to files
 - For this implementation, it was very minimal
 	- The original code had `console = Console()` and I changed it to `console = Console(record=True)`. This allows the Console class to save a copy of all its printed and logged data and allows us to use Rich's terminal export feature
  - Then, I added this line to tell `argparse` to be able to accept a new, optional argument for the output file path
```python
parser.add_argument("-o", "--output", help="Path to a file where results should be saved (for example, report.txt)")
```
  - Next, I updated the `main()` class to include:
```python
if args.output:
        try:
            console.save_text(args.output)
            console.print(f"\n[bold green] Report successfully saved to: {args.output}[/bold green]")
        except Exception as e:
            console.print(f"\n[red]Failed to save report to file: {e}[/red]")
```
- This code checks whether `args.output` has a value or in other words, if the user has provided an output path file and tries to save console content to that file specified in `args.output` and prints a success message to the terminal
- We can see below that I was able to use the `-o credentials_from_password_stores.txt` parameter and then at the bottom it printed `Report successfully saved to: credentials_from_password_stores.txt`
<img width="5192" height="4948" alt="image" src="https://github.com/user-attachments/assets/45a0bf3c-bc0f-4593-a600-a9258a465237" />

- The `The credentials_from_password_stores.txt` file has been successfully stored on my local computer

<img width="1144" height="899" alt="image" src="https://github.com/user-attachments/assets/895fb1c7-28ca-4351-86dc-f61cbb99b61c" />

## Post Project Implmentation #3: Handling bulk searches and output
This implementation allowed the user to type in multiple commands or even input a file and outputs it to a folder with all the files in it. The first change was to allow the user to type a `.txt` file which contained the technique IDs instead of one-by-one inputs

```python
parser.add_argument("query", nargs="?", help="A single ATT&CK technique ID or name.")
```
Before it was
```python
parser.add_argument("query", help="ATT&CK technique ID (`T1564`) or technique name.")
```
But now the `nargs="?"` allows for 0 or 1 argument and allows the user to run the tool without a single query and instead using a text file instead

I then added two more options that the user can type where `-f` allows the user to pass a file path string and `-o` creates a destination target directory folder string defaulting to a folder named `"reports"` if the user doesn't specify one
```python
parser.add_argument("-f", "--file", help="Path to a text file containing a list of ATT&CK IDs (one per line).")
parser.add_argument("-o", "--output-dir", default="reports", help="Directory folder where bulk reports will be saved.")
```
Then, I made a function that generates a single report for every technique instead of having one giant report that could result it in being messy and hard to read

You can see that I also added a `console.clear()` and this was because since we have `console = Console(record=True)` which logs everything and so running multiple techniques back to back would cause the reports to pile up into one big report and the techniques would be mixed together and so clearing the cache makes sure that each technique gets it own report

```python
def generate_single_report(mitre, sigma_root, query, output_dir=None):
    console.print(f"\n[bold blue]=========================================[/bold blue]")
    console.print(f"[bold]Processing technique for:[/bold] {query}")
    
    tech = find_technique(mitre, query)
    if not tech:
        console.print(f"[red]Technique '{query}' not found. Skipping.[/red]")
        return

    console.clear() 
    
    print_technique_summary(tech)
    
    console.print("\n[bold]Fetching mitigations from ATT&CK...[/bold]")
    mitigations = get_mitigations_for_technique(mitre, tech)
    print_mitigations(mitigations)
    
    console.print("\n[bold]Scanning local Sigma repo for matching rules...[/bold]")
    attack_id = get_attack_id(tech, query)
    matches = scan_sigma_for_technique(sigma_root, attack_id)
    print_sigma_matches(matches)

    if output_dir and attack_id:
        
        out_path = Path(output_dir)
        out_path.mkdir(exist_ok=True, parents=True)
        file_target = out_path / f"{attack_id}_report.txt"
        console.save_text(str(file_target))
        console.print(f"\n[bold green] Saved to {file_target}[/bold green]")
```

Furthermore, this just creates a directory which has each of the reports in it such as `reports/T1566_report.txt`. `console.save_text` then dumps the isolated text recording into that unique filename

```python
if output_dir and attack_id:
        out_path = Path(output_dir)
        out_path.mkdir(exist_ok=True, parents=True)
        file_target = out_path / f"{attack_id}_report.txt"
        console.save_text(str(file_target))
        console.print(f"\n[bold green] Saved to {file_target}[/bold green]")
```

Lastly, I made changes to the `main()` function where I made a empty Python array list called `queries` to store the multiple techniques and parse the users multiple argument such as `mitre T1566,T1036`. This code is important because it iterates through the array stack items one by one. If it determines that you are running a bulk operation (more than 1 query or reading from a file), it assigns the `output_folder` target path, going through `generate_single_report()` to cleanly dump organized files into your directory stack

```python
def main():
    args = process_arguments()
    
    queries = []
    
    if args.file:
        file_path = Path(args.file)
        if file_path.exists():
            queries = [line.strip() for line in file_path.read_text().splitlines() if line.strip()]
        else:
            console.print(f"[red]Error: Input file '{args.file}' not found.[/red]")
            sys.exit(1)
    elif args.query:
        queries = [q.strip() for q in args.query.split(",")]
    else:
        console.print("[red]Error: You must provide a query technique or a text file via -f.[/red]")
        sys.exit(1)

    console.print("[bold]Loading ATT&CK data...[/bold]")
    mitre = load_mitre_data(args.stix)
    sigma_root = get_sigma_root(args.sigma)

    console.print(f"[bold green]Starting bulk processing for {len(queries)} techniques...[/bold green]")
    for q in queries:
        # If doing bulk, pass the output folder name to save individual reports
        output_folder = args.output_dir if (len(queries) > 1 or args.file) else None
        generate_single_report(mitre, sigma_root, q, output_dir=output_folder)

    console.print("\n[bold green] All techniques processed successfully![/bold green]")
```

