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
        id = len(uuid4())
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

        return User(
            id=result[0][0],
            name=result[0][1],
            email=result[0][2],
            bio=result[0][3],
        )

    def read(): ...

    def update(): ...

    def delete(): ...


user_repository = UserRepository(db)
