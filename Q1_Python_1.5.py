# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). # Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

earn = float(input('Please input the earnings of your Company (USD): '))
charge = float(input('Please input the charges of your Company (USD): '))

profit = earn - charge

if profit > 0:
    stuff = int(input("Please input your stuff number: "))
    margin = profit / earn
    pers_margin = profit / stuff
    print(f'Congratulations!\nThe profit of company amounts {profit:.2f} USD\n'
          f'The profit margin amounts {margin:.2f}\nMargin per person amounts {pers_margin:.2f} USD')
elif profit == 0:
    print(f'Not bad you have to work better to get profit!')
else:
    print(f'Unfortunately your company incur losses and negative profit amounts {profit:.2f}')
