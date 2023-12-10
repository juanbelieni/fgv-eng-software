from dataclasses import dataclass
from utils.db import db, DB
from utils.repository import Repository
from typing import Optional
from uuid import uuid4
from hashlib import sha256


@dataclass
class User:
    id: str
    name: str
    email: str
    bio: str


class UserRepository(Repository):
    db: DB

    def __init__(self, db: DB):
        self.db = db

    def create(self, **attrs) -> Optional[User]:
        id = str(uuid4())
        name = attrs.get("name")
        email = attrs.get("email")
        bio = attrs.get("bio") or ""
        password = sha256(attrs["password"].encode("utf-8")).hexdigest()

        result = self.db.execute(
            "insert into user values (?,?,?,?,?)",
            (id, name, email, bio, password)
        )

        if result is None:
            return None

        return self.read(id=id)

    def read(self, **attrs) -> Optional[User]:
        wheres = []
        params = tuple()

        for key, value in attrs.items():
            if key == "password":
                value = sha256(value.encode("utf-8")).hexdigest()

            wheres.append(f"{key} = ?")
            params = (*params, value)

        where = " and ".join(wheres)

        result = self.db.execute(
            f"select id, name, email, bio from user where {where}",
            params
        )

        if result is None or len(result) == 0:
            return None

        return User(*result[0])

    def list(self): ...

    def update(self, user: User, **attrs) -> Optional[User]:
        name = attrs.get("name") or user.name
        bio = attrs.get("bio") or user.bio

        result = self.db.execute(
            "update user set name = ?, bio = ? where id = ?",
            (name, bio, user.id)
        )

        if result is None:
            return None

        return self.read(id=user.id)

    def delete(self, user: User):
        self.db.execute(
            "delete user where id = ?",
            (user.id,)
        )


user_repository = UserRepository(db)
