from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        raise Exception("Método não implementado")

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        raise Exception("Método não implementado")
