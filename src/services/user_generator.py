from typing import List
from pathlib import Path
import json
from ..models.user import FakerUser

# Module-level constants
DEFAULT_USER_COUNT = 10
DEFAULT_OUTPUT_FILE = 'users.json'


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


def save_users_to_file(count: int, output_file: str = DEFAULT_OUTPUT_FILE) -> None:
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
            
    except (IOError, json.JSONDecodeError) as e:
        raise IOError(f"Error saving user data: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}") 