# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

from itertools import cycle, count, islice

"""В первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Выход по кол-ву объектов в итераторе islice без break"""
my_list = []
for i in islice(count(3, 1), 8):
    my_list.append(i)
print(my_list)

"""Во втором задании использовала резалт первой итерации, т.к. не придумала, как их еще объединить(("""

iter = cycle(my_list)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

"""А вот выход по счетчику, но без break)))"""

n = 1
for i in cycle(my_list):
    if n < 30:
        print(i, end=' ')
        n += 1
