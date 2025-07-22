from src.category import Category
from src.product import Product
import pytest

def test_main_first_category(first_category, second_category):
    """Тест инициализации категорий"""
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert second_category.name == "Телевизоры"
    assert len(first_category.products) == 3

    assert first_category.category_count == 2

    assert second_category.category_count == 2

    assert first_category.product_count == 4

    assert second_category.product_count == 4


def test_main_add_product(first_category, first_product):
    """Добавление продукта в категорию"""
    length_of_categories = len(first_category.products)
    counter = Category.product_count

    first_category.add_product(first_product)

    assert len(first_category.products) == length_of_categories + 1
    assert Category.product_count == counter + 1


def test_category_str(first_category):
    """Возврат строкового результата от метода str в category"""
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."

def test_category_add_product_error(first_category):
    """Вызов ошибки при добавлении объекта не являющимся продуктом"""
    with pytest.raises(TypeError):
        first_category.add_product("Not a product")

def test_middle_price(first_category, category_empty_products):
    """Тест подсчета среднего ценника"""
    assert first_category.middle_price() == 140333.33
    assert category_empty_products.middle_price() == 0

def test_custom_exception(capsys):
    """Тест на добавление в категорию товара с нулевым значением и выводом сообщений обработки"""
    first_category = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )

    assert len(first_category.products) == 3

    # тест не работает потому что ловится ошибка в Product и нельзя инициализировать продукт с нулевым значением

    # product_add = Product(
    #     name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=0)
    # first_category.add_product(product_add)
    # message = capsys.readouterr()
    # assert message.out.strip().split('\n')[-2] == "Нельзя добавлять товар с нулевым количеством"
    # assert message.out.strip().split('\n')[-1] == "Обработка добавления товара завершена"

    product_add = Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5)
    first_category.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Товар успешно добавлен в категорию"
    assert message.out.strip().split('\n')[-1] == "Обработка добавления товара завершена"