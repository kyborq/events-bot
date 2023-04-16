from abc import abstractmethod, ABC
from telegram import Bot, Message


class Command(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def execute(self, bot: Bot, message: Message) -> None:
        pass

    def register(self, bot: Bot) -> None:
        @bot.message_handler(commands=[self.name])
        def handler(message):
            self.execute(bot, message)
        return handler
