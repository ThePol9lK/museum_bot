from telebot.types import Message

from keyboards.inline.contact_kb import keyboard_contacts
from loader import bot


@bot.message_handler(commands=["contacts"])
def display_contacts(message: Message):
    """
    Функция для вывода информации о контактах ЦДК 'Созвездие'

    :param message: Message
    :return:
    """
    bot.send_message(message.chat.id,
                     '141800, Московская область, г. Дмитров, ул. Загорская, д. 64\n'
                     '<b>Администратор:</b> <a href="+74962234418">+74962234418</a>\n'
                     '<b>Директор:</b> <a href="+74959939386">+74959939386</a>, MutkovkinaNV@mosreg.ru\n'
                     '<b>Заместитель директора по коммерческой работе:</b> <a href="+74959939386">+74959939386</a>\n'
                     '<b>Культурно-досуговый отдел:</b> <a href="+74959939424">+74959939424</a>\n'
                     '<b>Электронная почта:</b> dm-prazdnik@mail.ru',
                     parse_mode="HTML",
                     reply_markup=keyboard_contacts()
                     )
