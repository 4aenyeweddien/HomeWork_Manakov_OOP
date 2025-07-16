from src.base_category_order import BaseCategoryOrder
from src.product import Product

class Order(BaseCategoryOrder):
    """Класс заказа одного товара"""

    def __init__(self, product: Product, quantity: int):
        """Инициализация класса заказа"""

        self.product = product
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        """Возвращает стоимость заказа произведение стоимости и количества продуктов"""

        return self.product.price * self.quantity

    def __str__(self) -> str:
        """возвращает информацию о заказе"""

        return f"{self.product.name}, количество продуктов: {self.quantity}, общая стоимость: {self.total_price}"