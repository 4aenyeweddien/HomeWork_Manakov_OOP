from src.category import Category
from src.main import Order


def test_main_order(first_product):
    """Тестирование класса order"""
    order = Order(first_product, 3)
    assert order.product == first_product
    assert order.quantity == 3

    assert order.total_price == 540000
    # print(str(order))
    assert str(order) == "Samsung Galaxy S23 Ultra, количество продуктов: 3, общая стоимость: 540000.0"


def test_custom_exception(capsys, first_product):
    """Тестирование вывода сообщений при обработке добавления товара в заказ с нулевым значением и больше нуля"""

    order = Order(first_product, 3)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Товар успешно добавлен в заказ"
    assert message.out.strip().split('\n')[-1] == "Обработка добавления товара завершена"

    order = Order(first_product, 0)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Нельзя добавлять товар с нулевым количеством"
    assert message.out.strip().split('\n')[-1] == "Обработка добавления товара завершена"
