import unittest
from Student import Student


class TestKillMutants(unittest.TestCase):

    def setUp(self):
        self.student = Student("John Doe", "johndoe@gmail.com", 21)
        self.student.grade[2] = {}
        self.student.grade[2]["math"] = 75

    def test_kill_mutant46(self):
        student = Student("Jane Doe", "janedoe@yahoo.com", 0)
        self.assertEqual(student.name, "Jane Doe")
        self.assertEqual(student.email, "janedoe@yahoo.com")
        self.assertEqual(student.age, 0)

    def test_kill_mutant50(self):
        self.student.insert_grade(100, "math", 1, False)
        self.assertEqual(self.student.grade[1]["math"], 100)
        self.student.insert_grade(0, "math", 1, True)
        self.assertEqual(self.student.grade[1]["math"], 0)

    def test_kill_mutant53(self):
        self.student.insert_grade(75, "chemistry", 2, False)
        self.assertEqual(self.student.grade[2]["chemistry"], 75)
        with self.assertRaisesRegex(ValueError,
                                    "^Invalid semester! Semester cannot be negative or null and cannot exceed 2$"):
            self.student.insert_grade(70, "chemistry", 0, False)

    def test_kill_mutant74(self):
        student = Student("Jane Doe", "janedoe@yahoo.com", 15)
        self.assertEqual(student.get_platform_username(), student.email)
        student = Student("Jane Doe", "janedoe@gmail.com", 17)
        self.assertEqual(student.get_platform_username(), student.email)

    # mutants 80, 97 and 99 cannot be killed (in that case "<=" gives the same outcome as "=" )


if __name__ == '__main__':
    unittest.main()
