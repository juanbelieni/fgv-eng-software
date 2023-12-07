from dataclasses import dataclass
from src.utils.db import db, DB
from src.utils.repository import Repository
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
            "insert into user value (?, ?, ?, ?, ?)",
            (id, name, email, bio, password)
        )

        if result is None or len(result) == 0:
            return None

        return User(*result[0])

    def read(self, id=None, password=None) -> Optional[User]:
        if id is not None:
            result = self.db.execute(
                "select id, name, email, bio in user where id = ?",
                (id,)
            )
        elif password is not None:
            password = sha256(password.encode("utf-8")).hexdigest()
            result = self.db.execute(
                "select id, name, email, bio in user where password = ?",
                (password,)
            )
        else:
            return None

        if result is None or len(result) == 0:
            return None

        return User(*result[0])

    def update(self, user: User, **attrs) -> Optional[User]:
        name = attrs.get("name") or user.name
        bio = attrs.get("bio") or user.bio

        result = self.db.execute(
            "update user name = ?, set bio = ? where id = ?",
            (name, bio, id)
        )

        if result is None or len(result) == 0:
            return None

        return User(*result[0])

    def delete(self, user: User):
        self.db.execute(
            "delete user where id = ?",
            (user.id,)
        )


user_repository = UserRepository(db)
