# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

def checking(elements):
    for i in elements:
        try:
            i = int(i)
        except ValueError:
            pass
        else:
            global total
            total += i
    print(f'Общая сумма всех введенных чисел: {total}')


total = 0

while True:
    el = input('Please input number with space. Please enter "-" to break: ').split(' ')
    checking(el)
    if '-' in el:
        break

print('Это последнее вычисление, т.к. Вы захотели покинуть программу')