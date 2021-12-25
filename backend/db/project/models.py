from tortoise import Tortoise, fields, models

from config import DBPaths

Tortoise.init_models(DBPaths.project, 'models')


class Project(models.Model):
    id = fields.BigIntField(pk=True)

    name = fields.CharField(max_length=150, default="", description="Название")
    city = fields.CharField(max_length=100, default="", description="Город")
    address = fields.CharField(max_length=100, default="", description="Адрес")
    title = fields.CharField(max_length=100, default="", description="Заголовок")
    description = fields.CharField(max_length=100, default="", description="Описание")

    type = fields.CharField(max_length=100, default="", description="Класс")
    square = fields.FloatField(default=0, description="Площадь")
    count_levels = fields.IntField(default=0, description="Количество этажей")
    year = fields.IntField(default=0, description="Год сдачи")

    preview = fields.ForeignKeyField(
        'models.File', related_name='previewed', on_delete=fields.SET_NULL,
        null=True, default=None, description='Превью'
    )

    image = fields.ForeignKeyField(
        'models.File', related_name='imaged', on_delete=fields.SET_NULL,
        null=True, default=None, description='Большая картинка'
    )
