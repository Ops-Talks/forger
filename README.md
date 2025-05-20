# Forger

A Python tool for generating fake data and exporting it to JSON files. Built with Faker, Typer, and Poetry.

## Description

Forger is a command-line tool that helps you generate realistic fake data for testing and development purposes. It uses the Faker library to create various types of fake data and exports them to JSON files.

## Features

- Generate fake user data
- Export data to JSON format
- Customizable data generation
- Command-line interface using Typer

## Requirements

- Python 3.13 or higher
- Poetry for dependency management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/forger.git
cd forger
```

2. Install dependencies using Poetry:
```bash
poetry install
```

## Usage

After installation, you can use Forger through the command line:

```bash
# Generate fake user data
poetry run python main.py generate-users --count 10 --output users.json
```

## Development

This project uses Poetry for dependency management. To add new dependencies:

```bash
poetry add package-name
```

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Author

- weyderfs (weyderfs@gmail.com)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.