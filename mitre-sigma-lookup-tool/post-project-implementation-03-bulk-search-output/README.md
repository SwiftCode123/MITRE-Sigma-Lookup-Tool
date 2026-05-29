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
