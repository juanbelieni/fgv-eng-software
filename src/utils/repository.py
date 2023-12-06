from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def create(): ...

    @abstractmethod
    def read(): ...

    @abstractmethod
    def update(): ...

    @abstractmethod
    def delete(): ...
