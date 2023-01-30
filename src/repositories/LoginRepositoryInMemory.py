from database.DatabaseInMemory import DatabaseInMemory


class LoginRepositoryInMemory:
    def __init__(self):
        self._db = DatabaseInMemory()

    def findById(self, id: int):
        return self._db.users().findById(id)

    def findByEmail(self, email: str):
        return self._db.users().findByEmail(email)

    def create(self, data: dict):
        return self._db.users().create(data)
