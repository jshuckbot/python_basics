from task_1 import is_prime
import unittest


class TestIsPrime(unittest.TestCase):
    def test_number_is_simple(self):
        self.assertEqual(is_prime(1), 'Не простое')
        
    def test_number_lt_zero(self):
        self.assertEqual(is_prime(-1), 'Число должно быть натуральным')
    
    def test_number_is_multiple(self):
        self.assertEqual(is_prime(100), 'Состовное')


if __name__ == '__main__':
    unittest.main()