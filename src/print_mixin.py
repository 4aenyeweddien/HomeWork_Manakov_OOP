


class PrintMixin:
    """Класс-миксин для печати в консоль информации"""

    def __init__(self):
        """инициализация миксина"""
        print(repr(self))

    def __repr__(self) -> str:
        """вывод сообщения об объекте"""
        return f"{self.__class__.__name__}({self.name},{self.description},{self.price},{self.quantity})"