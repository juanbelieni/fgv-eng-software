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
        """
        Construtor da classe GoalRepository.

        Args:
            db (DB): Objeto de banco de dados.
        """
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
        """
        Cria uma nova meta (Goal) no banco de dados.

        Args:
            **attrs: Atributos da meta a ser criada.

        Returns:
            Optional[Goal]: Instância da meta criada.
        """
        id = str(uuid4())
        name = attrs.get("name")
        host = attrs.get("host")
        hidden = 0
        public = attrs.get("public")
        book = attrs.get("book")
        deadline = attrs.get("deadline")

        if name is None:
            name = "Meta de leitura para " + book

        result_goal = self.db.execute(
            "insert into goal values (?, ?, ?, ?, ?, ?, ?)",
            (id, name, host, public, hidden, book, deadline)
        )
        if result_goal is None:
            return None

        result_user_goal = self.db.execute(
            "insert into user_goal values (?, ?)",
            (host, id)
        )

        if result_user_goal is None:
            return None

        return self.read(id=id)

    def read(self, **attrs) -> Optional[Goal]:
        """
        Recupera uma meta do banco de dados com base nos atributos fornecidos.

        Args:
            **attrs: Atributos pelos quais a meta será buscada.

        Returns:
            Optional[Goal]: Instância da meta encontrada ou None se não encontrada.
        """
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

        return Goal(*result[0])

    def list(): pass

    def update(self, goal: Goal, **attrs) -> Optional[Goal]:
        """
        Atualiza os atributos de uma meta no banco de dados.

        Args:
            goal (Goal): Instância da meta a ser atualizada.
            **attrs: Atributos a serem atualizados.

        Returns:
            Optional[Goal]: Instância da meta atualizada.
        """
        updates = []
        params = tuple()

        if attrs.get("host") is not None or attrs.get("book") is not None:
            return None

        for key, value in attrs.items():
            updates.append(f"{key} = ?")
            params = (*params, value)

        params = (*params, goal.id)

        update = ", ".join(updates)

        result = self.db.execute(
            f"update goal set {update} where id = ?",
            params
        )

        if result is None:
            return None

        return self.read(id=id)

    def change_visibility(self, goal: Goal):
        """
        Altera a visibilidade de uma meta (oculta ou visível) no banco de dados.
        Uma meta oculta é uma meta excluída não-permanentemente.

        Args:
            goal (Goal): Instância da meta cuja visibilidade será alterada.
        """
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
        """
        Exclui uma meta no banco de dados.

        Args:
            goal (Goal): Instância da meta a ser excluída.
        """
        self.db.execute(
            "delete from goal where id = ?",
            (goal.id,)
        )

    def add_member(self, goal: Goal, user: User):
        """
        Adiciona um membro a uma meta no banco de dados.

        Args:
            goal (Goal): Instância da meta.
            user (User): Instância do usuário a ser adicionado à meta.

        Returns:
            Any: Resultado da operação (pode ser adaptado conforme necessário).
        """
        self.db.execute(
            "insert into user_goal values (?, ?)",
            (user.id, goal.id)
        )

        result = self.db.execute(
            "select * from user_goal where user = ? and goal = ?",
            (user.id, goal.id)
        )

        return result


goal_repository = GoalRepository(db)
