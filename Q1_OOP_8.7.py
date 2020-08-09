# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __getitem__(self):
        if self.b > 0:
            return f'Комплексное число: {self.a}+{self.b}i'
        else:
            return f'Комплексное число: {self.a}{self.b}i'

    def __add__(self, other):
        if (self.b + other.b) > 0:
            return f'Сумма: {self.a + other.a}+{self.b + other.b}i'
        else:
            return f'Сумма: {self.a + other.a}{self.b + other.b}i'

    def __mul__(self, other):
        if (self.a * other.b + other.a * self.b) > 0:
            return f'Произведение: {self.a * other.a - self.b * other.b}+{self.a * other.b + other.a * self.b}i'
        else:
            return f'Произведение: {self.a * other.a - self.b * other.b}{self.a * other.b + other.a * self.b}i'


z_1 = ComplexNum(3, 4)
z_2 = ComplexNum(7, -6)

print(z_1.__getitem__())
print(z_2.__getitem__())
print(z_1 + z_2)
print(z_1 * z_2)
