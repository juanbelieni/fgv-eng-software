from dataclasses import dataclass
from utils.db import db, DB
from utils.repository import Repository
from typing import Optional
from uuid import uuid4
from hashlib import sha256


@dataclass
class User:
    """
    User

    Represents a user with attributes id, name, email, and bio.

    Attributes:
    - id (str): The unique identifier for the user.
    - name (str): The name of the user.
    - email (str): The email address of the user.
    - bio (str): The user's biography.
    """
    id: str
    name: str
    email: str
    bio: str


class UserRepository(Repository):
    """
    User repository

    Handles user-related database operations such as creation, reading, updating and deletion.

    Attributes:
    - db (DB): The database instance for executing SQL queries.

    Methods:
    - create: Creates a new user in the database.
    - read: Reads a user from the database based on specified attributes.
    - update: Updates user attributes in the database.
    - delete: Deletes a user from the database.
    """

    db: DB

    def __init__(self, db: DB = db):
        """
        Initializes the UserRepository with a database instance.

        Parameters:
        - db (DB): The database instance for executing SQL queries.
        """

        self.db = db

    def __hash_password(self, password: str) -> str:
        return sha256(password.encode("utf-8")).hexdigest()

    def create(self, **attrs) -> Optional[User]:
        """
        Creates a new user in the database.

        Parameters:
        - **attrs: Keyword arguments containing user attributes.

        Returns:
        - Optional[User]: The created user if successful, else None.
        """

        id = str(uuid4())  # Unique identifier
        name = attrs.get("name")
        email = attrs.get("email")
        bio = attrs.get("bio") or ""
        password = self.__hash_password(attrs.get("password"))  # Password hash

        result = self.db.execute(
            "insert into user values (?,?,?,?,?)",
            (id, name, email, bio, password)
        )

        if result is None:
            return None

        return self.read(id=id)

    def read(self, **attrs) -> Optional[User]:
        """
        Reads a user from the database based on specified attributes.

        Parameters:
        - **attrs: Keyword arguments containing user attributes.

        Returns:
        - Optional[User]: The retrieved user if found, else None.
        """

        wheres = []
        params = tuple()

        for key, value in attrs.items():
            if key == "password":
                value = self.__hash_password(value)

            wheres.append(f"{key} = ?")
            params = (*params, value)

        where = " and ".join(wheres)

        result = self.db.execute(
            f"select id, name, email, bio from user where {where}",
            params
        )

        if result is None or len(result) == 0:
            return None

        return User(*result[0])

    def list(self):
        """
        Lists all users in the database.

        Not implemented.
        """
        pass

    def update(self, user: User, **attrs) -> Optional[User]:
        """
        Updates user attributes in the database.

        Parameters:
        - user (User): The user to be updated.
        - **attrs: Keyword arguments containing updated user attributes.

        Returns:
        - Optional[User]: The updated user if successful, else None.
        """

        name = attrs.get("name") or user.name
        bio = attrs.get("bio") or user.bio

        result = self.db.execute(
            "update user set name = ?, bio = ? where id = ?",
            (name, bio, user.id)
        )

        if result is None:
            return None

        return self.read(id=user.id)

    def delete(self, user: User):
        """
        Deletes a user from the database.

        Parameters:
        - user (User): The user to be deleted.
        """

        self.db.execute(
            "delete user where id = ?",
            (user.id,)
        )


user_repository = UserRepository()
