# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

directory, surname, hours, rate, bonus = argv

print("Фамилия сотрудника: ", surname)
print("Выработка в часах: ", hours)
print("Ставка в час: ", rate)
print("Премия: ", bonus)
try:
    print("Заработная плата: ", int(hours) * int(rate) + int(bonus))
except ValueError:
    print('Для расчета заработной платы проверьте корректность параметров!')

"""
Open in Terminal

тест 1:
python Q1_Python_4.1.py Ivanov 150 2000 15000

результат:
Фамилия сотрудника:  Ivanov
Выработка в часах:  150
Ставка в час:  2000
Премия:  15000
Заработная плата:  315000

тест 2:
python Q1_Python_4.1.py Ivanov 150 2000 ааа

результат:
Фамилия сотрудника:  Ivanov
Выработка в часах:  150
Ставка в час:  2000
Премия:  ааа
Для расчета заработной платы проверьте корректность параметров!

"""
