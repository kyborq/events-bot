from bot.command import Command
from bot.utils import send_message


class RegistrationCommand(Command):
    def __init__(self):
        super().__init__('register', 'Register Command')

        self.first_name = ""
        self.last_name = ""

        self.step_index = 0

    def execute(self, bot, message) -> None:
        send_message(bot, message.chat.id,
                     'Процесс регистрации начат')

        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        bot.add_conversation_handler(
            self.next_step, message.chat.id)

    def next_step(self, message):
        print(message.chat.id)
