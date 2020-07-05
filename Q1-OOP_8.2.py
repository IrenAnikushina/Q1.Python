# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.


class ZeroErr(Exception):
    def __init__(self, text):
        self.text = text


user_data = input('Please input two numbers with " " ')

try:
    div_1, div_2 = map(int, user_data.split())
    if div_2 == 0:
        raise ZeroErr('Zero division error!')
except ValueError:
    print('Check your data!')
except ZeroErr as err:
    print(err)
else:
    print(f'The result of division is {div_1 / div_2}')
