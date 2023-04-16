import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    DATABASE_URI = os.getenv('DATABASE_URI')
