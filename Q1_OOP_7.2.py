# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    def material_take_off(self):
        return round((float(my_coat.material_take_off) + float(my_suit.material_take_off)), 2)


class Coat(Clothes):

    @property
    def material_take_off(self):
        return round((self.size / 6.5 + 0.5), 2)


class Suit(Clothes):

    @property
    def grade(self):
        return self.size

    @grade.setter
    def grade(self, size):
        if self.size > 100:
            self.size = size / 100

    @property
    def material_take_off(self):
        return 2 * self.size + 0.3


my_coat = Coat(50)
my_suit = Suit(1.75)
print(f'Расход ткани на пальто на размер {my_coat.size} - {my_coat.material_take_off} метров')
print(f'Расход ткани на костюм на рост {my_suit.size} см - {my_suit.material_take_off} метров')
print(f'Общий расход ткани - {Clothes.material_take_off(0)} метров')
