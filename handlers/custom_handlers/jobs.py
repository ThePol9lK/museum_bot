from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["jobs"])
def display_contacts(message: Message):
    """

    :param message:
    :return:
    """
    bot.send_message(message.chat.id,
                     "<b>Время работы администрации:</b> понедельник-четверг с 09.00 до 18.00, пятница с 09.00 до "
                     "17.00.\n "
                     "<b>Обед</b> с 13.00 до 14.00.\n"
                     "<b>Время работы кассы:</b> ежедневно с 12:00 до 19.00",
                     parse_mode="HTML")
