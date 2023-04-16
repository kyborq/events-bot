import telebot
from bot.menus.main import MainMenu
from config.config import Config
from bot.handlers.start import StartCommand


class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(Config.BOT_TOKEN)

    def __start_polling(self):
        self.bot.polling(none_stop=True)

    def __add_handlers(self):
        start_command = StartCommand()

        start_command.register(self.bot)

    def __add_menu(self):
        main_menu = MainMenu()

        # self.bot.add_keyboard_button(main_menu.name, callback_data='main_menu')

    def run(self):
        self.__add_handlers()
        self.__add_menu()
        self.__start_polling()
