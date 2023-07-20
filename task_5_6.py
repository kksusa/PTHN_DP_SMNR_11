# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения

class Rectangle:
    """Rectangle class"""

    def __init__(self, *args):
        """Method of class initialization with rectangle sides"""
        if len(args) == 1:
            self.length = args[0]
            self.width = self.length
        else:
            self.length, self.width = args

    def get_perimeter(self):
        """Method of rectangle perimeter calculation"""
        return self.length * 2 + self.width * 2

    def get_square(self):
        """Method of rectangle area calculation"""
        return self.length * self.width

    def __str__(self):
        return f'Экземпляр класса Rectangle с длинами сторон {self.length} и {self.width}'

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'

    def __add__(self, other):
        """Method of rectangles perimeters addition"""
        return self.get_perimeter() + other.get_perimeter()

    def __sub__(self, other):
        """Method of rectangles perimeters subtraction"""
        return abs(self.get_perimeter() - other.get_perimeter())

    def __eq__(self, other):
        """Method of rectangles areas equality comparison"""
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        """Method of rectangles areas gt comparison"""
        return self.get_square() > other.get_square()

    def __ge__(self, other):
        """Method of rectangles areas ge comparison"""
        return self.get_square() >= other.get_square()

    def __lt__(self, other):
        """Method of rectangles areas lt comparison"""
        return self.get_square() < other.get_square()

    def __le__(self, other):
        """Method of rectangles areas le comparison"""
        return self.get_square() <= other.get_square()


rec_1 = Rectangle(5)
rec_2 = Rectangle(7)
print(f'{rec_1.get_perimeter() = }\n{rec_2.get_perimeter() = }')
rec_3 = rec_1 + rec_2
rec_4 = rec_1 - rec_2
print(f'{rec_3 = }\n{rec_4 = }')
print(rec_1 == rec_2)
print(rec_3 >= rec_4)
print(repr(rec_1))
print(rec_2)
