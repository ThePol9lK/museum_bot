import json
from loader import bot

from telebot.types import Message, CallbackQuery, InputMediaPhoto
from database.CRUD import get_all_posters
from keyboards.inline.pagination_first import pagination_first
from keyboards.inline.pagination_last import pagination_last
from keyboards.inline.pagination_others import pagination_others


@bot.message_handler(commands=["poster"])
def display_posters(message: Message):
    """
    Обработка команды poster.

    :param message: Message
    :return:
    """
    all_posters = get_all_posters()

    bot.send_photo(chat_id=message.chat.id,
                   photo=all_posters[0].image,
                   caption=f'{all_posters[0].title}\n {all_posters[0].description}',
                   reply_markup=pagination_first(
                       count=len(all_posters),
                       page=0,
                       key='poster',
                       link=all_posters[0].link
                   )
                   )


@bot.callback_query_handler(func=lambda call: call.data.startswith('{"KeyPage":"poster"'))
def callback_query_pagination(call: CallbackQuery) -> None:
    """
    Обработка пагинации на команду poster

    :param call: CallbackQuery
    :return:
    """
    json_string = json.loads(call.data)
    count = json_string['NumberPage']
    key = json_string['KeyPage']

    poster = get_all_posters()
    poster_photo = poster[count].image
    caption = f'{poster[count].title}\n {poster[count].description}'
    link = poster[count].link
    link_second = poster[count].buy_ticket

    media = InputMediaPhoto(poster_photo, caption=caption)

    if count == 0:
        keyboard = pagination_first(
            count=len(poster),
            page=count,
            key=key,
            link=link,
            link_second=link_second
        )

    elif count == len(poster) - 1:
        keyboard = pagination_last(
            count=len(poster),
            page=count,
            key=key,
            link=link,
            link_second=link_second
        )

    else:
        keyboard = pagination_others(
            count=len(poster),
            page=count,
            key=key,
            link=link,
            link_second=link_second
        )

    bot.edit_message_media(media=media,
                           chat_id=call.message.chat.id,
                           message_id=call.message.message_id,
                           reply_markup=keyboard)
