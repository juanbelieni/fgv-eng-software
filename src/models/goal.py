from dataclasses import dataclass
from utils.db import db, DB
from utils.repository import Repository
from models.user import User
from typing import Optional
from uuid import uuid4
# from hashlib import sha256

'''
@dataclass
class Goal:
    id: str
    name: str
    public: bool
    book: str
'''


@dataclass
class Goal:
    id: str
    name: str
    host: str
    public: bool
    hidden: bool
    book: str
    deadline: str


class GoalRepository(Repository):
    db: DB

    def __init__(self, db: DB):
        self.db = db

    '''
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
    '''

    '''
    def create(self, **attrs) -> Optional[Goal]:
        id = str(uuid4())
        name = attrs.get("name")
        host = attrs.get("host")
        public = attrs.get("public")
        hidden = attrs.get("hidden")
        book = attrs.get("book")

        result = self.db.execute(
            "insert into goal value (?, ?, ?, ?, ?, ?)",
            (id, name, host, public, hidden, book)
        )

        self.db.execute(
            "insert into user_goal valeu (?, ?)",
            (host, id)
        )

        if result is None or len(result) == 0:
            return None

        return Goal(*result[0])
    '''

    def create(self, **attrs) -> Optional[Goal]:
        id = str(uuid4())
        name = attrs.get("name")
        host = attrs.get("host")
        hidden = 0
        public = attrs.get("public")
        book = attrs.get("book")
        deadline = attrs.get("deadline")

        if name == None:
            name = "Meta de leitura para " + book

        self.db.execute(
            "insert into goal values (?, ?, ?, ?, ?, ?, ?)",
            (id, name, host, public, hidden, book, deadline)
        )

        result_goal = self.db.execute(
            f"select * from goal where id = '{id}'"
        )


        if result_goal is None:
            return None

        self.db.execute(
            "insert into user_goal values (?, ?)",
            (host, id)
        )

        return Goal(*result_goal[0])

    def read(self, **attrs) -> Optional[Goal]:
        wheres = []
        params = tuple()

        for key, value in attrs.items():
            wheres.append(f"{key} = ?")
            params = (*params, value)

        where = " and ".join(wheres)

        result = self.db.execute(
            f"select * from goal where {where}",
            params
        )

        if (result is None or result == []):
            return None

        return [Goal(*result[i]) for i in range(len(result))]

    def list(): ...
      
    def update(self, goal: Goal, **attrs) -> Optional[Goal]:
        updates = []
        params = tuple()

        if (attrs.get("host") != None or
                attrs.get("book") != None):
            return None

        for key, value in attrs.items():
            updates.append(f"{key} = ?")
            params = (*params, value)

        params = (*params, goal.id)

        update = ", ".join(updates)

        self.db.execute(
            f"update goal set {update} where id = ?",
            params
        )

        result = self.db.execute(
            f"select * from goal where id = '{goal.id}'"
        )

        return Goal(*result[0])

    def change_visibility(self, goal: Goal):
        # Hide goal or make it visible again.
        if goal.hidden == 0:
            hidden = 1
        else:
            hidden = 0

        self.db.execute(
            f"update goal set hidden = ? where id = ?",
            (hidden, goal.id)
        )

        result = self.db.execute(
            f"select * from goal where id = '{goal.id}'"
        )

        return Goal(*result[0])

    def delete(self, goal: Goal):
        self.db.execute(
            "delete from goal where id = ?",
            (goal.id,)
        )

    def add_member(self, goal: Goal, user: User):
        self.db.execute(
            "insert into user_goal values (?, ?)",
            (user.id, goal.id)
        )

        result = self.db.execute(
            "select * from user_goal where user = ? and goal = ?",
            (user.id, goal.id)
        )

        return result

    def list(): ...


goal_repository = GoalRepository(db)
