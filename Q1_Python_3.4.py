# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func1(x, y):
    print(f'Если возвести {x} в степень {y} получится {x ** y} (с помощью **)')


def my_func2(x, y, num=1):
    for i in range(0, abs(y)):
        num *= x
    print(f'Если возвести {x} в степень {y} получится {1 / num} (с помощью цикла)')


while True:
    try:
        x = int(input('Введите положительное число: '))
        y = int(input('Введите отрицательное число: '))
    except ValueError:
        print('Вы ввели не число! Еще одна попытка')
    else:
        if x <= 0 or y >= 0:
            print('Первое число положительное, в второе - отрицательное! Попробуйте еще раз!')
        else:
            my_func1(x, y)
            my_func2(x, y)
            break
