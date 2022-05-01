"""
Zadanie 8
Napisz test dla właściwości fullname.
"""

import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_email(self):
        obj_anna = Student('ana', 'kowalska', 4.6, True)

        self.assertEqual(obj_anna.email, 'ana.kowalska@university.com')

        obj_anna.name = 'anna'
        self.assertEqual(obj_anna.email, 'anna.kowalska@university.com')

    def test_fullname(self):
        obj_anna = Student('anna', 'kowalska', 4.6, True)

        self.assertEqual(obj_anna.fullname, 'Anna Kowalska')

        obj_anna.last = 'Zamezna'
        self.assertEqual(obj_anna.fullname, 'Anna Zamezna')


if __name__ == '__main__':
    unittest.main()