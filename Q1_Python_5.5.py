# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

nums = [randint(1, 20) for i in range(10)]
print(nums)
result = 0

with open('text_5.txt', 'w', encoding='utf-8') as file:
    for num in nums:
        file.write(str(num) + ' ')
        result = result + num

print(f'Сумма чисел - {result}')
