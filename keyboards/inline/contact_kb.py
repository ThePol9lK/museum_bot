from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def keyboard_contacts() -> InlineKeyboardMarkup:
    """
    Клавиатура для вывода клавиатуры с ссылками информации о сайтах

    :return: InlineKeyboardMarkup
    """
    CONTACTS_DICT = {
        "В контакте": "https://vk.com/cdk_orevo",
        "Сайт": "https://xn----dtbecebkckn9b9a2d.xn--p1ai/"
    }

    return InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(
                    text=button,
                    url=CONTACTS_DICT[button]
                )
            ] for button in CONTACTS_DICT
        ]
    )

