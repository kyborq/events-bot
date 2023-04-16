from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    description = Column(String)

    start_date = Column(Date)
    start_time = Column(Time)

    seats = Column(Integer)

    creator_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='event_creator')
