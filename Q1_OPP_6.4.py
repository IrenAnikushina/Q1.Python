# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

import random


class Car:
    speed = -1
    color = None
    name = None
    is_police = None

    def __init__(self):
        try:
            self.name, self.color = map(str, input('Enter name and color of the car with "//": ').split("//"))
            self.speed = int(input('Enter current speed of the car: '))
            self.is_police = input('Is it police car "+" or "-"? ')
            if self.is_police == "+":
                self.is_police = True
        except ValueError:
            print('Check your data!')

    def car_go(self):
        print(f'Hey, {self.color} {self.name} hurry up vroom-vroom!')

    def car_stop(self):
        print(f'Finally {self.color} {self.name} stopped')

    def turn(self):
        self.derection = random.choice(['lefts', 'rights', 'reverse'])
        print(f'Your {self.color} {self.name} turns {self.derection}')

    def show_speed(self):
        if self.speed >= 0:
            print(f'Your {self.color} {self.name} goes with current speed {self.speed} km/hour')

    def get_info(self):
        if self.speed >= 0:
            print(f'Your car is {self.color} {self.name}, which is moving {self.speed} km/hour')


class TownCar(Car):
    def police(self):
        if self.is_police:
            print('You selected wrong class! This is TownCar but not PoliceCar class.')

    def show_speed(self):
        if 0 <= self.speed > 60:
            print('Speed limit is exceeded! Police ordered you to stop!')
            self.car_stop()


class SportCar(Car):
    def police(self):
        if self.is_police:
            print('You selected wrong class! This is TownCar but not PoliceCar class.')

    def show_speed(self):
        if 0 <= self.speed < 90:
            print('You can move faster! But you have to turn because of police!')
            self.turn()
            self.speed += 30
            print(f'Your speed increased to {self.speed}!')


class WorkCar(Car):
    def police(self):
        if self.is_police:
            print('You selected wrong class! This is WorkCar but not PoliceCar class.')

    def show_speed(self):
        if 0 <= self.speed > 40:
            print('Speed limit is exceeded! Please slow down!')
            self.car_stop()


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            print('Bip-bip sirens wailing!!!')
        else:
            print('You selected wrong class! ')


print('Filling class TownCar')
town = TownCar()
town.police()
town.get_info()
town.show_speed()

"""
Filling class TownCar
Enter name and color of the car with "//": VW Polo//white
Enter current speed of the car: 90
Is it police car "+" or "-"? +
You selected wrong class! This is TownCar but not PoliceCar class.
Your car is white VW Polo, which is moving 90 km/hour
Speed limit is exceeded! Police ordered you to stop!
white VW Polo stopped
"""

print('\nFilling class SportCar')
sport = SportCar()
sport.get_info()
sport.show_speed()

"""
Filling class SportCar
Enter name and color of the car with "//": Ferrari//red
Enter current speed of the car: 80
Is it police car "+" or "-"? -
Your car is red Ferrari moving 80 km/hour
You can move faster! But you have to turn because of police!
red Ferrari turns lefts
Your speed increased to 110!
"""

print('\nFilling class WorkCar')
work = WorkCar()
work.get_info()
work.police()
work.show_speed()

"""
Filling class WorkCar
Enter name and color of the car with "//": MAN//grey
Enter current speed of the car: 60
Is it police car "+" or "-"? +
Your car is grey MAN, which is moving 60 km/hour
You selected wrong class! This is WorkCar but not PoliceCar class.
Speed limit is exceeded! Please slow down!
grey MAN stopped
"""

print('\nFilling class PoliceCar')
police = PoliceCar()
police.get_info()
police.police()
police.car_go()

"""
Filling class PoliceCar
Enter name and color of the car with "//": Infinity//black
Enter current speed of the car: 90
Is it police car "+" or "-"? +
Your car is black Infinity, which is moving 90 km/hour
Bip-bip sirens wailing!!!
Hey, black Infinity hurry up vroom-vroom!
"""
