import shutil

from typing import Optional
from uuid import uuid4

from fastapi import UploadFile

from config import MediaPath
from db.base.models import File
from db.base.schemas import GetFile


class FileService:

    @staticmethod
    def _os_file_save(file, file_path):
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file, buffer)

    @staticmethod
    async def save_file(
            file: Optional[UploadFile],
            postfix: str
    ) -> GetFile:

        path = f'{MediaPath.path}/{uuid4()}.{postfix}'

        file_object = file.file

        FileService._os_file_save(file_object, path)

        new_file = await File.create(path=path)
        return await GetFile.from_tortoise_orm(new_file)
