from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        raise Exception("Método não implementado")

    @abstractmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        raise Exception("Método não implementado")
