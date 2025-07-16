from abc import ABC, abstractmethod


class BaseCategoryOrder(ABC):
    """Абстрактный базовый класс для Category и Order"""

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод вывода текста"""
        pass