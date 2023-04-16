from sqlalchemy.orm import Session
from models.role import Role
from models.user import User
from models.event import Event


class EventService:
    def __init__(self, db: Session):
        self.db = db

    def create_event(self, title: str, description: str):
        event = Event(title=title, description=description)
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event
