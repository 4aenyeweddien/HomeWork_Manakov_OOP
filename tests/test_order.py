from src.main import Order


def test_main_order(first_product):
    """Тестирование класса order"""
    order = Order(first_product, 3)
    assert order.product == first_product
    assert order.quantity == 3

    assert order.total_price == 540000
    # print(str(order))
    assert str(order) == "Samsung Galaxy S23 Ultra, количество продуктов: 3, общая стоимость: 540000.0"
