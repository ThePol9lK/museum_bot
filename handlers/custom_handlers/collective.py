import json

from keyboards.inline.collective_kb import kinds_collective_kb
from loader import bot

from telebot.types import Message, CallbackQuery, InputMediaPhoto
from database.CRUD import get_all_collective
from keyboards.inline.pagination_first import pagination_first
from keyboards.inline.pagination_last import pagination_last
from keyboards.inline.pagination_others import pagination_others


@bot.message_handler(commands=["collective"])
def display_collectives(message: Message):
    """
    Обработка команды collective.

    :param message: Message
    :return:
    """
    bot.send_message(message.chat.id, 'Выберите коллектив', reply_markup=kinds_collective_kb())


@bot.callback_query_handler(func=lambda call: call.data == '1' or call.data == '2')
def display_posters(call: CallbackQuery):
    """
    Обработка на команду выбор вида коллективов

    :param call: CallbackQuery
    :return:
    """
    all_collective = get_all_collective(int(call.data))

    bot.send_photo(chat_id=call.message.chat.id,
                   photo=all_collective[0].image,
                   caption=f'{all_collective[0].name}\n{all_collective[0].description}',
                   reply_markup=pagination_first(
                       count=len(all_collective),
                       page=0,
                       key='collective',
                       key_2=call.data,
                       link=all_collective[0].link
                   )
                   )


@bot.callback_query_handler(func=lambda call: call.data.startswith('{"KeyPage":"collective"'))
def callback_query_pagination(call: CallbackQuery) -> None:
    """
    Обработка пагинации на команду collective

    :param call: CallbackQuery
    :return:
    """
    json_string = json.loads(call.data)
    count = json_string['NumberPage']
    key = json_string['KeyPage']
    key_2 = json_string['Key']

    all_collective = get_all_collective(int(key_2))
    poster_photo = all_collective[count].image
    caption = f'{all_collective[count].name}\n{all_collective[count].description}'
    link = all_collective[count].link

    media = InputMediaPhoto(poster_photo, caption=caption)

    if count == 0:
        keyboard = pagination_first(
            count=len(all_collective),
            page=count,
            key=key,
            link=link,
            key_2=key_2
        )

    elif count == len(all_collective) - 1:
        keyboard = pagination_last(
            count=len(all_collective),
            page=count,
            key=key,
            link=link,
            key_2=key_2
        )

    else:
        keyboard = pagination_others(
            count=len(all_collective),
            page=count,
            key=key,
            link=link,
            key_2=key_2
        )

    bot.edit_message_media(media=media,
                           chat_id=call.message.chat.id,
                           message_id=call.message.message_id,
                           reply_markup=keyboard)
