from src.base_product import BaseProduct
from src.print_mixin import PrintMixin

class Product(BaseProduct, PrintMixin):
    """Класс продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует продукт"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """возвращает строковое представление продукта на складе"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """складывает продукты по стоимости с учетом количества"""
        if isinstance(other, self.__class__):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list["Product"] = None) -> "Product":
        """Метод добавляющий новый продукт или обновляющий уже существующий"""
        if existing_products:
            for existing_product in existing_products:
                if product_data["name"] == existing_product.name:
                    existing_product.quantity += product_data["quantity"]
                    existing_product.price = max(existing_product.price, product_data["price"])
                    return existing_product
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price) -> None:
        """установка новой цены с проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            print("Вы уверены в понижении цены товара? Введите - y / n")
            while True:
                user_input = input().lower()
                if user_input == "y":
                    self.__price = new_price
                    break
                elif user_input == "n":
                    break
                else:
                    print("Ошибка ввода. Введите y/n")
        else:
            self.__price = new_price