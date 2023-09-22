import lxml
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
import re
import json
import csv

# data-filter
# 18 - для взрослых
# 16 - для взрослых старше 55 лет
# 17 и 1 - для детей и подростков


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}


# URLS = ["https://xn----dtbecebkckn9b9a2d.xn--p1ai/category/lyubitelskie-obedineniya/"]
#
#
# def get_text(url: str) -> str:
#     """
#     Получение текста с сайта
#     :param url:
#     :return:
#     """
#     return requests.get(url, headers=headers).text
#
#
# #
# def save_text(scr: str) -> None:
#     """
#     Сохранение текста в файл
#     :param scr:
#     :return:
#     """
#     with open("index.html", 'w') as index:
#         index.write(scr)
#
#
# def get_text_file(file: str) -> BeautifulSoup:
#     """
#     Получение текста из файла
#     :param file:
#     :return:
#     """
#     with open(file, 'r') as index:
#         scr = index.read()
#     soup = bs(scr, "lxml")
#     return soup
#
#
# def get_filters(scr: lxml) -> set:
#     """
#
#     :param scr:
#     :return:
#     """
#     return set([filter.get("data-filter") for filter in scr])
#
#
# def save_category(scr: BeautifulSoup, filter: str) -> dict:
#     """
#
#     :param scr:
#     :param filter:
#     :return:
#     """
#     all_posts = scr.find_all('div', attrs={"data-filter": filter})
#     posts_dict = {}
#     for post in all_posts:
#         desc_post = {}
#
#         ind_post = post.find('div', attrs={"class": "ports"}).get('id')
#         hrefs_post = post.find_all('a')
#
#         photo_post = hrefs_post[0].get('href')
#         href_post = hrefs_post[1].get('href')
#         h3_post = hrefs_post[2].text
#
#         desc_post['Описание'] = h3_post
#         desc_post['Фото'] = photo_post
#         desc_post['Ссылка'] = href_post
#
#         posts_dict[ind_post] = desc_post
#     return posts_dict


# def get_info_post(posts_dict:dict):
#     decs_post_list = []
#     for key_post in posts_dict.keys():
#         decs_post_list.append(posts_dict[key_post]['Ссылка'])
#     post_con = soup.find('div', attrs={"class": "tab-content"})
#     post_c = soup.find_all('p')
#
#     post_decription = post_c[0].text + '\n' + post_c[1].text
#     post_button = soup.find('a', attrs={"class": 'wp-block-button__link'}).get('href')


# def save_json(posts_dict:dict) -> None:
#     """
#
#     :param posts_dict:
#     :return:
#     """
#
#     with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
#         json.dump(posts_dict, file, indent=4, ensure_ascii=False)


def main():
    pass


with open('index.html', 'r') as index:
    scr = index.read()
soup = bs(scr, "lxml")

all_posts = soup.find_all('div', attrs={"data-filter": "18"})
posts_dict = {}
for post in all_posts:
    desc_post = {}

    ind_post = post.find('div', attrs={"class": "ports"}).get('id')
    hrefs_post = post.find_all('a')

    photo_post = 'https://цдк-созвездие.рф' + hrefs_post[0].get('href').replace('https://xn----dtbecebkckn9b9a2d.xn--p1ai', '')
    href_post = 'https://цдк-созвездие.рф' + hrefs_post[1].get('href').replace('https://xn----dtbecebkckn9b9a2d.xn--p1ai', '')
    h3_post = hrefs_post[2].text

    desc_post['Заголовок'] = h3_post
    desc_post['Фото'] = photo_post
    desc_post['Ссылка'] = href_post

    posts_dict[ind_post] = desc_post

decs_post_list = {}
for key_post in posts_dict.keys():
    decs_post_list[key_post] = posts_dict[key_post]['Ссылка']


for i in decs_post_list.keys():
    post_content = requests.get(decs_post_list[i], headers=headers).text
    soup = bs(post_content, "lxml")

    post_con = soup.find('div', attrs={"class": "tab-content"})
    post_c = soup.find_all('p')

    post_decription = post_c[0].text + '\n' + post_c[1].text
    post_button = soup.find('a', attrs={"class": 'wp-block-button__link'}).get('href')

    posts_dict[i]['Описание'] = post_decription
    posts_dict[i]['Кнопка'] = post_button

print(posts_dict)

with open(r"answer.json", "w", encoding="utf-8") as file:
    json.dump(posts_dict, file, indent=4, ensure_ascii=False)


print(posts_dict)
