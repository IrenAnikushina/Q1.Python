# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input('Please insert time (quantity of seconds) - '))

h = user_time // 3600
m = user_time % 3600 // 60
s = user_time % 60

print(f'Time was converted to the format hh:mm:ss -  {h:02}:{m:02}:{s:02}')
