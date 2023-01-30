data = {
    "users": [
        {
            "id": 1,
            "name": "John Doe",
            "email": "teste@gmail.com",
            "password": "12345678",
        }
    ],
}


class DatabaseInMemory:
    _db = data
    _query = []

    def users(self):
        self._query = self._db["users"]
        return self

    def findById(self, id: int):
        return filter(lambda table: table["id"] == id, self._query)

    def findByEmail(self, email: str):
        user = list(filter(lambda table: table["email"] == email, self._query))

        return dict(user[0]) if user else None

    def create(self, data):
        data = dict(data, id=len(self._query) + 1)

        self._query.append(data)

        return data
