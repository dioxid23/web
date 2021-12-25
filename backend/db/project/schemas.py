from typing import Optional

from tortoise.contrib.pydantic import PydanticModel
from db.base.schemas import GetFile
from db.project.models import Project


class CreateProject(PydanticModel):
    name: str
    city: str
    address: str
    title: str
    description: str

    type: str
    square: float
    count_levels: int
    year: int

    class Config:
        orig_model = Project


class GetProject(CreateProject):
    id: int

    preview: Optional[GetFile]

    image: Optional[GetFile]
