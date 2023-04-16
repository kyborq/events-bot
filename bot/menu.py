from abc import abstractmethod, ABC
from telegram import Bot, Message
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Option(ABC):
    def __init__(self, name, data):
        self.name = name
        self.data = data


class Menu(ABC):
    def __init__(self, name):
        self.name = name
        self.keyboard = self.create_keyboard()

    def create_keyboard(self):
        keyboard = InlineKeyboardMarkup()
        for option in self.create_options():
            button = InlineKeyboardButton(
                option['text'], callback_data=option['callback_data'])
            keyboard.add(button)
        return keyboard

    @abstractmethod
    def create_options(self):
        pass

    @abstractmethod
    def execute(self, bot: Bot, message: Message) -> None:
        pass
