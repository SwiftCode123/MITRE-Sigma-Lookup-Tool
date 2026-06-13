# Splunk Integration Development
- With the setup finished, this part details the about the building the Python bridge inside my `mitre-sigma-lookup-tool` project to translate the Sigma rules and push them directly over the network 

## Updating the `.env` file
- First, I had to update the `.env` file. This was to add a new Splunk VM connection detail so the script knows where to send the data to. Obviously, I can't show you this but for placeholder purposes, below are the values you need to fill in except the port, everyone knows that one
```python
SPLUNK_HOST=[Proxmox Ubuntu IP address goes here]
SPLUNK_PORT=8089        
SPLUNK_USER=[Your Splunk username here]
SPLUNK_PASSWORD=[Your Splunk password here]
```

## Install the required libraries
- Make sure you are in your virtual environment (`venv`) and activated and these are the libraries required to compile Sigma rules and communicate with the Splunk API
```bash
pip install splunk-sdk pysigma pysigma-backend-splunk
```
- where `splunk-sdk` handles the authenticated networking tunnel to the Proxmox VM and `pysigma` and `pysigma-backend-splunk` are python compilation framework that transforms Sigma YAML directly into Splunk SPL strings

- Then I added the code logic (see `mitre-attack-sigma.py` file). The flow is detailed below in a nice detailed diagram

## SIEM Architecture Diagram
<img width="1319" height="628" alt="image" src="https://github.com/user-attachments/assets/5da63915-5516-4654-a2b0-c4ae3f61bfff" />
