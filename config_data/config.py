import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():  # поиск env файла
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()  # загрузка env файла

BOT_TOKEN = os.getenv("BOT_TOKEN")
VK_TOKEN = os.getenv("VK_TOKEN")
EMAIL = os.getenv("EMAIL")
PASSWORD_EMAIL = os.getenv("PASSWORD_EMAIL")
GROUP_NAME = os.getenv("GROUP_NAME")

# Команды для бота
COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("anketa", "Обратная связь"),
    ("collective", "Вывести коллективы"),
    ("contacts", "Вывод информации о контактах ЦДК 'Созвездие'"),
    ("jobs", "Вывод информации о работы ЦДК 'Созвездие'"),
    ("news", "Вывод новстей"),
    ("poster", "Вывод афиши"),
    ("teacher", "Вывод учителей")
)
