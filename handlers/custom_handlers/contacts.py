from telebot.types import Message

from keyboards.inline.contact_kb import keyboard_contacts
from loader import bot


@bot.message_handler(commands=["contacts"])
def display_contacts(message: Message):
    """

    :param message:
    :return:
    """
    bot.send_message(message.chat.id,
                     '141800, Московская область, г. Дмитров, ул. Загорская, д. 64\n'
                     '<b>Администратор:</b> <a href="tel:84962234418">8(496) 223-44-18</a>\n'
                     '<b>Директор:</b> 8(495) 993-93-86, MutkovkinaNV@mosreg.ru\n'
                     '<b>Заместитель директора по коммерческой работе:</b> 8(495)993-93-86\n'
                     '<b>Культурно-досуговый отдел:</b> 8(495) 993-94-24\n'
                     '<b>Электронная почта:</b> dm-prazdnik@mail.ru',
                     parse_mode="HTML",
                     reply_markup=keyboard_contacts()
                     )
