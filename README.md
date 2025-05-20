# Forger

A Python CLI tool for generating fake data and exporting it to JSON files.

<p align="center" width="100%">
    <img width="50%"src="assets/forger.png" />
</p>

## Overview

Forger helps you generate realistic test data using the Faker library. It's perfect for developers who need to quickly create test datasets for their applications.

## Features

- Generate fake user data with customizable fields
- Export to JSON format
- Support for multiple data types (names, addresses, emails)
- Command-line interface with Typer
- Configurable output format
- Batch processing

## Sample of JSON result file

```json
{
    "id": "21f94bb0-3756-417b-9b02-60052c81c84c",
    "name": "Michele",
    "middle_name": "Pamela",
    "last_name": "Martin",
    "email": "michele.martin@example.com",
    "password": "6y84DZsk$%V+",
    "gender": "male",
    "age": 49,
    "is_active": true,
    "created_at": "2025-05-20T11:59:05.956115",
    "updated_at": "2025-05-20T11:59:05.956117"
  }
```

## Requirements

- Python 3.13+
- Poetry
- Git

## Quick Start

1. Clone and install:
```bash
git clone https://github.com/yourusername/forger.git
cd forger
poetry install
```

2. Verify installation:
```bash
forger --help
```

## Usage

```sh
# Basic usage
forger # Will generate 10 users and a output file users.json

# With parameters
$ forger -c 50 -o user50.json

$ forger -c 50 -o user50 #without file extension
```

## Development

1. Fork and clone the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Install dependencies: `poetry install`
4. Run tests: `poetry run pytest`

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

Apache 2.0 License - see [LICENSE](LICENSE) for details.
