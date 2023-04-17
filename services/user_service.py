from sqlalchemy.orm import Session
from models.user import User


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, chat_id: int, first_name: str, last_name: str) -> User:
        existed_user = self.get_user(
            first_name=first_name, last_name=last_name)

        if (not existed_user):
            user = User(first_name=first_name,
                        last_name=last_name, chat_id=chat_id, role_id=2)

            self.db.add(user)

            self.db.commit()
            self.db.refresh(user)

            return user

        return existed_user

    # def get_user(self, first_name: str, last_name: str) -> User:
    #     return self.db.query(User).filter(
    #         User.first_name == first_name and
    #         User.last_name == last_name
    #     ).first()

    def get_user_by_chat_id(self, chat_id: int) -> User:
        return self.db.query(User).filter(
            User.chat_id == chat_id
        ).first()

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)

        if not user:
            return False

        self.db.delete(user)
        self.db.commit()

        return True
