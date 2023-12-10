from dataclasses import dataclass
from utils.db import db, DB
from utils.repository import Repository
from typing import Optional, Generator
from uuid import uuid4



@dataclass
class Progress:
    id: str
    user: str
    book: str
    percent: float


class ProgressRepository(Repository):
    db: DB

    def __init__(self, db: DB):
        self.db = db

    def create(self, **attrs) -> Optional[Progress]:
        id = str(uuid4())
        user = attrs.get("user")
        book = attrs.get("book")
        percent = attrs.get("percent")

        result = self.db.execute(
            "insert into progress values (?, ?, ?, ?)",
            (id, user, book, percent)
        )

        if result is None:
            return None

        return self.read(id=id)

    def read(self, id=None) -> Optional[Progress]:

        result = self.db.execute(
            "select id, user, book, percent from progress where id = ?",
            (id,)
        )

        if result is None or len(result) == 0:
            return None

        return Progress(*result[0])

    def list(self, user=None) -> Optional[list[Progress]]:
        if user is None:
            return None
        
        result = self.db.execute(
            "select id, user, book, percent from progress where user = ?",
            (user,)
        )
        
        if result is None:
            return None

        return [Progress(*line) for line in result]


    def update(self, id=None, percent=None) -> Optional[Progress]:

        result = self.db.execute(
            "update progress set percent = ? where id = ?",
            (percent, id)
        )

        if result is None:
            return None

        return self.read(id=id)

    def delete(self, id=None) -> Optional[Progress]:
        self.db.execute(
            "delete from progress where id = ?",
            (id,)
        )


progress_repository = ProgressRepository(db)
