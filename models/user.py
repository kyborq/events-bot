from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base
from models.role import Role
from models.event import Event


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)

    role_id = Column(Integer, ForeignKey('roles.id'))

    role = relationship(Role, back_populates="users")
    event_creator = relationship(Event, back_populates="creator")
