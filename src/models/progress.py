from dataclasses import dataclass
from utils.db import db, DB
from utils.repository import Repository
from typing import Optional, Generator
from uuid import uuid4


@dataclass
class Progress:
    """Classe de dados para representar o progresso do usuário em um livro."""
    id: str
    user: str
    book: str
    percent: float


class ProgressRepository(Repository):
    """Repositório para interagir com os dados de progresso no banco de dados."""

    db: DB

    def __init__(self, db: DB):
        """
        Construtor do ProgressRepository.

        Parameters:
        - db (DB): Instância do banco de dados.
        """
        self.db = db

    def create(self, **attrs) -> Optional[Progress]:
        """
        Cria um novo registro de progresso no banco de dados.

        Parameters:
        - **attrs: Atributos necessários para criar o progresso.

        Returns:
        - Optional[Progress]: Instância do Progress criada.
        """
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
        """
        Recupera um registro de progresso do banco de dados com base no ID.

        Parameters:
        - id: ID do progresso a ser recuperado.

        Returns:
        - Optional[Progress]: Instância do Progress recuperada.
        """

        result = self.db.execute(
            "select id, user, book, percent from progress where id = ?",
            (id,)
        )

        if result is None or len(result) == 0:
            return None

        return Progress(*result[0])

    def list(self, user=None) -> Optional[list[Progress]]:
        """
        Lista todos os registros de progresso associados a um usuário.

        Parameters:
        - user: Usuário para o qual listar o progresso.

        Returns:
        - Optional[list[Progress]]: Lista de instâncias de Progress associadas ao usuário.
        """
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
        """
        Atualiza o percentual de progresso de um registro no banco de dados.

        Parameters:
        - id: ID do progresso a ser atualizado.
        - percent: Novo percentual de progresso.

        Returns:
        - Optional[Progress]: Instância do Progress atualizada.
        """

        result = self.db.execute(
            "update progress set percent = ? where id = ?",
            (percent, id)
        )

        if result is None:
            return None

        return self.read(id=id)

    def delete(self, id=None) -> Optional[Progress]:
        """
        Exclui um registro de progresso do banco de dados.

        Parameters:
        - id: ID do progresso a ser excluído.

        Returns:
        - Optional[Progress]: Instância do Progress excluída.
        """
        self.db.execute(
            "delete from progress where id = ?",
            (id,)
        )


progress_repository = ProgressRepository(db)
