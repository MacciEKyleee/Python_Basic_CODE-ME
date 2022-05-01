import unittest
from areas import rectangle, triangle, trapezoid

class AreasTestCase(unittest.TestCase):
   #pass
   def setUp(self):
       self.a = 4
       self.b = 6

   def test_rectangle_with_correct_values(self):
       result = rectangle(self.a,self.b)
       self.assertEqual(result,24)

   def test_rectangle_with_incorrect_values(self):
       #r = rectangle(self.a, 'Aaaa')
       #self.assertRaises(ValueError)
        #self.assertRaises(ValueError,rectangle(4,'***'))
        with self.assertRaises(ValueError):
            rectangle(4,'jakiś tekst')

   def test_triangle_with_correct_values(self):
       result = triangle(self.a,self.b)
       self.assertEqual(result,12)

   def test_triangle_with_incorrect_values(self):
       result = rectangle(self.a,self.b)
       self.assertEqual(result,24)

   # def test_dump(self):
   #     state = not is_account_active()
   #     self.assertFalse(state)


   def tearDown(self):
       del self.a
       del self.b

if __name__== '__main__':
    unittest.main()