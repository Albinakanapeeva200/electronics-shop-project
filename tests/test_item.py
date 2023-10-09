from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    """Тест на общую стоимость конкретного товара в магазине"""
    item1 = Item("toy", 500.0, 3)
    assert item1.calculate_total_price() == 1500.0


def test_apply_discount():
    """Тест на установленную скидку для конкретного товара"""
    item1 = Item("toy", 500.0, 3)
    item1.pay_rate = 0.6
    item1.apply_discount()
    assert item1.price == 300


def test_name():
    item = Item('Смартфон', 10000, 5)
    assert item.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('4.0') == 4
    assert Item.string_to_number('4.4') == 4


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
