## Post Project Implmentation #4: Open-source Library - Atomic Red Team
This implementation required installing the Atomic Red Team library

### 1. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Clone the Atomic Red Team library
```bash
git clone https://github.com/redcanaryco/atomic-red-team.git
```
- This code checks whether any Atomic Red Team tests are available in the `atomic_tests` list and if they are, it creates a formatted terminal table and adds information for the test name, supported platforms, and executor engine, and loops through each test to extract those values (using default values when fields are missing), adds each test as a row in the table, and then prints the completed table to the console. If no tests are found, it instead prints a yellow warning message stating that no local Atomic Red Team tests were found for the technique

```python
   if atomic_tests:
        table = Table(title="Atomic Red Team Simulation Tests")
        table.add_column("Test Name", style="cyan")
        table.add_column("Supported Platforms", style="green")
        table.add_column("Executor Engine", style="magenta")

        for test in atomic_tests:
            name = test.get("name", "Unnamed Test")
            platforms = ", ".join(test.get("supported_platforms", []))
            executor = test.get("executor", {}).get("name", "manual")
            table.add_row(name, platforms, executor)
        
        console.print(table)
    else:
        console.print("[yellow]No local Atomic Red Team tests found for this technique.[/yellow]")
```

### Example Usage
<img width="6872" height="4948" alt="image" src="https://github.com/user-attachments/assets/70c75991-1295-44bd-9d49-3d7c0c88fa7b" />

- Above, you can see it has printed all three pieces of information: Technique ID information, Sigma rules and the attack simulations tests from the Atomic Red Team library. For this technique ID, `T1016 (System Network Configuration Discovery)`, where the adversary runs native, built-in system tools to look at the machine's internal network configuration such as IP addresses & subnets, DNS servers, routing tables, and firewall rules

- For example, in the attack simulation test, `List Windows Firewall Rules`, malicious actors typically run this command

```bash
netsh advfirewall firewall show rule name=all
```
- to understand what inbound and outbound ports, programs, or services are allowed through      the firewall. By executing this test with Atomic Red Team, security teams can validate        whether their Endpoint Detection and Response (EDR) or SIEM solutions successfully            generate telemetry or alerts when this discovery command is run
