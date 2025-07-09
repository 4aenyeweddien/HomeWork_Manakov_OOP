from abc import ABC, abstractmethod
from typing import Any
from src.base_product import BaseProduct
from src.base_category_order import BaseCategoryOrder


class PrintMixin:
    """Класс-миксин для печати в консоль информации"""

    def __init__(self):
        """инициализация миксина"""
        print(repr(self))

    def __repr__(self) -> str:
        """вывод сообщения об объекте"""
        return f"{self.__class__.__name__}({self.name},{self.description},{self.price},{self.quantity})"


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


class Category(BaseCategoryOrder):
    """Класс категории продуктов"""

    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        """Инициализация категории"""

        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """возвращает информацию о категории в строке"""

        quantity_of_products = 0
        for s in self.__products:
            quantity_of_products += s.quantity
        return f"{self.name}, количество продуктов: {quantity_of_products} шт."

    def add_product(self, product: Product) -> None:
        """добавляет продукт в категорию"""

        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list[str]:
        """Возвращает список продуктов в категории"""
        product_list = []
        for product in self.__products:
            product_list.append(f"{str(product)}")
        return product_list


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


class Smartphone(Product):
    """Класс категории смартфоны наследуемый от Product"""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Инициализация класса смартфонов наследник Product"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс категории газонная трава наследуемый от Product"""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Инициализация класса, наследник Product"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)