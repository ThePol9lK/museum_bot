from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def pagination_first(count: int, page: int, key: str, link: str = None,
                     link_second: str = None) -> InlineKeyboardMarkup:
    """
    Клавиатура пагинация для вывода фото (на первое фото)

    :param count:
    :param page:
    :param key:
    :param link:
    :param link_second:
    :return:
    """

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text=f'{page+1}/{count}', callback_data=f' '),

        InlineKeyboardButton(text=f'Следующее',
                             callback_data="{\"KeyPage\":" + '"' + key + '"' + ",\"NumberPage\":" + str(page + 1) + "}")
    )

    if link:
        markup.add(InlineKeyboardButton(text='Больше информации', url=f'{link}'))

    if link_second:
        markup.add(InlineKeyboardButton(text='Купить билет', url=f'{link_second}'))

    return markup
