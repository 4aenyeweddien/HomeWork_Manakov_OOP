from src.main import Category, Product

def test_main_product(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_main_second_product(second_product):
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_main_first_category(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert len(first_category.products) == 3

    assert first_category.category_count == 2

    assert second_category.category_count == 2

    assert first_category.product_count == 4

    assert second_category.product_count == 4

# def test_main_new_product(new_product, first_product):
#     """Тест создания нового продукта"""
#     new_product = first_product.new_product(new_product)
#
#     assert new_product.name == new_product["name"]
#     assert new_product.description == new_product["description"]
#     assert new_product.price == new_product["price"]
#     assert new_product.quantity == new_product["quantity"]

def test_main_getter_price(first_product):
    assert first_product.price == 180000.0

# def test_main_setter_price(first_product, new_product):
#     assert first_product

def test_main_add_product(first_category, first_product):
    length_of_categories = len(first_category.products)
    counter = Category.product_count

    first_category.add_product(first_product)

    assert len(first_category.products) == length_of_categories + 1
    assert Category.product_count == counter + 1


