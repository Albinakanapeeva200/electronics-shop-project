import csv
from src.exeption_error import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        """Складывает экземпляры класса Phone и Item (сложение по количеству товара в магазине)"""
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """приватность атрибута name"""
        return self.__name

    @name.setter
    def name(self, name):
        """проверяет, что длина наименования товара не больше 10 симвовов"""
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, filename):
        """инициализирует экземпляры класса Item данными из файла src/items.csv"""
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                items = []
                for i in reader:
                    name = str(i['name'])
                    price = float(i['price'])
                    quantity = int(i['quantity'])
                    item = cls(name, price, quantity)
                    items.append(item)
                cls.all = items
        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл {filename}")
        except InstantiateCSVError:
            raise InstantiateCSVError(f"Файл {filename} поврежден")

    @staticmethod
    def string_to_number(str_number):
        """возвращающает число из числа-строки"""
        number = str_number.split('.')
        return int(number[0])
