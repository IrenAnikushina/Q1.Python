# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


month = None

while month not in range(1, 13):
    month = int(input('Please enter the number of the month: '))

# dict
year_dict = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}
for key, val in year_dict.items():
    if month in val:
        print(f'This month belongs to {key}!')

# list (I'm not sure)
year = ['winter', 'spring', 'summer', 'autumn']

if 3 <= month <= 5:
    print(f'It is {year[1]}!')
elif 6 <= month <= 8:
    print(f'It is {year[2]}!')
elif 9 <= month <= 11:
    print(f'It is {year[3]}!')
else:
    print(f'It is {year[0]}!')
