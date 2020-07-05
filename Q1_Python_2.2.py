# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


# user_list = []
#
# while True:
#     el = input('Please enter element or enter "--" to finish: ')
#     if el == '--':
#         break
#     else:
#         user_list.append(el)

user_list = (input('Please enter elements of list one by one using "_" as separator: ')).split("_")

print(f'This is your list - {user_list}')

new_list = user_list.copy()

for i in range(1, len(new_list), 2):
    new_list[i - 1], new_list[i] = new_list[i], new_list[i - 1]

print(f'And as result we get new list - {new_list}')
