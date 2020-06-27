# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from translate import Translator

with open('text_4.txt', 'r', encoding='utf-8') as en_num, open('text_4.2.0.txt', 'w', encoding='utf-8') as ru_num:
    for line in en_num:
        num = line.split()
        translator = Translator(to_lang="Russian")
        trans = translator.translate(num[0])
        print(trans, num[1], num[2], file=ru_num)
#       # print(trans, num[1], num[2])
