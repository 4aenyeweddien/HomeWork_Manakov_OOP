from unittest.mock import patch

import pytest

from src.main import Category, Product


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





def test_category_iterator(category_iterator):
    """тест итератор по категории"""
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(category_iterator).name == "Iphone 15"
    assert next(category_iterator).name == "Xiaomi Redmi Note 11"
    with pytest.raises(StopIteration):
        next(category_iterator)


def test_smartphone_init(smartphone1):
    """Инициализация класса наследника смартфоны"""
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_lawngrass_init(lawngrass1):
    """Инициализация класса наследника газонная трава"""
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"


def test_category_add_product_error(first_category):
    """Вызов ошибки при добавлении объекта не являющимся продуктом"""
    with pytest.raises(TypeError):
        first_category.add_product("Not a product")


def test_product_add_error(smartphone1, lawngrass1):
    """Вызов ошибки при сложении продуктов из разных классов"""
    with pytest.raises(TypeError):
        result = smartphone1 + lawngrass1


def test_product_add2(smartphone1, smartphone2, lawngrass1, lawngrass2):
    """Проверка сложения двух продуктов"""
    assert smartphone1 + smartphone2 == 2580000.0
    assert lawngrass1 + lawngrass2 == 16750.0
