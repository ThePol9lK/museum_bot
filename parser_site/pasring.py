import json
import os

import requests


from config_data.config import VK_TOKEN, GROUP_NAME


class ParserVK:
    @staticmethod
    def read_news_json() -> None:
        """
        Читает значения в answer.json

        :return:
        """
        with open('parser_site/answer.json', 'r', encoding="utf-8") as fcc_file:
            fcc_data = json.load(fcc_file)
        return fcc_data

    @staticmethod
    def save_news_json(fresh_posts_id) -> None:
        """
        Сохраняет значения в answer.json

        :return:
        """

        with open(f"parser_site/answer.json", "w", encoding="utf-8") as file:
            json.dump(fresh_posts_id, file, indent=4, ensure_ascii=False)

    @staticmethod
    def first_request():
        """
        Собираем значения для вывода информации

        :return:
        """
        url = f"https://api.vk.com/method/wall.get?domain={GROUP_NAME}&count=11&access_token={VK_TOKEN}&v=5.131"

        req = requests.get(url)
        src = req.json()

        #проверяем существует ли директория с именем группы
        if os.path.exists(f"parser_site/{GROUP_NAME}"):
            print(f"Директория с именем {GROUP_NAME} уже существует!")
        else:
            os.mkdir(f'parser_site/{GROUP_NAME}')

        # сохраняем данные в json файл, чтобы видеть структуру
        with open(f"parser_site/{GROUP_NAME}/{GROUP_NAME}.json", "w", encoding="utf-8") as file:
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
        if not os.path.exists(f"parser_site/{GROUP_NAME}/exist_posts_{GROUP_NAME}.txt"):
            print("Файла с ID постов не существует, создаём файл!")

            with open(f"parser_site/{GROUP_NAME}/exist_posts_{GROUP_NAME}.txt", "w") as file:
                for item in fresh_posts_id:
                    file.write(str(item) + "\n")

    @staticmethod
    def news_answer():
        """
        Собираем значения для вывода информации

        :return:
        """

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

        ParserVK.save_news_json(fresh_posts_id)
