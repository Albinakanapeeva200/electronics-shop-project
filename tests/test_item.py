"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


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
