import json
from loader import bot

from telebot.types import Message, CallbackQuery, InputMediaPhoto
from database.CRUD import get_all_teachers
from keyboards.inline.pagination_first import pagination_first
from keyboards.inline.pagination_last import pagination_last
from keyboards.inline.pagination_others import pagination_others


@bot.message_handler(commands=["teacher"])
def display_posters(message: Message):
    """

    :param message:
    :return:
    """
    all_teachers = get_all_teachers()

    bot.send_photo(chat_id=message.chat.id,
                   photo=all_teachers[0].image,
                   caption=f'{all_teachers[0].name}\nВозраст - {all_teachers[0].age}\nКурсы: {all_teachers[0].courses}',
                   reply_markup=pagination_first(
                       count=len(all_teachers),
                       page=0,
                       key='teacher',
                       link=all_teachers[0].link
                   )
                   )


@bot.callback_query_handler(func=lambda call: call.data.startswith('{"KeyPage":"teacher"'))
def callback_query_pagination(call: CallbackQuery) -> None:
    json_string = json.loads(call.data)
    count = json_string['NumberPage']
    key = json_string['KeyPage']
    all_teachers = get_all_teachers()
    print(type(all_teachers))
    poster_photo = all_teachers[count].image
    caption = f'{all_teachers[count].name}\n Возраст - {all_teachers[count].age}\n Курсы: {all_teachers[count].courses}'
    link = all_teachers[count].link

    media = InputMediaPhoto(poster_photo, caption=caption)

    if count == 0:
        keyboard = pagination_first(
            count=len(all_teachers),
            page=count,
            key=key,
            link=link,
        )

    elif count == len(all_teachers) - 1:
        keyboard = pagination_last(
            count=len(all_teachers),
            page=count,
            key=key,
            link=link
        )

    else:
        keyboard = pagination_others(
            count=len(all_teachers),
            page=count,
            key=key,
            link=link
        )

    bot.edit_message_media(media=media,
                           chat_id=call.message.chat.id,
                           message_id=call.message.message_id,
                           reply_markup=keyboard)
