from config.database import Base, engine
from models.user import User
from models.role import Role
from models.event import Event


Base.metadata.create_all(bind=engine)
