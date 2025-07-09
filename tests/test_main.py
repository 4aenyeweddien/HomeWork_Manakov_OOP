from unittest.mock import patch

import pytest





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