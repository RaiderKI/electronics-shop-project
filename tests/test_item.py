import pytest
from src.item import Item

@pytest.fixture
def fix_item():
    return Item('Смартфон', 10000, 20)
def test_calculate_total_price():
    item = Item("мышка", 50, 5)
    assert item.calculate_total_price() == 250


def test_apply_discount():
    item = Item("Клавиатура", 75, 5)
    item.pay_rate = 1.6
    item.apply_discount()
    assert item.price == 120


def test_instantiate_from_csv(fix_item):
    assert len(Item.all) == 1


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(fix_item):
    assert repr(fix_item) == "Item('Смартфон', 10000, 20)"


def test_str(fix_item):
    assert str(fix_item) == 'Смартфон'
