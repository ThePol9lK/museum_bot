from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

CONTACTS_DICT = {
    "В контакте": "https://vk.com/cdk_orevo",
    "Сайт": "https://xn----dtbecebkckn9b9a2d.xn--p1ai/"
}


def keyboard_contacts():
    """

    :return:
    """
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

