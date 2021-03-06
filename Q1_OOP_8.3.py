# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя “stop” команду. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.


class IsDigitCheckList(Exception):

    def __init__(self, txt):
        self.txt = txt


final_list = []

while True:
    el = input('Please input number with space. Please enter "-" to break: ')
    try:
        if el.isdigit() is False:
            if el == '-':
                break
            else:
                raise IsDigitCheckList('Please enter numbers only!')
        else:
            el = int(el)
    except IsDigitCheckList as err:
        print(err)
    else:
        final_list.append(el)

print(f'You decided to escape the program. Your list: {final_list}')
