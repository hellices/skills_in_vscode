from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class User:
    """User model representing a system user.
    
    Attributes:
        id: Unique user identifier
        email: User's email address
        name: User's full name
        created_at: Timestamp of user creation
    """
    id: int
    email: str
    name: str
    created_at: datetime
    
    def __post_init__(self):
        """Validate user data after initialization."""
        if not self.email:
            raise ValueError("Email is required")
        if "@" not in self.email:
            raise ValueError("Invalid email format")
