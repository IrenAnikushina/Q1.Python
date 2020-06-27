# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
"""
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

profits = {}
average_profit = {}
i = 0
average = 0
with open('text_7.txt', 'r', encoding='utf-8') as firms:
    for line in firms:
        firm_data = line.split()
        profit = int(firm_data[2]) - int(firm_data[3])
        if profit > 0:
            i += 1
            average = average + profit
        profits[firm_data[0]] = profit
        average_profit['average_profit'] = average / i
result = [profits, average_profit]
print(result)

with open("text_7.json", "w", encoding='utf-8') as task7:
    json.dump(result, task7, ensure_ascii=False)
