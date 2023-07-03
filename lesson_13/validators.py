from my_exceptions import ValidateFullNameError, ValidateEvaluationError


class ValidatorFullName:
    """Валидатор ФИО"""
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value.istitle() and value.isalpha():
            setattr(instance, self.private_name, value)
        else:
            raise ValidateFullNameError(value)
        

class ValidatorEvaluation:
    """Валидатор оценок по предмету"""
    def __init__(self, min_range: int, max_range: int):
        self.min_range = min_range
        self.max_range = max_range

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value is not None and not self.min_range <= value <= self.max_range:
            raise ValidateEvaluationError(self.min_range, self.max_range, value)
        setattr(instance, self.private_name, value)
        