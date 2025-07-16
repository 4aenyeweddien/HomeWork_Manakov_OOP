from src.category import Category
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