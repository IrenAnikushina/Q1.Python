# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def amount(list):
    return sum(list) - min(list)


my_list = []
i = 1
while i < 4:
    try:
        my_list.append(int(input(f'Введите {i}-е число -  ')))
        i += 1
    except ValueError:
        print('Вы ввели не число')

print(f'Сумма наибольших двух чисел - {amount(my_list)}')
