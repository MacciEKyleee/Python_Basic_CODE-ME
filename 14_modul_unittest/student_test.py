import unittest

from student import Student

class StudentTestCase(unittest.TestCase): # To sprawia że klasa będzie klasą testującą)

    def setUp(self):
        self.stA = Student('Anna','Kowalska',4.6,None)

    # def test_student_email(self):
    #     st = Student('Anna','Kowalska',4.6,None)
    #     self.assertEqual(st.email,'anna.kowalska@university.com')
    #
    # def setUp(self):
    #     print('***** setUp ****\n')
    def test_student_email_created(self):
        self.assertEqual(self.stA.email,'anna.kowalska@university.com')

    def test_student_email_updated(self):
        # st = Student('Anna', 'Kowalska', 4.6, None)
        self.assertEqual(self.stA.email, 'anna.kowalska@university.com')

        self.stA.last = 'smith'
        self.assertEqual(self.stA.email,'anna.smith@university.com')

    def test_student_grant_schoolarship(self):
        stB = Student('Bartosz','Borowiak',3.6,None)

        self.stA.grant_scholarship()
        #self.assertEqual(self.stA.scholarship, True)
        self.assertTrue(self.stA.scholarship)


        stB.grant_scholarship()
        #self.assertEqual(stB.scholarship, True)
        self.assertFalse(stB.scholarship)


if __name__=='__main__': # to jest ważne, aby wyświetlało wynik testu
    unittest.main()