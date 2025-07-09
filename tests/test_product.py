from unittest.mock import patch

import pytest

from src.main import Product

def test_product(first_product):
    """Тест инициализации первого продукта"""
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_main_second_product(second_product):
    """Тест инициализации второго продукта"""
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_main_getter_price(first_product):
    """Тест геттера возвращаюшего стоимость продукта"""
    assert first_product.price == 180000.0


def test_new_product_creation(new_product):
    """Тест создания нового продукта при отсутствии дубликатов"""
    product = Product.new_product(new_product)

    assert product.name == new_product["name"]
    assert product.price == new_product["price"]
    assert product.quantity == new_product["quantity"]


def test_new_product_update(new_product):
    """Тест обновления существующего продукта"""
    existing = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    updated = Product.new_product(new_product, [existing])

    assert updated.quantity == 10
    assert updated.price == 180000.0
    assert updated.description == "256GB, Серый цвет, 200MP камера"

def test_set_higher_price(first_product):
    """Цена должна обновиться без подтверждения, если новая цена выше"""
    first_product.price = 200000.0
    assert first_product.price == 200000.0


def test_set_zero_or_negative_price(first_product, capsys):
    """При нулевой/отрицательной цене должно выводиться предупреждение, а цена не меняться"""
    original_price = first_product.price

    first_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert first_product.price == original_price

    first_product.price = -1000
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert first_product.price == original_price


def test_lower_price_with_confirmation(first_product):
    """При понижении цены должно запрашиваться подтверждение (ввод 'y')"""
    with patch("builtins.input", return_value="y"):
        first_product.price = 150000.0
        assert first_product.price == 150000.0


def test_lower_price_with_rejection(first_product):
    """При отказе (ввод 'n') цена не должна измениться"""
    original_price = first_product.price
    with patch("builtins.input", return_value="n"):
        first_product.price = 150000.0
        assert first_product.price == original_price


def test_lower_price_with_invalid_input(first_product, capsys):
    """При некорректном вводе (не 'y'/'n') должно повторяться подтверждение"""
    with patch("builtins.input", side_effect=["invalid", "y"]):
        first_product.price = 150000.0
        captured = capsys.readouterr()
        assert "Ошибка ввода. Введите y/n" in captured.out
        assert first_product.price == 150000.0


def test_product_str(first_product):
    """Возврат строкового результата от метода str в продукте"""
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_product_add(first_product, second_product):
    """Проверка сложения двух продуктов"""
    assert first_product + second_product == 2580000.0