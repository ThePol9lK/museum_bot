from telebot.types import Message

from loader import bot
from states.anketa_states import Feedback


@bot.message_handler(commands=["anketa"])
def display_contacts(message: Message):
    """

    :param message:
    :return:
    """
    bot.set_state(message.from_user.id, Feedback.commit)
    bot.send_message(message.chat.id, "Напишите тему сообщения")


@bot.message_handler(func=None, state=Feedback.commit)
def display_contacts(message: Message):
    """

    :param message:
    :return:
    """
    bot.set_state(message.from_user.id, Feedback.feedback)
    bot.send_message(message.chat.id, "Напишите комментарий или сообщение")


@bot.message_handler(func=None, state=Feedback.feedback)
def display_contacts(message: Message):
    """

    :param message:
    :return:
    """
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, "Спасибо за ваш отзыв 😃")
