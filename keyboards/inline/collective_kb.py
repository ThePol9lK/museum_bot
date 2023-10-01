from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.CRUD import get_all_kinds_collective


def kinds_collective_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура для вывода клавиатуры с категориями коллективов

    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    return InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(
                    text=cat.name,
                    callback_data=cat.id
                )
            ] for cat in get_all_kinds_collective()
        ]
    )
