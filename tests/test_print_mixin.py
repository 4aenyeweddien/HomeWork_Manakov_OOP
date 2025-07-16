from src.main import LawnGrass, Product, Smartphone


def test_print_mixin_product(capsys):
    """Тест миксина, который выводит информацию об объекте Product"""
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra,256GB, Серый цвет, 200MP камера,180000.0,5)"


def test_print_mixin_smartphone(capsys):
    """Тест миксина, который выводит информацию об объекте Smartphone"""

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra,256GB, Серый цвет, 200MP камера,180000.0,5)"


def test_print_mixin_lawngrass(capsys):
    """Тест миксина, который выводит информацию об объекте Lawngrass"""

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава,Элитная трава для газона,500.0,20)"
