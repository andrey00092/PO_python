import doctest
from typing import Union


# TODO Написать 3 класса с документацией и аннотацией типов
class Mammal:
    """
    Создание и подготовка к работе объекта "Млекопитающее"

    :param weight: Вес млекопитающего (в кг)
    :param age: Возраст млекопитающего (полное число лет)
    :param meat_eater: Ест ли млекопитающее мясо

    Примеры:
    >>> dog = Mammal(20, 5, True)  # Инициализация экземпляра класса
    >>> elephant = Mammal(5000, 23, False)  # Инициализация экземпляра класса
    """

    def __init__(self, weight: Union[int, float], age: int, meat_eater: bool):

        if not isinstance(weight, (int, float)) or not isinstance(age, int) or not isinstance(meat_eater, bool):
            raise TypeError("Некорректный тип данных")
        if weight <= 0 or age <= 0:
            raise ValueError("Недопустимое значение")

        self.weight = weight
        self.age = age
        self.meat_eater = meat_eater

    def weight_changed(self, weight_change: Union[int, float], weight_gained: bool):
        """
        Метод увеличивает или уменьшает вес млекопитающего
        :param weight_change: На сколько изменился вес
        :param weight_gained: Вес увеличился или уменьшился

        :return: Вес млекопитающего

        Пример:
        >>> dog = Mammal(20, 5, True)
        >>> dog.weight_changed(2.5, False)
        """
        if not isinstance(weight_change, (int, float)) or not isinstance(weight_gained, bool):
            raise TypeError("Некорректный тип данных")
        if weight_change <= 0 or weight_change >= self.weight:
            raise ValueError("Недопустимое значение")

        if weight_gained is True:
            self.weight += weight_change
        else:
            self.weight -= weight_change

    def has_gotten_old(self, age_change: int):
        """
        Метод увеличивает возраст млекопитающего

        :param age_change: На сколько изменился возраст

        :return: Возраст млекопитающего

        Пример:
        >>> dog = Mammal(20, 5, True)
        >>> dog.has_gotten_old(3)
        """
        if not isinstance(age_change, int):
            raise TypeError("Некорректный тип данных")
        if age_change <= 0:
            raise ValueError("Недопустимое значение")

        self.age += age_change


class Table:
    """
    Создание и подготовка к работе объекта "Стол"

    :param material: Материал стола
    :param dimensions: Габариты стола
    :param assembled: Собран или разобран

    Пример:
    >>> table1 = Table("dark_wood", [300, 200, 100], True)  # Инициализация экземпляра класса
    """

    def __init__(self, material: str, dimensions: list, assembled: bool):
        self.material = material
        self.dimension = dimensions
        self.assembled = assembled

    def disassemble(self) -> bool:
        """
        Метод для разборки стола

        :return: Получилось ли разобрать стол
        """
        ...

    def assemble(self) -> bool:
        """
        Метод для сборки стола

        :return: Получилось ли собрать стол
        """
        ...


class Notebook:
    """
    Создание и подготовка к работе объекта "Тетрадь"

    :param pages: Количество страниц
    :param page_type: Тип страниц тетради

    Пример:
    >>> notebook1 = Notebook(24, "Клетка")  # Инициализация экземпляра класса
    """

    def __init__(self, pages: int, page_type: str):
        self.pages = pages
        self.page_theme = page_type
        self.crossed_pages = 0

    def tear_out_sheets(self, number_of_pages: int):
        """
        Метод уменьшает количество страниц в тетради

        :param number_of_pages: Количество вырываннных страниц

        :return: Оставшееся количество страниц в тетради
        """
        if not isinstance(number_of_pages, int):
            raise TypeError("Некорректный тип данных")
        if number_of_pages <= 0 or number_of_pages > self.pages:
            raise ValueError("Недопустимое значение")
        ...

    def cross_out(self, number_of_pages: int):
        """
        Метод увеличивает количество зачёркнутых страниц в тетради

        :param number_of_pages: Количество зачёркнутых страниц

        :return: Общее количество зачёркнутых страниц в тетради
        """
        if not isinstance(number_of_pages, int):
            raise TypeError("Некорректный тип данных")
        if number_of_pages <= 0 or number_of_pages > self.crossed_pages:
            raise ValueError("Недопустимое значение")
        ...


if __name__ == "__main__":

    # dog = Mammal(20, 5, True)
    #
    # print(dog.weight, dog.age, dog.meat_eater)
    #
    # dog.weight_changed(2.5, False)
    # dog.has_gotten_old(3)
    #
    # print(dog.weight, dog.age, dog.meat_eater)

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
