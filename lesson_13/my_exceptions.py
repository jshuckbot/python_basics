class ValidateError(Exception):
    """Исключение валидации данных"""


class ValidateFullNameError(ValidateError):
    """Исключение валидации ФИО"""
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f'Введенное значение {self.value} не соответствует валидации!'
    

class ValidateEvaluationError(ValidateError):
    """Исключение валидации оценок по предмету"""
    def __init__(self, min_range, max_range, value):
        self.min_range = min_range
        self.max_range = max_range
        self.value = value

    def __str__(self):
        return f'Введенное значение {self.value} не лежит в диапазоне [{self.min_range}, {self.max_range}]'
    