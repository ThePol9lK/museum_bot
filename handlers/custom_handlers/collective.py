import json

from keyboards.inline.collective_kb import kinds_collective_kb
from loader import bot

from telebot.types import Message, CallbackQuery, InputMediaPhoto
from database.CRUD import get_all_collective
from keyboards.inline.pagination_first import pagination_first
from keyboards.inline.pagination_last import pagination_last
from keyboards.inline.pagination_others import pagination_others


@bot.message_handler(commands=["collective"])
def display_posters(message: Message):
    """

    :param message:
    :return:
    """
    bot.send_message(message.chat.id, 'Выберите коллектив', reply_markup=kinds_collective_kb())

@bot.callback_query_handler(func=lambda call: True)
def display_posters(call: CallbackQuery):
    all_collective = get_all_collective(call.data)

    bot.send_photo(chat_id=call.message.chat.id,
                   photo=all_collective[0].image,
                   caption=f'{all_collective[0].name}\n{all_collective[0].description}',
                   reply_markup=pagination_first(
                       count=len(all_collective),
                       page=0,
                       key='collective',
                       link=all_collective[0].link
                   )
                   )

# @bot.callback_query_handler(func=lambda call: call.data.startswith('{"KeyPage":"collective"'))
# def callback_query_pagination(call: CallbackQuery) -> None:
#
#     json_string = json.loads(call.data)
#     count = json_string['NumberPage']
#     key = json_string['KeyPage']
#
#     all_collective = get_all_collective(call.data)
#     poster_photo = all_collective[count].image
#     caption = f'{all_collective[count].name}\n Возраст - {all_collective[count].age}\n Курсы: {all_collective[count].courses}'
#     link = all_collective[count].link
#
#     media = InputMediaPhoto(poster_photo, caption=caption)
#
#     if count == 0:
#         keyboard = pagination_first(
#                        count=len(all_collective),
#                        page=count,
#                        key=key,
#                        link=link,
#                    )
#
#     elif count == len(all_collective)-1:
#         keyboard = pagination_last(
#             count=len(all_collective),
#             page=count,
#             key=key,
#             link=link
#         )
#
#     else:
#         keyboard = pagination_others(
#             count=len(all_collective),
#             page=count,
#             key=key,
#             link=link
#         )
#
#     bot.edit_message_media(media=media,
#                            chat_id=call.message.chat.id,
#                            message_id=call.message.message_id,
#                            reply_markup=keyboard)

