import json

from telebot.types import Message, CallbackQuery, InputMediaPhoto

from keyboards.inline.pagination_first import pagination_first
from keyboards.inline.pagination_last import pagination_last
from keyboards.inline.pagination_others import pagination_others
from loader import bot
from parser_site.pasring import ParserVK


@bot.message_handler(commands=["news"])
def display_news(message: Message):
    """
    Обработка команды news.

    :param message: Message
    :return:
    """
    ParserVK.first_request()
    ParserVK.news_answer()
    news = ParserVK.read_news_json()

    count = len(news)

    news_key = list(news.keys())[0]

    bot.send_photo(chat_id=message.chat.id,
                   photo=news[news_key][0],
                   caption=news[news_key][1][:1024],
                   reply_markup=pagination_first(
                       count=count,
                       page=0,
                       key='news',
                       link=news[news_key][2]
                   )
                   )


@bot.callback_query_handler(func=lambda call: call.data.startswith('{"KeyPage":"news"'))
def callback_query_pagination(call: CallbackQuery) -> None:
    """
    Обработка пагинации на команду news

    :param call: CallbackQuery
    :return:
    """
    json_string = json.loads(call.data)
    page = json_string['NumberPage']
    key = json_string['KeyPage']

    news = ParserVK.read_news_json()
    news_key = list(news.keys())[page]
    count = len(news)

    media = InputMediaPhoto(news[news_key][0], caption=news[news_key][1][:1024])
    link = news[news_key][2]

    if page == 0:
        keyboard = pagination_first(
            count=count,
            page=page,
            key=key,
            link=link
        )

    elif page == count-1:
        keyboard = pagination_last(
            count=count,
            page=page,
            key=key,
            link=link
        )

    else:
        keyboard = pagination_others(
            count=count,
            page=page,
            key=key,
            link=link
        )

    bot.edit_message_media(media=media,
                           chat_id=call.message.chat.id,
                           message_id=call.message.message_id,
                           reply_markup=keyboard)
