import typer
from rich.console import Console
from rich.panel import Panel
from .services.user_generator import save_users_to_file

# Initialize Typer app and Rich console
app = typer.Typer(help="Generate fake user data with customizable options")
console = Console()


@app.command()
def main(
    count: int = typer.Option(
        10,
        "--count", "-c",
        help="Number of fake users to generate",
        min=1
    ),
    output: str = typer.Option(
        'users.json',
        "--output", "-o",
        help="Output JSON file path"
    )
) -> None:
    """Generate fake user data and save it to a JSON file.
    
    If no arguments are provided, generates 10 users and saves to users.json
    """
    try:
        if not output.endswith('.json'):
            output += '.json'
            
        save_users_to_file(count, output)
        
        # Display success message in a nice panel
        console.print(Panel(
            f"[green]Successfully generated {count} users and saved to {output}[/green]",
            title="Forger",
            border_style="green"
        ))
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1) 