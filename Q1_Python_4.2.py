# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randint

test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [test_list[i] for i in range(1, len(test_list), ++1) if test_list[i] > test_list[i - 1]]
print(f'Было {test_list}\nСтало {new_list}')

test_list2 = [randint(-500, 500) for el in range(0, 10)]
new_list2 = [test_list2[i] for i in range(1, len(test_list2), ++1) if test_list2[i] > test_list2[i - 1]]
print(f'Было {test_list2}\nСтало {new_list2}')
