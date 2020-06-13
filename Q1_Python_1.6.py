# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

print('Program of motivation in sport for beginners bid welcome you! Please answer few questions:')
a = int(input('How much kilometers is possible for you to run in 1st day (km)? '))
b = int(input("What is your target distance for running (km)? "))
i = 1
# print(f'Day {i}, plan - {a:.1f} kms')
while a < b:
    a = a * 1.1
    i += 1
    # print(f'Day {i}, plan - {a:.1f} kms')

print(f'In {i} days you will reach your target and run not less than {b} kilometers')