import peewee

db = peewee.SqliteDatabase('bot.db')


class ModelBase(peewee.Model):
    """
    Базовый класс для таблиц

    id:AutoField() - для таблицы
    """
    id = peewee.AutoField()

    class Meta:
        database = db


class Poster(ModelBase):
    """
    Таблица Афиша

    title:CharField() - имя афиши
    description:TextField() - описание афиши
    image:CharField() - фото афиши
    link:CharField() - адрес на сайте для афиши
    buy_ticket:CharField() - второй адрес на сайте для афиши
    """
    title = peewee.CharField()
    description = peewee.TextField()
    image = peewee.CharField()
    link = peewee.CharField()
    buy_ticket = peewee.CharField()


class Teacher(ModelBase):
    """
    Таблица Учителей

    name:CharField()- имя учителя
    age:IntegerField() - возраст учителя
    image:CharField() - фото учителя
    link:CharField() - адрес на сайте для учителя
    courses:CharField() - курсы, которые преподают учителя
    """
    name = peewee.CharField()
    age = peewee.IntegerField()
    image = peewee.CharField()
    link = peewee.CharField()
    courses = peewee.CharField()


class KindsCollective(ModelBase):
    """
    Таблица Виды Коллективов

    name:CharField()- имя вида коллектива
    """
    name = peewee.CharField()


class Collective(ModelBase):
    """
    Таблица Коллективов

    name:CharField() - имя коллектива
    description:TextField() - описание коллектива
    image:CharField() - фото коллектива
    link:CharField() - - ссылка на сайт коллектива
    category:ForeignKeyField(KindsCollective) - категория вида коллектива
    """
    name = peewee.CharField()
    description = peewee.TextField()
    image = peewee.CharField()
    link = peewee.CharField()
    category = peewee.ForeignKeyField(KindsCollective)

