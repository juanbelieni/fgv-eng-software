from dataclasses import dataclass
from src.utils.db import db, DB
from src.utils.repository import Repository
from typing import Optional


@dataclass
class Progress:
    user: str
    goal: str
    percent: float


class ProgressRepository(Repository):
    db: DB

    def __init__(self, db: DB):
        self.db = db

    def create(self, **attrs) -> Optional[Progress]:
        user = attrs.get("user")
        goal = attrs.get("goal")
        percent = attrs.get("percent")

        result = self.db.execute(
            "insert into progress value (?, ?, ?)",
            (user, goal, percent)
        )

        if result is None or len(result) == 0:
            return None

        return Progress(*result[0])

    def read(self, user:str=None, goal:str=None) -> Optional[Progress]:
        if user is not None and goal is not None:
            result = self.db.execute(
                "select user, goal, percent from progress where user = ? and goal = ?",
                (user, goal)
            )
        else:
            return None

        if result is None or len(result) == 0:
            return None

        return Progress(*result[0])

    def update(self, **attrs) -> Optional[Progress]:
        user = attrs.get("user")
        goal = attrs.get("goal")
        percent = attrs.get("percent")

        result = self.db.execute(
            "update progress set percent = ? where user = ? and goal = ?",
            (percent, user, goal)
        )

        if result is None or len(result) == 0:
            return None

        return Progress(*result[0])

    def delete(self, progress: Progress):
        self.db.execute(
            "delete from progress where progress.user = ? and progress.goal = ?",
            (progress.user, progress.goal,)
        )


progress_repository = ProgressRepository(db)