# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def product(num, next_num):
    return num * next_num


print(reduce(product, [el for el in range(100, 1001) if el % 2 == 0]))

"""
Тест1:
произведение всех четных чисел от 1 до 10
print(reduce(product, [el for el in range(1, 11) if el % 2 == 0]))

Рез-т:
3840 (корректно)

Тест2:
произведение всех НЕчетных чисел от 1 до 10
print(reduce(product, [el for el in range(1, 11) if el % 2 != 0]))

Рез-т:
945 (корректно)

Значит, надеюсь, неимоверно огромное число, полученное в результате выполнения условий задачи, тоже корректное)))

"""
