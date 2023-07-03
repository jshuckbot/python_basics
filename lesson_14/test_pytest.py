from task_1 import is_prime
import pytest


def test_number_is_simple():
    assert is_prime(1) == 'Не простое'


def test_number_lt_zero():
    assert is_prime(-1) == 'Число должно быть натуральным'
    

def test_number_is_multiple():
    assert is_prime(100) == 'Состовное'


if __name__ == '__main__':
    pytest.main(['-v'])
    