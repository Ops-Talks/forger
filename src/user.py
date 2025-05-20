import json
from datetime import datetime
from faker import Faker
from typing import List
import os


class FakerUser:
    """A class to generate fake user data using the Faker library."""
    
    def __init__(self):
        """Initialize a new FakerUser with random data."""
        fake = Faker()
        self.id = fake.uuid4()
        self.name = fake.first_name()
        self.middle_name = fake.first_name()
        self.last_name = fake.last_name()
        email_base = f"{self.name.lower()}.{self.last_name.lower()}"
        self.email = f"{email_base}@example.com"
        self.password = fake.password(length=12)
        self.gender = fake.random_element(elements=('male', 'female', 'other'))
        self.age = fake.random_int(min=18, max=99)
        self.is_active = True
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_json(self) -> str:
        """Convert user data to JSON string."""
        j = {
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


def generate_faker_users(count: int = 10) -> List[FakerUser]:
    """Generate a list of fake users.
    
    Args:
        count: Number of users to generate (default: 10)
        
    Returns:
        List of FakerUser objects
    """
    if count <= 0:
        raise ValueError("Count must be a positive integer")
    return [FakerUser() for _ in range(count)]


def input_user_data(count: int, output_file: str = 'user_fake.json') -> None:
    """Generate fake users and save them to a JSON file.
    
    Args:
        count: Number of users to generate
        output_file: Path to the output JSON file (default: 'user_fake.json')
    """
    try:
        if count <= 0:
            raise ValueError("Count must be a positive integer")
            
        users = generate_faker_users(count)
        user_data = [json.loads(user.get_json()) for user in users]
        
        # Create directory only if the output file is in a subdirectory
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump(user_data, f, indent=2)
        
        print(f"Generated {count} users and saved to {output_file}")
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error saving user data: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main() -> None:
    """Main function to generate fake users."""
    try:
        no_of_input = 10
        input_user_data(no_of_input)
    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == '__main__':
    main()