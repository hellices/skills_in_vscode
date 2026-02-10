from typing import Optional, List
from datetime import datetime
from ..models.user import User


class UserService:
    """Service for managing user operations."""
    
    def __init__(self):
        self._users: List[User] = []
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Retrieve a user by their ID."""
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def create_user(self, email: str, name: str) -> User:
        """Create a new user."""
        user_id = len(self._users) + 1
        user = User(
            id=user_id,
            email=email,
            name=name,
            created_at=datetime.now()
        )
        self._users.append(user)
        return user
