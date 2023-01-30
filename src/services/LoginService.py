from repositories.LoginRepositoryInMemory import LoginRepositoryInMemory


class LoginService:
    def __init__(self):
        self._login_repository = LoginRepositoryInMemory()

    def signin(self, credentials):
        user = self._login_repository.findByEmail(credentials.email)
        credentials = dict(credentials)

        if user is None:
            return {}

        if user.get("password") != credentials.get("password"):
            return {"error": "Invalid password"}

        return user

    def signup(self, credentials):
        user = self._login_repository.findByEmail(credentials.email)
        credentials = dict(credentials)

        if credentials.get("password") != credentials.get("confirmPassword"):
            return {"error": "Passwords do not match"}

        if user is not None:
            return {"error": "Email already registered"}

        user = self._login_repository.create(credentials)

        return user
