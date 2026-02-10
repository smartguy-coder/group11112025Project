from fastapi import Request, Depends

from apps.core.base_model import async_session_maker


async def get_data_first():
    return 30


async def get_data(request: Request, first=Depends(get_data_first)):
    print(request)
    return 444+first


async def get_session():
    async with async_session_maker() as session:
        yield session
