from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Абстрактный класс для продуктов и наследников"""

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод вывода текста"""
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        """Абстрактный метод сложения"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Абстрактный метод добавления"""
        pass