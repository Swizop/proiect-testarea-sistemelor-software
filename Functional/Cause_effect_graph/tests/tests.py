import unittest
from Student import Student


class TestCauseEffectGraphMethod1(unittest.TestCase):

    # Initializing a mock student before each test case
    # This function is called before each test
    def setUp(self):
        self.student = Student("John Doe", "johndoe@gmail.com", 21)
        self.student.grade[2] = {}
        self.student.grade[2]["math"] = 75

    # test numbers correspond with row highlighted in red in Excel document
    def test1_case1(self):
        with self.assertRaisesRegex(ValueError, r"^Invalid grade! Grade cannot be negative and cannot exceed 100.$"):
            self.student.insert_grade(-3, "math", 1, False)

    def test2_case1(self):
        with self.assertRaisesRegex(ValueError,
                                    "^Invalid semester! Semester cannot be negative and cannot exceed 2$"):
            self.student.insert_grade(50, "math", 3, False)

    def test3_case1(self):
        with self.assertRaisesRegex(ValueError,
                                    "^Invalid subject! Subject cannot be empty.$"):
            self.student.insert_grade(30, "", 1, False)

    def test4_case1(self):
        self.student.insert_grade(60, "math", 1, False)
        self.assertEqual(self.student.grade[1]["math"], 60)

    def test4_case2(self):
        self.student.insert_grade(0, "math", 1, False)
        self.assertEqual(self.student.grade[1]["math"], 0)

    def test5_case1(self):
        self.student.insert_grade(73, "english", 1, True)
        self.assertEqual(self.student.grade[1]["english"], 73)

    def test6_case1(self):
        self.assertEqual(self.student.grade[2]["math"], 75)
        self.student.insert_grade(80, "math", 2, True)
        self.assertEqual(self.student.grade[2]["math"], 80)

    def test8_case1(self):
        with self.assertRaisesRegex(AttributeError,
                                    "^Grade for semester: '2' and subject 'math' already exists.$"):
            self.student.insert_grade(70, "math", 2, False)


class TestCauseEffectGraphMethod2(unittest.TestCase):

    # Initializing a mock student before each test case
    # This function is called before each test
    def setUp(self):
        self.student = Student("John Doe", "johndoe@gmail.com", 21)
        self.student.grade[1] = {}
        self.student.grade[1]["math"] = 90
        self.student.grade[1]["chemistry"] = 70

    # test numbers correspond with row highlighted in red in Excel document
    def test1_case1(self):
        with self.assertRaisesRegex(ValueError, r"^Semester not in grades$"):
            self.student.get_grade("math", 2, False)

    def test2_case1(self):
        with self.assertRaisesRegex(ValueError, r"^Subject not in grades$"):
            self.student.get_grade("english", 1, False)

    def test3_case1(self):
        self.assertEqual(self.student.get_grade("math", 1, False), 90)

    def test4_case1(self):
        self.assertEqual(self.student.get_grade("chemistry", 1, True), f"Student {self.student.name} has the grade: "
                                                                       f"70 for the subject: chemistry and"
                                                                       f" semester: {1}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
