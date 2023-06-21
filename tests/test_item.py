import pytest
from src.item import Item


def test_calculate_total_price():
    item = Item("мышка", 50, 5)
    assert item.calculate_total_price() == 250


def test_apply_discount():
    item = Item("Клавиатура", 75, 5)
    item.pay_rate = 1.6
    item.apply_discount()
    assert item.price == 120

