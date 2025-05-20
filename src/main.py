import json
from datetime import datetime
from faker import Faker
from typing import List, Dict, Any
from pathlib import Path


# Module-level constants
DEFAULT_OUTPUT_FILE = 'user_fake.json'
DEFAULT_USER_COUNT = 10
MIN_AGE = 18
MAX_AGE = 99
PASSWORD_LENGTH = 12
GENDER_OPTIONS = ('male', 'female', 'other')


class FakerUser:
    """A class to generate fake user data using the Faker library.
    
    This class generates random user data including personal information,
    contact details, and account status. All data is generated using the
    Faker library to ensure realistic and diverse test data.
    
    Attributes:
        id (str): Unique identifier for the user
        name (str): User's first name
        middle_name (str): User's middle name
        last_name (str): User's last name
        email (str): User's email address
        password (str): User's password
        gender (str): User's gender
        age (int): User's age
        is_active (bool): User's account status
        created_at (datetime): Account creation timestamp
        updated_at (datetime): Last update timestamp
    """
    
    def __init__(self):
        """Initialize a new FakerUser with random data."""
        fake = Faker()
        self.id = fake.uuid4()
        self.name = fake.first_name()
        self.middle_name = fake.first_name()
        self.last_name = fake.last_name()
        email_base = f"{self.name.lower()}.{self.last_name.lower()}"
        self.email = f"{email_base}@example.com"
        self.password = fake.password(length=PASSWORD_LENGTH)
        self.gender = fake.random_element(elements=GENDER_OPTIONS)
        self.age = fake.random_int(min=MIN_AGE, max=MAX_AGE)
        self.is_active = True
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_json(self) -> str:
        """Convert user data to JSON string.
        
        Returns:
            str: JSON string representation of the user data
        """
        j: Dict[str, Any] = {
            'id': self.id,
            'name': self.name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'gender': self.gender,
            'age': self.age,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        return json.dumps(j)


def generate_faker_users(count: int = DEFAULT_USER_COUNT) -> List[FakerUser]:
    """Generate a list of fake users.
    
    Args:
        count: Number of users to generate (default: DEFAULT_USER_COUNT)
        
    Returns:
        List[FakerUser]: List of FakerUser objects
        
    Raises:
        ValueError: If count is not a positive integer
    """
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer")
    return [FakerUser() for _ in range(count)]


def input_user_data(count: int, output_file: str = DEFAULT_OUTPUT_FILE) -> None:
    """Generate fake users and save them to a JSON file.
    
    Args:
        count: Number of users to generate
        output_file: Path to the output JSON file (default: DEFAULT_OUTPUT_FILE)
        
    Raises:
        ValueError: If count is not a positive integer
        IOError: If there are issues writing to the file
        json.JSONDecodeError: If there are issues with JSON encoding
    """
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer")
        
    try:
        users = generate_faker_users(count)
        user_data = [json.loads(user.get_json()) for user in users]
        
        # Create directory only if the output file is in a subdirectory
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with output_path.open('w') as f:
            json.dump(user_data, f, indent=2)
        
        print(f"Generated {count} users and saved to {output_file}")
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error saving user data: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise


def main() -> None:
    """Main function to generate fake users with user input."""
    try:
        while True:
            try:
                count = int(input("Enter the number of users to generate (positive integer): "))
                if count <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        output_file = input("Enter the output filename (default: user_fake.json): ").strip()
        if not output_file:
            output_file = DEFAULT_OUTPUT_FILE
        elif not output_file.endswith('.json'):
            output_file += '.json'
            
        input_user_data(count, output_file)
    except Exception as e:
        print(f"Error in main: {e}")
        raise


if __name__ == '__main__':
    main()