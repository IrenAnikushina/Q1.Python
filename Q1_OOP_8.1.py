# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def transformation(cls):
        try:
            cls.day, cls.month, cls.year = map(int, obj_1.date.split('-'))
            Date.validation()
        except ValueError:
            print('Check your data! It must be digits in correct format!')

    @staticmethod
    def validation():
        print(f'Day: {obj_1.day}, month: {obj_1.month}, year: {obj_1.year}. Your date is correct')
        if obj_1.day > 31 or obj_1.month > 12:
            print('Date is incorrect')


user_date = input('Input date in format dd-mm-yyyy ')
obj_1 = Date(user_date)
obj_1.transformation()
