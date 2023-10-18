from src.item import Item


class MixinLang:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        if self.__language.upper() == 'EN':
            self.__language = 'RU'
            return self
        if self.__language.upper() == 'RU':
            self.__language = 'EN'
            return self


class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)
