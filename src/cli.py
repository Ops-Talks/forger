import typer
from typing import Optional
from pathlib import Path
from user import input_user_data

app = typer.Typer(help="Data Generation CLI Tool")

@app.command()
def generate(
    count: int = typer.Option(
        10,
        "--count", "-c",
        help="Number of records to generate",
        min=1
    ),
    output: Path = typer.Option(
        "user_fake.json",
        "--output", "-o",
        help="Output file path",
        dir_okay=False,
        writable=True
    )
):
    """
    Generate fake user data with specified number of records.
    """
    try:
        input_user_data(count, str(output))
        typer.echo(f"Successfully generated {count} records in {output}")
    except Exception as e:
        typer.echo(f"Error: {str(e)}", err=True)
        raise typer.Exit(1)

def main():
    app()

if __name__ == "__main__":
    main() 