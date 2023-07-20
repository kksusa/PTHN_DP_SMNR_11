# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

import time


class MyString(str):
    """MyString class"""

    def __new__(cls, value, name):
        """Method of class creation with string name and date of creation attributes"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance

    def __str__(self):
        """Method of class creation with string name and date of creation attributes"""
        return f'Экземпляр класса MyString с именем "{self.name}" и временем создания "{self.time}"'

    def __repr__(self):
        return f'MyString({self.name}, {self.time})'


string_1 = MyString('new', 'string_2')
print(string_1)
print(repr(string_1))
print(string_1.upper())
print(string_1.title())
print(string_1.time)
print(string_1.name)
