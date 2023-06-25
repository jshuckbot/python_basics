import time


class MyString(str):
    """Моя строка"""
    def __new__(cls, value: str, name: str):
        """Расширяет метод параметрами value, name"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        
        return instance


class Arhive:
    """Архив"""
    numbers = []
    values = []
    
    def __new__(cls, number: int, value: str):
        """Расширяет метод параметрами number, value"""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        
        return instance
    
    def __init__(self, number: int, value: str):
        """Инициализирует экземпляр"""
        self.number = number
        self.value = value
    
    def __repr__(self):
        """Представление для разработчика"""
        return f'Arhive({self.number}, {self.value})'


class Rectangle:
    """Прямоугольник"""
    def __init__(self, a: int, b: int = None):
        """Инициализирует объект прямоугольника"""
        self.a = a
        self.b = a if b is None else b
        
    def perimeter(self):
        """Расчитывает периметр"""
        return 2 * (self.a + self.b)
    
    def area(self):
        """Расчитывает площадь"""
        return self.a * self.b
    
    def __add__(self, other):
        """Сложение периметров"""
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)
    
    def __sub__(self, other):
        """Вычитание периметров"""
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min((self.a, self.b, other.a, other.b)) 
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)
        