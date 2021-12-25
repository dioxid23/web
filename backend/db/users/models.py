from fastapi_users.db import TortoiseBaseUserModel, TortoiseUserDatabase
from fastapi_users import models
from tortoise import fields, Tortoise
from typing import Optional

from tortoise.contrib.pydantic import PydanticModel

from config import DBPaths


class UserModel(TortoiseBaseUserModel):
    first_name = fields.CharField(max_length=150, default="", description="Имя")
    last_name = fields.CharField(max_length=150, default="", description="Фамилия")

    class PydanticMeta:
        include = ('id', 'first_name', 'last_name')


Tortoise.init_models(DBPaths.users, 'models')


class User(models.BaseUser):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
        orig_model = UserModel


class UserCreate(models.BaseUserCreate):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
        orig_model = UserModel


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB, PydanticModel):
    pass


user_db = TortoiseUserDatabase(UserDB, UserModel)
