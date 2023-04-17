import telebot
from bot.menus.main import MainMenu
from config.config import Config
from bot.handlers.start import StartCommand
from bot.handlers.registration import RegistrationCommand


class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(Config.BOT_TOKEN)
        # self.conv = telebot.TeleBot.step

    def __start_polling(self):
        self.bot.polling(none_stop=True)

    def __add_handlers(self):
        start_command = StartCommand()
        register_command = RegistrationCommand()

        start_command.register(self.bot)
        register_command.register(self.bot)

    def __add_menu(self):
        # main_menu = MainMenu()

        # self.bot.add_keyboard_button(main_menu.name, callback_data='main_menu')

        pass

    def run(self):
        self.__add_handlers()
        self.__add_menu()
        self.__start_polling()
