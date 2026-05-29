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
