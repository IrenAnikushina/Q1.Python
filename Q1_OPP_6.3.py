# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name = None
    surname = None
    position = None
    _income_ = {'wage': None, 'bonus': None}

    def __init__(self):
        try:
            self.name, self.surname, self.position = map(str,
                                                         input('Введите имя, фимилию, должность через пробел ').split())
            Worker._income_['wage'], Worker._income_['bonus'] = map(int, input(
                'Введите оклад и бонус через пробел ').split())
        except ValueError:
            pass


class Position(Worker):

    def get_full_name(self):
        if self.name and self.surname and self.position is not None:
            print(f'Итак, наш работник - {self.name} {self.surname}, занимает должность {self.position}')
        else:
            print('Не удалось получить персональные данные')

    def get_total_income(self):
        try:
            print(f"Ежемесячный доход с учетом премии - {Worker._income_['wage'] + Worker._income_['bonus']}")
        except TypeError:
            print('Не хватает данных для подсчета дохода')


unit = Position()
unit.get_full_name()
unit.get_total_income()
