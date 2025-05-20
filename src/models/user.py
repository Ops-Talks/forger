import json
from datetime import datetime
from faker import Faker
from typing import Dict, Any

# Module-level constants
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