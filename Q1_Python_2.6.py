# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

print('Your catalogue is empty! Please insert needed data to check the analytics.')
catalogue = []  # list
analytics = {  # dict
    'name': list(),
    'price': list(),
    'q_ty': list(),
    'unit': list()
}
i = 1

while True:
    action = input('Enter command: "-" to cancel, "+" to add article, "?" to check the analytics: ')
    if action == '-':
        break
    elif action == '+':
        spec = {  # dict
            'name': input('Enter name: '),
            'price': int(input('Enter price: ')),
            'q_ty': int(input('Enter quantity: ')),
            'unit': input('Enter units: ')
        }
        new_article = (i, spec)  # tuple
        catalogue.append(new_article)  # list
        for key, val in spec.items():
            if val not in analytics[key]:
                analytics[key].append(val)
        i += 1
    elif action == '?':
        print('CATALOGUE:')
        for el in catalogue:
            print(el)
        print('ANALYTICS:')
        for key, val in analytics.items():
            print(f'{key}: {val}')
    else:
        print("WRONG! Enter correct command!")

print('Thank you for using our program! See you!')
