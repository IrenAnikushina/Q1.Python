# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def ttl_text(string):
    i = 0
    new_list = []
    for i in list(string):
        if ord(i) not in range(97, 123) and ord(i) != 32:
            print('Проверьте введненные символы')
            new_list.clear()
            break
        else:
            new_list.append(i)
    if len(new_list) > 0:
        print(''.join(new_list).title())


while True:
    my_string = input('Введите слово или несколько слов через пробел. Для выхода введите "-"\n'
                      'Используйте только латинские маленькие буквы!: ')
    if '-' in my_string:
        break
    else:
        ttl_text(my_string)
print('Вы захотели выйти из программы')
