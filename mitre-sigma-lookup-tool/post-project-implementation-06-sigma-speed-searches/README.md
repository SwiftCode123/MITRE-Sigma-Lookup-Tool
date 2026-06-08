## Post Project Implmentation #5: Improving the speed of Sigma searches
- This implementation was all about improving the speed of the Sigma searches. Currently, everytime someone searched for an ATTACK technique such as `T1566`, the program opened every Sigma file, read the file contents, searched for the technique, parsed the YAML/JSON metadata and returned the matches. If someone searched another technique, it repeated this entire process again. Therefore, if we have 10,000 Sigma rules and a 100 ATTACK techniques to process, this could take reading up 10,000 files 100 times

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
  - Later, when someone searches for `T1566`, the program does `SIGMA_INDEX["T1566"]` instead of searching the entire disk again
 
## Code Change Explanation
- First, I created a global dictionary that holds all ATTACK to rule mappings
  ```python
  SIGMA_INDEX = {}
```
