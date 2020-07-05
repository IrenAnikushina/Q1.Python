# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

total = 0
persons = 0
duds = {}

with open('text_3.txt', 'r', encoding='utf-8') as salary:
    for line in salary:
        persons += 1
        pers = line.split()
        total = total + float(pers[1])
        if float(pers[1]) < 20000:
            duds[pers[0]] = float(pers[1])

print(f'Суммарный заработок составляет {total} у.е., средний заработок - {total / persons} у.е.\n'
      f'Сотрудники с ЗП менее 20000 у.е.: ')
for person, volume in duds.items():
    print(person, volume)
