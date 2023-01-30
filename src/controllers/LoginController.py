from fastapi import APIRouter
from pydantic import BaseModel


from src.services.LoginService import LoginService

router = APIRouter()


login_service = LoginService()


class SignupBody(BaseModel):
    email: str
    password: str
    confirmPassword: str


class SigninBody(BaseModel):
    email: str
    password: str


@router.post("/signup")
async def signup(body: SignupBody):
    return login_service.signup(body)


@router.post("/signin")
async def signin(body: SigninBody):
    return login_service.signin(body)
