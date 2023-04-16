from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.config import Config

engine = create_engine(Config.DATABASE_URI, connect_args={
                       "check_same_thread": False})
Session = sessionmaker(bind=engine)
Base = declarative_base()
