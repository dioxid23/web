from typing import List

from fastapi import APIRouter, UploadFile
from fastapi.params import File, Form

from db.base.services.file_service import FileService
from db.project.models import Project
from db.project.schemas import GetProject, CreateProject

router = APIRouter()


# Создание проекта
@router.post('', response_model=GetProject)
async def create(schema: CreateProject):
    project = await Project.create(**schema.dict())
    return await GetProject.from_tortoise_orm(project)


# Патч
@router.patch('/{project_id}', response_model=GetProject)
async def update(project_id: int, schema: CreateProject):
    data = schema.dict()

    await Project.filter(pk=project_id).update(**data)
    obj = Project.get(pk=project_id)

    return await GetProject.from_queryset_single(obj)


# Взять все
@router.get('', response_model=List[GetProject])
async def filter():
    return await GetProject.from_queryset(Project.all())


# Взять один
@router.get('/{project_id}', response_model=GetProject)
async def get(project_id: int):
    return await GetProject.from_queryset_single(Project.get(id=project_id))


# Удалить
@router.delete('/{project_id}')
async def delete(project_id: int):
    await Project.filter(id=project_id).delete()


# Установить превью
@router.put("/set_preview/{project_id}", response_model=GetProject)
async def set_preview(
        project_id: int,
        preview: UploadFile = File(...),
        postfix: str = Form(...)
):
    project = await Project.get(id=project_id)
    file_scheme = await FileService.save_file(preview, postfix)

    project.preview_id = file_scheme.id
    await project.save()

    return await GetProject.from_tortoise_orm(project)


# Установить основную картинку

@router.put("/set_image/{project_id}", response_model=GetProject)
async def set_image(
        project_id: int,
        image: UploadFile = File(...),
        postfix: str = Form(...)
):
    project = await Project.get(id=project_id)
    file_scheme = await FileService.save_file(image, postfix)

    project.image_id = file_scheme.id
    await project.save()

    return await GetProject.from_tortoise_orm(project)
