# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

lines = 0
words = 0
with open('text_1.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line != '\n':
            lines += 1
            words = words + len(line.split())

print(f'Количество строк - {lines}, количество слов - {words}')
