# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

ave = "Welcome, my friend! Let's buddy up!"
bye = '\nIt was pleasant to meet you but I still have 5 tasks to do. See you later!'
name = 'Irina'
age = 33

print(ave)

user_name = input("\nWhat's your name? ")
print(f'Pleasant to meet you, {user_name}! And my name is {name}.')
user_age = int(input('\nAnd how old are you? '))
print(f'So your age is {user_age}, dear {user_name}! BTW the difference between us is {abs(user_age - age)} years.')
main_question = input('\nDo like Python? (Y/N) ')

if main_question == 'Y' or 'y':
    print("Wonderful! I like it too! That's why I'm here:)")
else:
    print("I don't believe you! It seems you still like it!")

print(bye)