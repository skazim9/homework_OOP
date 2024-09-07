import pytest

from src.commerce import Product, Category
from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


@pytest.fixture
def samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture
def category_p():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

def test_product(samsung):  # тест на продукт
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5


def test_product_creation():
    # Фикстура для теста
    product_data = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 20
    }

    product = Product.new_product(product_data)

    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100.0
    assert product.quantity == 20


def test_product_str_method():
    product = Product("Товар 2", "Описание товара 2", 150.0, 5)
    assert str(product) == "Товар 2, 150.0 руб. Остаток: 5 шт."


def test_price_setter():
    product = Product("Товар 3", "Описание товара 3", 200.0, 10)
    product.price = 250.0
    assert product.price == 250.0

    product.price = -50.0  # Попробуем установить отрицательную цену
    assert product.price != -50.0  # Цена не должна измениться


def test_category_creation():
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание товара 2", 150.0, 10)
    category = Category("Категория 1", "Описание категории 1", [product1, product2])

    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert len(category.products.split('\n')) - 1 == 2  # количество продуктов


def test_category_add_product():
    product = Product("Товар 3", "Описание товара 3", 200.0, 2)
    category = Category("Категория 2", "Описание категории 2", [])

    category.add_product(product)

    assert len(category.products.split('\n')) - 1 == 1


def test_category_all_products_count():
    product1 = Product("Iphone 15Pro", "Apple", 120000.0, 7)
    product2 = Product("Galaxy S21", "Samsung", 150000.0, 8)
    category = Category("Смартфоны", "телефоны для свзяи", [product1, product2])

    assert str(category) == "Смартфоны, количество продуктов: 15 шт."


def test_print_mixin_product(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_print_mixin_smartphone(capsys):
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"


def test_print_mixin_lawn_grass(capsys):
    LawnGrass("Газон для лужайки", "Зеленый газон, незамрезающий", 4500.0, 140, "Россия", "7 дней", "Зеленый")

    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газон для лужайки, Зеленый газон, незамрезающий, 4500.0, 140)"


def test_product_zero_quantity():
    """Проверяет вызов исключения ValueError при нулевом или отрицательном количестве товара"""
    with pytest.raises(ValueError):
        Product("Nokia", "A52", 12000.0, 0)
        Product("Samsung", "Galaxy S9", 40000.0, -10)

def test_category_middle_price(category_p):
    """Проверяет правильность подсчета средней цены в категории"""
    assert category_p.middle_price() == 140333.33


def test_category_middle_price_empty():
    """Проверяет вывод нулевого значения средней цены, при отсутствии списка товаров в категории"""
    cat = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником",
        [],
    )
    assert cat.middle_price() == 0