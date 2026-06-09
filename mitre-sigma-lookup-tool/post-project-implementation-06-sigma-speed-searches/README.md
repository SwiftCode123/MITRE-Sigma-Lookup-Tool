## Post Project Implmentation #5: Improving the speed of Sigma searches
- This implementation was all about improving the speed of the Sigma searches. Currently, everytime someone searched for an ATTACK technique such as `T1566`, the program opened every Sigma file, read the file contents, searched for the technique, parsed the YAML/JSON metadata and returned the matches. If someone searched another technique, it repeated this entire process again. Therefore, if we have 10,000 Sigma rules and a 100 ATTACK techniques to process, this could mean reading 10,000 files 100 times.
- Therefore, the solution to this is to use an inverted index data structure using a Python dictionary combined with an initialization cache. In general, an Inverted Index maps a search term (the ATTACK ID) directly to the files that contain it, similar to the index at the back of a textbook

- After the changes, the idea is for the program to scan all Sigma files once, extract every ATTACK ID it finds and essentially build a lookup table (dictionary) in memory. Conceptually, it creates something like this

  ```python
  SIGMA_INDEX = {
      "T1566": [
          {"file": "rule1.yml", "title": "Phishing Detection"},
          {"file": "rule2.yml", "title": "Email Attachment Alert"}
      ],
      "T1036": [
          {"file": "rule3.yml", "title": "Masquerading Detection"}
      ]
  }
  ```
- Later, when someone searches for `T1566`, the program does `SIGMA_INDEX["T1566"]` instead of searching the entire disk again. This reduces the search operation from a full file scan to an average case `O(1)` dictionary lookup
 
## Code Explanation
- First, I created a global dictionary that holds all ATTACK to rule mappings

  ```python
  SIGMA_INDEX = {}
  ```
  
- This function scans all Sigma rules once during startup and creates a lookup table in memory. Instead of re-reading thousands of files for every ATTACK technique search, the program reuses this cached data throughout report processing. This reduces disk I/O and allows techniques to be retrieved through fast dictionary lookups

  ```python
  build_sigma_index()
  ```

- This function performs a direct lookup against the cached Sigma index and returns the matching rules for a given ATT&CK technique

  ```python
  lookup_sigma_in_index()
  ```
  
- Together, these changes eliminate repeated disk scans and metadata parsing, significantly reducing the time required to process large numbers of ATTACK techniques against large Sigma rule repositories

## Performance Comparison
- W.I.P
