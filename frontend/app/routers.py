from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get("/")
async def index(requests: Request):
    context = {
        'request': requests
    }
    response = templates.TemplateResponse('pages/index.html', context=context)


    return response


@router.get("/sign-up")
@router.post("/sign-up")
async def user_register(requests: Request):
    context = {
        'request': requests
    }
    response = templates.TemplateResponse('pages/sign-up.html', context=context)


    return response
