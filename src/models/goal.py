from dataclasses import dataclass
from src.utils.db import db, DB
from src.utils.repository import Repository
from typing import Optional
from uuid import uuid4
from hashlib import sha256

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
        hidden = attrs.get("hidden")
        public = attrs.get("public")
        book = attrs.get("book")

        print(name)
        if name == None:
            name = "Minha meta de leitura para " + book

        result = self.db.execute(
            "insert into goal values (?, ?, ?, ?, ?, ?)",
            (id, name, host, public, hidden, book)
        )

        self.db.execute(
            "insert into user_goal values (?, ?)",
            (host, id)
        )

        if result is None or len(result) == 0:
            return None

        return Goal(*result[0])

    def read(): ...

    def update(): ...

    def delete(): ...

    def add_people(): ...

goal_repository = GoalRepository(db)
