# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating = [9, 9, 7, 5, 3, 3, 2, 1]
print(f'We have rating {rating}')
new_rating = rating.copy()

number = float(input('Please enter new number: '))

if number <= new_rating[-1]:
    new_rating.append(number)
else:
    for i in range(len(new_rating)):
        if number > new_rating[i]:
            new_rating.insert(i, number)
            break

print(f'Updated rating: {new_rating}')
