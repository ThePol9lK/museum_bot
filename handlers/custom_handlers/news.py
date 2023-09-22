from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["news"])
def display_contacts(message: Message):
    """

    :param message:
    :return:
    """
    bot.send_message(message.chat.id, "Последние новости:")
