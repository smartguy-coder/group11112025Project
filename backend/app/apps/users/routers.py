from fastapi import APIRouter, status, Depends

from apps.core.dependencies import get_session
from apps.users.crud import user_manager
from apps.users.schemas import RegisterUserSchema, UserBaseFieldsSchema

users_router = APIRouter()


@users_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user_register_data: RegisterUserSchema, session=Depends(    get_session   )) -> UserBaseFieldsSchema:
    user = await user_manager.create_user(session=session, user_register_data=user_register_data)
    return user
