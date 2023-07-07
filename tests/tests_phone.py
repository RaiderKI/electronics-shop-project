from src.phone import Phone
import pytest


@pytest.fixture
def fix_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(fix_phone):
    assert fix_phone.name == "iPhone 14"
    assert fix_phone.price == 120_000
    assert fix_phone.quantity == 5
    assert fix_phone.number_of_sim == 2


def test_phone_repr(fix_phone):
    assert repr(fix_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(fix_phone):
    assert fix_phone.number_of_sim == 2
