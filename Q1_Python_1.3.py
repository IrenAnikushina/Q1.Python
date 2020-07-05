# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = input('Please enter number greater than 0: ')

while n <= '0':
    print("I've asked for number greater than 0! Please try again!")
    n = input('Please enter number greater than 0: ')

print(f'The result of operation {n} + {n + n} + {n + n + n} will be {int(n) + int(n + n) + int(n + n + n)}')
