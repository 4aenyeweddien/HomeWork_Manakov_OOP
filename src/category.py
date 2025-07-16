from src.base_category_order import BaseCategoryOrder
from src.product import Product

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

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
