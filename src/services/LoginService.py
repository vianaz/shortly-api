from fastapi import HTTPException
from libs import crypt

from repositories.LoginRepositoryInMemory import LoginRepositoryInMemory


class LoginService:
    def __init__(self):
        self._login_repository = LoginRepositoryInMemory()

    def signin(self, credentials):
        user = self._login_repository.findByEmail(credentials.email)

        if user is None:
            raise HTTPException(status_code=401, detail="Invalid email")

        is_invalid_password = not crypt.decrypt(
            credentials.password, str(user.get("password"))
        )

        if is_invalid_password:
            raise HTTPException(status_code=401, detail="Invalid password")

        return "Logged in successfully"

    def signup(self, credentials):
        user = self._login_repository.findByEmail(credentials.email)
        credentials = dict(credentials)

        if credentials.get("password") != credentials.get("confirmPassword"):
            raise HTTPException(status_code=401, detail="Passwords do not match")

        if user is not None:
            raise HTTPException(status_code=401, detail="User already exists")

        credentials = {
            "name": credentials.get("name"),
            "email": credentials.get("email"),
            "password": crypt.encrypt(str(credentials.get("password"))),
        }

        self._login_repository.create(credentials)

        return "User created successfully"
