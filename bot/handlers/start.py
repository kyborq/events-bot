from bot.command import Command
from bot.utils import send_message


class StartCommand(Command):
    def __init__(self):
        super().__init__('start', 'Start Command')

    def execute(self, bot, message) -> None:
        send_message(bot, message.chat.id, 'Hello, World!')
