# Forger

A Python tool for generating fake data and exporting it to JSON files. Built with Faker, Typer, and Poetry.

## Description

Forger is a command-line tool that helps you generate realistic fake data for testing and development purposes. It uses the Faker library to create various types of fake data and exports them to JSON files. Perfect for developers who need to quickly generate test data for their applications.

## Features

- Generate fake user data with customizable fields
- Export data to JSON format with proper formatting
- Support for multiple data types (names, addresses, emails, etc.)
- Command-line interface using Typer for easy interaction
- Configurable output format and file naming
- Support for custom data generation rules
- Batch processing capabilities

## Requirements

- Python 3.13 or higher
- Poetry for dependency management
- Git (for installation)

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

3. Verify the installation:
```bash
poetry run python main.py --help
```

## Usage

After installation, you can use Forger through the command line:

```bash
# Generate fake user data
poetry run python main.py generate-users --count 10 --output users.json

# Generate data with custom fields
poetry run python main.py generate-users --count 5 --fields name,email,address --output custom_users.json

# Generate data with specific locale
poetry run python main.py generate-users --count 3 --locale fr_FR --output french_users.json
```

## Development

### Setup Development Environment

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/yourusername/forger.git
cd forger
```

3. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

4. Install development dependencies:
```bash
poetry install
```

### Adding Dependencies

To add new dependencies:

```bash
# Add a production dependency
poetry add package-name

# Add a development dependency
poetry add --group dev package-name
```

### Running Tests

```bash
poetry run pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and follow the existing code style.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Author

- weyderfs (weyderfs@gmail.com)

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.