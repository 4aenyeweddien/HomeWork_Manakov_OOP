from src.base_category_order import BaseCategoryOrder
from src.product import Product
from src.exceptions import ZeroQuantityProduct

class Order(BaseCategoryOrder):
    """Класс заказа одного товара"""

    def __init__(self, product: Product, quantity: int):
        """Инициализация класса заказа"""

        self.product = product
        try:
            if quantity == 0:
                raise ZeroQuantityProduct("Нельзя добавлять товар с нулевым количеством")
        except ZeroQuantityProduct as e:
            print(str(e))
        else:
            self.quantity = quantity
            print("Товар успешно добавлен в заказ")
        finally:
            print("Обработка добавления товара завершена")


    @property
    def total_price(self) -> float:
        """Возвращает стоимость заказа произведение стоимости и количества продуктов"""

        return self.product.price * self.quantity

    def __str__(self) -> str:
        """возвращает информацию о заказе"""

        return f"{self.product.name}, количество продуктов: {self.quantity}, общая стоимость: {self.total_price}"