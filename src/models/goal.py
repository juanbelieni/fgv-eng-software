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
    public: bool
    book: str
    password: str


class GoalRepository(Repository):
    db: DB

    def __init__(self, db: DB):
        self.db = db

    def create(self, **attrs) -> Optional[Goal]:
        id = str(uuid4())
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

        return Goal(*result[0])

    def read(): ...

    def update(): ...

    def delete(): ...


goal_repository = GoalRepository(db)