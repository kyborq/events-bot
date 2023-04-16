from bot.menu import Menu


class MainMenu(Menu):
    def __init__(self):
        super().__init__('Main menu')

    def create_options(self):
        return [
            {'text': 'Settings', 'callback_data': 'settings_menu'},
            # ...
        ]

    def message_handler(self):
        pass
