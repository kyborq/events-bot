from sqlalchemy.orm import Session
from models.role import Role
from models.user import User


class RoleService:
    def __init__(self, db: Session):
        self.db = db

    def create_role(self, name: str) -> Role:
        role = Role(name=name)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    def assign_role(self, user_id: int, role_id: int) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError(f"User with id {user_id} does not exist")
        role = self.db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise ValueError(f"Role with id {role_id} does not exist")

        user.role = role
        self.db.commit()
        self.db.refresh(user)
        return user
