# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Please enter number greater than 0: '))

while number <= 0:
    print("I've asked for number greater than 0! Please try again!")
    number = int(input('Please enter number greater than 0: '))

max_n = 0

while (number % 10) > 0:
    n = number % 10
    if n > max_n:
        max_n = n
    number = number // 10

print(f'The biggest digit in your number is {max_n}')