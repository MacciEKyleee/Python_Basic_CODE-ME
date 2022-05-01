import unittest
from fields import rectangle


class FieldsTestCase(unittest.TestCase):
    def test_rectangle_with_correct_values(self):
        self.assertEqual(rectangle(5, 5), 25)


if __name__ == '__main__':
    unittest.main()