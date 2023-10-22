class InstantiateCSVError(Exception):
    """Класс для исключения при поврежденном файле"""

    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message
