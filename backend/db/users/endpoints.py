from fastapi import APIRouter, Depends

from db.users.models import User, UserModel
from db.users.schemas import GetUserDetail
from db.users.services.services import fastapi_users_service, cookie_authentication, SECRET

auth_router = fastapi_users_service.get_auth_router(cookie_authentication)
register_router = fastapi_users_service.get_register_router()
reset_password_router = fastapi_users_service.get_reset_password_router(SECRET)

user_router = APIRouter()
user_router.include_router(auth_router, prefix="/auth")
user_router.include_router(register_router, prefix="/auth")


@user_router.get("/me", response_model=GetUserDetail)
async def get_me(user: User = Depends(fastapi_users_service.get_current_active_user)):
    user_model = await UserModel.get(id=user.id)
    return await GetUserDetail.from_tortoise_orm(user_model)
