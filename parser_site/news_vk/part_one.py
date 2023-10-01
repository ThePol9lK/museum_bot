import json
import os

import requests


from config_data.config import VK_TOKEN, GROUP_NAME


# class ParserVK:
#     url = f"https://api.vk.com/method/wall.get?domain={GROUP_NAME}&count=11&access_token={VK_TOKEN}&v=5.131"
#
#     def read_news_json(self) -> None:
#         """
#         Читает значения в answer.json
#
#         :return:
#         """
#         with open('parser_site/answer.json', 'r', encoding="utf-8") as fcc_file:
#             fcc_data = json.load(fcc_file)
#         return fcc_data
#
#     def save_news_json(self, fresh_posts_id) -> None:
#         """
#         Сохраняет значения в answer.json
#
#         :return:
#         """
#
#         with open(f"parser_site/answer.json", "w", encoding="utf-8") as file:
#             json.dump(fresh_posts_id, file, indent=4, ensure_ascii=False)
#
#     def news_answer(self):
#         """
#
#
#         :return:
#         """
#         with open(f'parser_site/{GROUP_NAME}/{GROUP_NAME}.json', 'r', encoding="utf-8") as fcc_file:
#             fcc_data = json.load(fcc_file)
#
#         fresh_posts_id = {}
#         posts = fcc_data["response"]["items"]
#
#         for count in range(1, 11):
#
#             fresh_post_id = posts[count]
#             posts_id = posts[count]["id"]
#             posts_text = posts[count]['text']
#             url = f"https://vk.com/wall{posts[count]['from_id']}_{posts_id}"
#
#             if "copy_history" in fresh_post_id:
#                 continue
#
#             elif "attachments" in fresh_post_id:
#
#                 photo_quality = [
#                     "w",
#                     "z",
#                     "y"
#                 ]
#
#                 post = fresh_post_id["attachments"]
#                 if post[0]['type'] == 'photo':
#                     post_photo = ''
#
#                     for pq in photo_quality:
#                         break_out_flag = False
#                         for i in range(len(post[0]["photo"]["sizes"])):
#                             if pq in post[0]["photo"]["sizes"][i]['type']:
#                                 post_photo = post[0]["photo"]["sizes"][i]['url']
#
#                                 break_out_flag = True
#                                 break
#                         if break_out_flag:
#                             break
#                     fresh_posts_id[posts_id] = post_photo, posts_text, url
#
#                 elif post[0]['type'] == 'video':
#                     continue
#
#         self.save_news_json(fresh_posts_id)


def get_wall_posts():
    group_name = 'cdk_sozvezdie'
    url = f"https://api.vk.com/method/wall.get?domain={GROUP_NAME}&count=11&access_token={VK_TOKEN}&v=5.131"
    req = requests.get(url)
    src = req.json()

    # проверяем существует ли директория с именем группы
    if os.path.exists(f"{group_name}"):
        print(f"Директория с именем {group_name} уже существует!")
    else:
        os.mkdir(group_name)

    # сохраняем данные в json файл, чтобы видеть структуру
    with open(f"{group_name}/{group_name}.json", "w", encoding="utf-8") as file:
        json.dump(src, file, indent=4, ensure_ascii=False)

    # собираем ID новых постов в список
    fresh_posts_id = []
    posts = src["response"]["items"]

    for fresh_post_id in posts:
        fresh_post_id = fresh_post_id["id"]
        fresh_posts_id.append(fresh_post_id)

    """Проверка, если файла не существует, значит это первый
    парсинг группы(отправляем все новые посты). Иначе начинаем
    проверку и отправляем только новые посты."""
    if not os.path.exists(f"{group_name}/exist_posts_{group_name}.txt"):
        print("Файла с ID постов не существует, создаём файл!")

        with open(f"{group_name}/exist_posts_{group_name}.txt", "w") as file:
            for item in fresh_posts_id:
                file.write(str(item) + "\n")

        # извлекаем данные из постов
        for post in posts:

            post_id = post["id"]
            print(f"Отправляем пост с ID {post_id}")

            try:
                if "attachments" in post:
                    post = post["attachments"]

                    # забираем фото
                    if post[0]["type"] == "photo":

                        photo_quality = [
                            "photo_2560",
                            "photo_1280",
                            "photo_807",
                            "photo_604",
                            "photo_130",
                            "photo_75"
                        ]

                        if len(post) == 1:

                            for pq in photo_quality:
                                if pq in post[0]["photo"]:
                                    post_photo = post[0]["photo"][pq]
                                    print(f"Фото с расширением {pq}")
                                    print(post_photo)
                                    break
                        else:
                            for post_item_photo in post:
                                if post_item_photo["type"] == "photo":
                                    for pq in photo_quality:
                                        if pq in post_item_photo["photo"]:
                                            post_photo = post_item_photo["photo"][pq]
                                            print(f"Фото с расширением {pq}")
                                            print(post_photo)
                                            break
                                else:
                                    print("Линк или аудио пост")
                                    break

            except Exception:
                print(f"Что-то пошло не так с постом ID {post_id}!")

    else:
        print("Файл с ID постов найден, начинаем выборку свежих постов!")


def news_answer():
    with open(f'parser_site/{GROUP_NAME}/{GROUP_NAME}.json', 'r', encoding="utf-8") as fcc_file:
        fcc_data = json.load(fcc_file)

    fresh_posts_id = {}
    posts = fcc_data["response"]["items"]

    for count in range(1, 11):

        fresh_post_id = posts[count]
        posts_id = posts[count]["id"]
        posts_text = posts[count]['text']
        url = f"https://vk.com/wall{posts[count]['from_id']}_{posts_id}"

        if "copy_history" in fresh_post_id:
            continue

        elif "attachments" in fresh_post_id:

            photo_quality = [
                "w",
                "z",
                "y"
            ]

            post = fresh_post_id["attachments"]
            if post[0]['type'] == 'photo':
                post_photo = ''

                for pq in photo_quality:
                    break_out_flag = False
                    for i in range(len(post[0]["photo"]["sizes"])):
                        if pq in post[0]["photo"]["sizes"][i]['type']:
                            post_photo = post[0]["photo"]["sizes"][i]['url']

                            break_out_flag = True
                            break
                    if break_out_flag:
                        break
                fresh_posts_id[posts_id] = post_photo, posts_text, url

            elif post[0]['type'] == 'video':
                continue

    with open(f"parser_site/answer.json", "w", encoding="utf-8") as file:
        json.dump(fresh_posts_id, file, indent=4, ensure_ascii=False)


def read_news_json():
    with open('parser_site/answer.json', 'r', encoding="utf-8") as fcc_file:
        fcc_data = json.load(fcc_file)
    return fcc_data
