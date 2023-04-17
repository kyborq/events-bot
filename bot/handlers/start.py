from bot.command import Command
from bot.utils import send_message
from config.database import Session
from services.user_service import UserService


class StartCommand(Command):
    def __init__(self):
        super().__init__('start', 'Start Command')
        self.counter = 0

    def execute(self, bot, message) -> None:
        user_service = UserService(Session())
        chat_id = message.chat.id

        if (self.counter > 5):
            send_message(bot, message.chat.id,
                         'Хватит нажимать на кнопку!!! Пожалуйста!!! Умоляю перестань!!!')
            self.counter = 0
            return

        if (not user_service.get_user_by_chat_id(chat_id)):
            send_message(bot, message.chat.id,
                         'Привет, а вы здесь впервые! Давайте познакомимся :) Меня зовут Митти, а вас?')
            self.counter = self.counter + 1
            return

        send_message(bot, message.chat.id, 'Вы зарегистрированы')
