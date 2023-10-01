import peewee
from .models import db, Poster, Teacher, KindsCollective, Collective


def get_all_posters() -> peewee.ModelSelect:
    """
    Вывод всех значений афиш

    :return: peewee.ModelSelect
    """
    return Poster.select()


def get_all_teachers() -> peewee.ModelSelect:
    """
    Вывод всех учителей

    :return: peewee.ModelSelect
    """
    return Teacher.select()


def get_all_kinds_collective() -> peewee.ModelSelect:
    """
    Вывод всех значений видов коллективов

    :return: peewee.ModelSelect
    """
    return KindsCollective.select()


def get_all_collective(id_kinds_collective: int) -> peewee.ModelSelect:
    """
    Вывод значений всех коллективов по значение id вида коллектива

    :param id_kinds_collective:
    :return: peewee.ModelSelect
    """
    return Collective.select().where(Collective.category == id_kinds_collective)


def create_tables() -> None:
    """
    Создание таблиц для базы данных

    :return:
    """
    with db:
        db.create_tables([Poster, Teacher, KindsCollective, Collective])


db.connect()
create_tables()
