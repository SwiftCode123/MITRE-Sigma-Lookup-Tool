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

```python
def generate_single_report(mitre, sigma_root, query, output_dir=None):
    console.print(f"\n[bold blue]=========================================[/bold blue]")
    console.print(f"[bold]Processing technique for:[/bold] {query}")
    
    tech = find_technique(mitre, query)
    if not tech:
        console.print(f"[red]Technique '{query}' not found. Skipping.[/red]")
        return
    
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

Lastly, I made changes to the `main()` function where I made a empty Python array list called `queries` to store the multiple techniques and parse the users multiple argument such as `mitre T1566,T1036`. This code is important because it iterates through the array stack items one by one. If it determines that you are running a bulk operation (more than 1 query or reading from a file), it assigns the `output_folder` target path, going through `generate_single_report()` to cleanly dump organized files into your directory stack. Note that this still works if the user types in a single argument as it did originally

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
## Example Usage
### Searching with Multiple Techniques (Comma Separated)
<img width="6872" height="11124" alt="image" src="https://github.com/user-attachments/assets/a7d7d3b6-45db-4644-b6ba-8f5bdaf79288" />

You can see that I searched with the `T1057`, `T1016`, `T1033` techniques all that once and it was able to output it to the console and save it to my folder named `reports` since I did not specify a folder name

<img width="363" height="58" alt="image" src="https://github.com/user-attachments/assets/f31f2a94-7a94-4b82-b5cc-a5e5658be333" />

### Searching by Text file
<img width="6800" height="11184" alt="image" src="https://github.com/user-attachments/assets/6f1a3d11-2ab9-4568-8f38-a80755010f8d" />

I fed a file named `bulk_targets.txt` with 3 techniques to the tool and it printed out all the information and successfully saved it to the `reports` folder

<img width="340" height="61" alt="image" src="https://github.com/user-attachments/assets/cb30b6f4-7d11-4a49-a5e2-01433fbac5f9" />

### Searching with Custom Directory Option
Lastly, I tested it the `-o` option with `mitre T1057,T1033 -o incident_alpha_reports` being the command and put my folder name that I wanted and it printed out all the techniques

<img width="5768" height="8428" alt="image" src="https://github.com/user-attachments/assets/539b1b25-7c08-4069-8d82-fb4689d8b88d" />

Below, it created the folder structure that I inputted
<img width="371" height="47" alt="image" src="https://github.com/user-attachments/assets/3876bc6f-5f2f-400d-b2fe-00d87b738939" />


