"""
Zadanie 7
Wszystkie funkcje liczące pola powinny przyjmować tylko wartości liczbowe. Utwórz funkcję sprawdzającą czy wszystkie wartości boków są wartościami liczbowymi. Dodaj testy dla każdego z 3 wzorów na pola figur.

"""
import unittest
from fields import rectangle, triangle, trapezoid


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.h = 50

    def test_rectangle_with_correct_values(self):
        self.assertEqual(rectangle(self.a, self.h), 500)

    def test_rectangle_with_incorrect_value(self):
        with self.assertRaises(ValueError):
            rectangle(5, 'aaa')

    def test_triangle_with_correct_values(self):
        self.assertEqual(triangle(self.a, self.h), 250)

    def test_triangle_with_incorrect_value(self):
        with self.assertRaises(ValueError):
            triangle(5, 'aaa')

    def test_trapezoid_with_correct_values(self):
        self.assertEqual(trapezoid(self.a, 5, self.h), 375)

    def test_trapezoid_with_incorrect_value(self):
        with self.assertRaises(ValueError):
            trapezoid(5, 4, 'aaa')


    def tearDown(self):
        del self.a
        del self.h


if __name__ == '__main__':
    unittest.main()