from telegram import Bot


def send_message(bot: Bot, chat_id: int | str, text: str):
    bot.send_message(chat_id, text)
