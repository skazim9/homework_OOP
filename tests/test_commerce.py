import pytest
import unittest

from src.commerce import Product, Category


@pytest.fixture
def samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                    "удобства жизни",
                    1)


def test_product(samsung):  # тест на продукт
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5


def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                                    "функций для удобства жизни")
    assert category.products == 1


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Создание объекта Product перед каждым тестом"""
        self.product = Product(name="Samsung Galaxy",
                               description="Описание Samsung Galaxy",
                               price=89000.0,
                               quantity=5)

    def test_initialization(self):
        """Тестирование инициализации объекта Product"""
        self.assertEqual(self.product.name, "Samsung Galaxy")
        self.assertEqual(self.product.description, "Описание Samsung Galaxy")
        self.assertEqual(self.product.price, 89000.0)
        self.assertEqual(self.product.quantity, 5)

    def test_price_setter_valid(self):
        """Тестирование установки корректной цены"""
        self.product.price = 15000.0
        self.assertEqual(self.product.price, 15000.0)

    def test_new_product_creation(self):
        """Тестирование метода new_product"""
        new_product_data = {
            "name": "Iphone 15pro",
            "description": "Описание Iphone 15pro",
            "price": 120000.0,
            "quantity": 7
        }
        new_product = Product.new_product(new_product_data)
        self.assertEqual(new_product.name, "Iphone 15pro")
        self.assertEqual(new_product.description, "Описание Iphone 15pro")
        self.assertEqual(new_product.price, 120000.0)
        self.assertEqual(new_product.quantity, 7)


class Product_test:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product_test("Samsung Galaxy", 89000.0, 10)
        self.product2 = Product_test("Iphone 15pro", 120000.0, 5)
        self.category = Category("Категория Смартофны", "Описание категории Смартфоны", [self.product1, self.product2])

    def test_initialization(self):
        self.assertEqual(self.category.name, "Категория Смартофны")
        self.assertEqual(self.category.description, "Описание категории Смартфоны")
        self.assertEqual(len(self.category.products.splitlines()), 2)

    def test_add_product(self):
        new_product = Product_test("Товар 3", 200.0, 2)
        self.category.add_product(new_product)
        self.assertEqual(len(self.category.products.splitlines()), 3)
        self.assertIn("Товар 3", self.category.products)

    def test_product_count(self):
        self.assertEqual(Category.product_count, 7)