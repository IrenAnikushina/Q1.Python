# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = 'Порисуем!'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'ручка'

    def draw(self, color='синий'):
        print(f'{Stationery.title}\nВаш инструмент - {self.title}. Лучше возьмите {color} карандаш!')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self, color='красный'):
        print(f'{Stationery.title}\nВы выбрали {self.title}. Сейчас нам нужен {color} цвет!')


class Handle(Stationery):
    title = 'маркер'

    def draw(self, color='черный'):
        print(f'{Stationery.title}\nЭто {self.title}. Следы от маркера сложно удалить, а тем более, если он {color}!')


my_pen = Pen()
my_pen.draw()

my_pencil = Pencil()
my_pencil.draw()

my_handle = Handle()
my_handle.draw()
