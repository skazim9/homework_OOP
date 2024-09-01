import pytest

from src.lawngrass import LawnGrass

@pytest.fixture
def lawnGrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawnGrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

def test_lawn_grass(lawnGrass1, lawnGrass2):

    assert lawnGrass1.name == "Газонная трава"
    assert lawnGrass1.description == "Элитная трава для газона"
    assert lawnGrass1.price == 500.0
    assert lawnGrass1.quantity == 20
    assert lawnGrass1.country == "Россия"
    assert lawnGrass1.germination_period == "7 дней"
    assert lawnGrass1.color == "Зеленый"

    assert lawnGrass2.name == "Газонная трава 2"
    assert lawnGrass2.description == "Выносливая трава"
    assert lawnGrass2.price == 450.0
    assert lawnGrass2.quantity == 15
    assert lawnGrass2.country == "США"
    assert lawnGrass2.germination_period == "5 дней"
    assert lawnGrass2.color == "Темно-зеленый"


def test_add_lawn_grass(lawnGrass1, lawnGrass2):

    assert lawnGrass1 + lawnGrass2 == '16750.0 руб.'


def test_add_lawn_grass_error(lawnGrass1):

    with pytest.raises(TypeError):
        lawnGrass1 + 1