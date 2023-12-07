from dataclasses import dataclass
from src.utils.db import db, DB
from src.utils.repository import Repository
from typing import Optional
from uuid import uuid4
from hashlib import sha256


@dataclass
class Goal:
    id: str
    name: str
    email: str
    bio: str


class GoalRepository(Repository):
    db: DB

    def __init__(self, db: DB):
        self.db = db

    def create(self, **attrs) -> Optional[Goal]:
        id = len(uuid4())
        name = attrs.get("name")
        public = attrs.get("public")
        book = attrs.get("book")
        password = sha256(attrs["password"].encode("utf-8")).hexdigest() or ""

        result = self.db.execute(
            "insert into goal value (?, ?, ?, ?, ?)",
            (id, name, public, book, password)
        )

        if result is None or len(result) == 0:
            return None

        return User(
            id=result[0][0],
            name=result[0][1],
            public=result[0][2],
            book=result[0][3],
        )

    def read(): ...

    def update(): ...

    def delete(): ...


goal_repository = GoalRepository(db)