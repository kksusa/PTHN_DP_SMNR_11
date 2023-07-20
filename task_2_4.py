# 📌 Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-
# архивов
# 📌 list-архивы также являются свойствами экземпляра
# 📌 Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    """Archive class"""

    my_list_number = []
    my_list_string = []

    # def __new__(cls, *args, **kwargs):
    # instance = super().__new__(cls, *args, **kwargs)

    def __init__(self, number, my_string):
        """Method of class initialization with any number, any string attributes and appending to list"""
        self.number = number
        self.my_string = my_string
        self.my_list_number.append(number)
        self.my_list_string.append(my_string)

    def __str__(self):
        return f'Экземпляр класса Archive с числом "{self.number}" и строкой "{self.my_string}"'

    def __repr__(self):
        return f'Archive({self.number}, {self.my_string})'


a = Archive(5, 'five')
print(f'{a.my_list_number = }, {a.my_list_string = }')
b = Archive(4, 'four')
print(f'{b.my_list_number = }, {b.my_list_string = }')
help(Archive)
print(a)
print(repr(b))
