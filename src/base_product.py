from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для представления товаров"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class BaseEntity(ABC):
    """Абстрактный класс для общих свойств сущностей"""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        pass
