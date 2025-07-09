from typing import Any

from src.category import Category


class CategoryIterator:
    """Итератор для перебора продуктов в категории"""

    def __init__(self, category_obj: Category):
        """Инициализация итератора"""

        self.category = category_obj
        self.index = 0
        self.products_list = category_obj._Category__products

    def __iter__(self) -> "CategoryIterator":
        """Возвращает итератор"""

        self.index = 0
        return self

    def __next__(self) -> Any:
        """Возвращает следующий продукт"""

        if self.index < len(self.products_list):
            product_obj = self.products_list[self.index]
            self.index += 1
            return product_obj
        else:
            raise StopIteration