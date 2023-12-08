from dataclasses import dataclass
from src.utils.db import db, DB
from src.utils.repository import Repository
from typing import Optional
from uuid import uuid4
from hashlib import sha256


@dataclass
class Progress:
    user: str
    goal: str
    page: int


class ProgressRepository(Repository):
    db: DB

    def __init__(self, db: DB):
        self.db = db

    def create(self, **attrs) -> Optional[Progress]:
        user = attrs.get("user")
        goal = attrs.get("goal")
        page = attrs.get("page")

        result = self.db.execute(
            "insert into progress value (?, ?, ?, ?, ?)",
            (user, goal, page)
        )

        if result is None or len(result) == 0:
            return None

        return Progress(
            user=result[0][0],
            goal=result[0][1],
            page=result[0][2],
        )

    def read(): ...

    def update(): ...

    def delete(): ...


goal_repository = GoalRepository(db)