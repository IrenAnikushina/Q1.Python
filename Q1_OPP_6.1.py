# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
from turtle import Turtle
import time

t = Turtle()


class TrafficLight:
    __color_ = {1: 'красный', 2: 'желтый', 3: 'зеленый'}

    # def __init__(self):
    #     print(TrafficLight.__color_)
    #     try:
    #         self.user_color = int(input('Какой сейчас горит свет (номер)? '))
    #         print(f'Сейчас горит {TrafficLight.__color_[self.user_color]} свет. Светофор заработал!')
    #     except:
    #         print('Нужно ввести цифру в соответствии со светом светофора')

    def running(self, r=45):
        print(f'Сфетофор работает вот так: ')
        y = r * 2
        try:
            while True:
                self.tl_color(y, r, 1)
                self.tl_color(y - y, r, 0)
                self.tl_color(y - y * 2, r, 0)
                time.sleep(7)
                self.tl_color(y, r, 0)
                self.tl_color(y - y, r, 2)
                self.tl_color(y - y * 2, r, 0)
                time.sleep(2)
                self.tl_color(y, r, 0)
                self.tl_color(y - y, r, 0)
                self.tl_color(y - y * 2, r, 3)
                time.sleep(7)
                self.tl_color(y, r, 0)
                self.tl_color(y - y, r, 2)
                self.tl_color(y - y * 2, r, 0)
                time.sleep(2)
        except:
            pass

    def tl_color(self, y, r, color, x=0):
        t.screen.setup(150, 350)
        t.screen.bgcolor('grey')
        t.hideturtle()
        t.speed(0)
        t.up()
        t.goto(x, y - r)
        t.down()
        t.fillcolor('black')
        if color == 1:
            t.fillcolor('red')
        elif color == 2:
            t.fillcolor('yellow')
        elif color == 3:
            t.fillcolor('green')
        t.begin_fill()
        t.circle(r)
        t.end_fill()


tl = TrafficLight()
tl.running()
