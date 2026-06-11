## Post Project Implmentation #7: Automatically update MITRE and Sigma 
- For this implementation, I added support for automatically updating MITRE ATT&CK data and Sigma rules, removing the need to manually download and apply updates
### 1. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install GitPython
```bash
pip install GitPython
```
- I added the update logic script to my code which downloads the newest `enterprise-attack.json` from the official MITRE Live STIX repository and calls a git pull on my local
`sigma` folder

- Then, I added another line of code to let the command line accept the `--update` flag and this function runs before it does anything else

```python
parser.add_argument("--update", action="store_true", help="Automatically pull latest MITRE and Sigma updates before searching.")
```
- Note: If you do get an error such as `Failed to update MITRE data: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)>` run the command below and change the Python version to your current version that is inside your virtual environment

```bash
/Applications/Python\ 3.15/Install\ Certificates.command
```
- HTTPS certificate validation requires a trusted root certificate store. When Python makes an HTTPS request (for example, using `urllib`), it needs access to a set of trusted root CA certificates so it can verify the certificate chain presented by the server. If Python cannot find or access a suitable trust store, certificate verification fails even if the website's certificate is valid

- In a normal verification process, Python verifies the server certificate, follows the chain through any intermediate certificates, and ultimately checks whether the chain terminates at a trusted root CA in its trust store. If the necessary root certificates are unavailable, Python cannot complete this chain-of-trust validation and rejects the connection

### Example Usage
<img width="1964" height="1108" alt="image" src="https://github.com/user-attachments/assets/173b3ce3-f881-4994-98d0-ebbb66572818" />
