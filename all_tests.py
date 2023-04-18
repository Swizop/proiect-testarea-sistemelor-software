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


class TestStudentFunctional(unittest.TestCase):

    def test_constructor(self):
        # Clase de echivalenta
        # Domeniu de intrari:
        # nume string
        # nume alt tip
        # mail string
        # mail alt tip
        # age int
        # age alt tip
        # age < 0
        # Domeniu de iesiri:
        # obiect creat bine
        # value error

        # Le combinam intre ele mai jos
        # nume string, mail string, age int -> obiect creat bine
        student1 = Student("John Doe", "johndoe@example.com", 20)
        self.assertEqual(student1.name, "John Doe")
        self.assertEqual(student1.email, "johndoe@example.com")
        self.assertEqual(student1.age, 20)

        # nume int -> eroare
        with self.assertRaises(ValueError):
            student2 = Student(34, "jane@example.com", 22)

        # mail int -> eroare
        with self.assertRaises(ValueError):
            student3 = Student("John Doe", 34, 22)

        # age str -> eroare
        with self.assertRaises(ValueError):
            student4 = Student("John Doe", "jane@example.com", "Alex")

        # age < 0 -> eroare
        with self.assertRaises(ValueError):
            student5 = Student("John Doe", 34, -3)

    def test_calculate_grade(self):
        # Analiza valorilor de frontieră
        # Scorurile pot fi in intervalul inchis 0, 100
        # Deci avem valori de frontiera pentru toate 3 scorurile:
        # 0, 100
        # 101
        # 101
        # Putem testa si ca scorurile sunt int, cum ne dorim
        # Pe parte de valori de iesire, putem avea si numere cu ,

        student = Student("John Doe", "johndoe@example.com", 20)

        # valori care nu sunt int
        with self.assertRaises(ValueError):
            student.calculate_grade("40", 30, 70)

        with self.assertRaises(ValueError):
            student.calculate_grade(40, 30, "70")

        with self.assertRaises(ValueError):
            student.calculate_grade(40, 30.5, 70)

        # Valori OK
        self.assertEqual(student.calculate_grade(50, 30, 70), 50)
        self.assertEqual(student.calculate_grade(40, 40, 40), 40)

        # Valori limita inferioara, 0
        self.assertEqual(student.calculate_grade(0, 50, 70), 40)
        self.assertEqual(student.calculate_grade(40, 0, 50), 30)
        self.assertEqual(student.calculate_grade(40, 20, 0), 20)
        self.assertEqual(student.calculate_grade(0, 30, 0), 10)
        self.assertEqual(student.calculate_grade(0, 0, 0), 0)

        # Valori sub limita inferioara, (negative, 101)
        with self.assertRaises(ValueError):
            student.calculate_grade(101, 30, 70)
        with self.assertRaises(ValueError):
            student.calculate_grade(70, 101, 70)
        with self.assertRaises(ValueError):
            student.calculate_grade(70, 30, 101)
        with self.assertRaises(ValueError):
            student.calculate_grade(70, 101, 101)
        with self.assertRaises(ValueError):
            student.calculate_grade(101, 101, 101)
        with self.assertRaises(ValueError):
            student.calculate_grade(-14, -36, -122)

        # Valori limita superioara, 100
        self.assertEqual(student.calculate_grade(100, 50, 60), 70)
        self.assertEqual(student.calculate_grade(30, 100, 50), 60)
        self.assertEqual(student.calculate_grade(30, 20, 100), 50)
        self.assertEqual(student.calculate_grade(100, 10, 100), 70)
        self.assertEqual(student.calculate_grade(100, 100, 100), 100)

        # Valori peste limita superioara, (101, > 100)
        with self.assertRaises(ValueError):
            student.calculate_grade(101, 30, 70)
        with self.assertRaises(ValueError):
            student.calculate_grade(70, 101, 70)
        with self.assertRaises(ValueError):
            student.calculate_grade(70, 30, 101)
        with self.assertRaises(ValueError):
            student.calculate_grade(70, 101, 101)
        with self.assertRaises(ValueError):
            student.calculate_grade(101, 101, 101)
        with self.assertRaises(ValueError):
            student.calculate_grade(1002, 103, 45321)

        # Verificare si pe numere cu ,
        self.assertEqual(round(student.calculate_grade(3, 4, 3), 2), 3.33)
        self.assertEqual(round(student.calculate_grade(3, 0, 2), 2), 1.67)

    def test_get_highest_score(self):
        # Partiționarea în categorii
        # Gasim iar valori de frontiera si intervalele lor
        # Avem din nou de-aface cu scoruri, deci interval 0, 100
        # Totusi, in cazul acesta avem frontiere si cand numerele sunt egale
        # Pentru fiecare scor (avem 3), avem cazurile:
        # non-int
        # < -1
        # -1
        # 0
        # 2, 99
        # 100
        # 101
        # > 101
        # Avem cazuri de egalitate:
        # toate diferite
        # Pe langa acesta, cazurile in care numerele sunt egale 2 cate 2
        # score1 cu score2
        # score2 cu score3
        # score3 cu score1
        # Si cazul in care numerele sunt egale toate
        # score1 cu score2 cu score3
        # Deci 5 cazuri totale de egalitate
        #
        # Total am avea: 3 numere * 8 cazuri pt fiecare * 5 cazuri de egalitate = 120 cazuri de testat
        # O sa ne alegem totusi niste constrangeri pentru a avea mai putine
        # Spre exemplu, in cazurile de egalitate, nu trebuie sa testam toate cele 24 de cazuri pentru fiecare
        # E indeajuns sa testam cate unul, astfel reducand foarte mult cazurile de testat

        student = Student("John Doe", "johndoe@example.com", 20)

        # valori care nu sunt int
        with self.assertRaises(ValueError):
            student.get_highest_score("40", 30, 70)

        with self.assertRaises(ValueError):
            student.get_highest_score(40, 30, "70")

        with self.assertRaises(ValueError):
            student.get_highest_score(40, 30.5, 70)

        # Valori OK
        self.assertEqual(student.get_highest_score(50, 30, 70), 70)
        self.assertEqual(student.get_highest_score(70, 40, 10), 70)

        # Valori limita inferioara, 0
        self.assertEqual(student.get_highest_score(0, 50, 70), 70)
        self.assertEqual(student.get_highest_score(40, 0, 50), 50)
        self.assertEqual(student.get_highest_score(40, 20, 0), 40)
        self.assertEqual(student.get_highest_score(0, 30, 0), 30)
        self.assertEqual(student.get_highest_score(0, 0, 0), 0)

        # Valori sub limita inferioara, (negative, 101)
        with self.assertRaises(ValueError):
            student.get_highest_score(101, 30, 70)
        with self.assertRaises(ValueError):
            student.get_highest_score(70, 101, 70)
        with self.assertRaises(ValueError):
            student.get_highest_score(70, 30, 101)
        with self.assertRaises(ValueError):
            student.get_highest_score(70, 101, 101)
        with self.assertRaises(ValueError):
            student.get_highest_score(101, 101, 101)
        with self.assertRaises(ValueError):
            student.get_highest_score(-14, -36, -122)

        # Valori limita superioara, 100
        self.assertEqual(student.get_highest_score(100, 50, 60), 100)
        self.assertEqual(student.get_highest_score(30, 100, 50), 100)
        self.assertEqual(student.get_highest_score(30, 20, 100), 100)
        self.assertEqual(student.get_highest_score(100, 10, 100), 100)
        self.assertEqual(student.get_highest_score(100, 100, 100), 100)

        # Valori peste limita superioara, (101, > 100)
        with self.assertRaises(ValueError):
            student.get_highest_score(101, 30, 70)
        with self.assertRaises(ValueError):
            student.get_highest_score(70, 101, 70)
        with self.assertRaises(ValueError):
            student.get_highest_score(70, 30, 101)
        with self.assertRaises(ValueError):
            student.get_highest_score(70, 101, 101)
        with self.assertRaises(ValueError):
            student.get_highest_score(101, 101, 101)
        with self.assertRaises(ValueError):
            student.get_highest_score(1002, 103, 45321)

        # Valori egale
        self.assertEqual(student.get_highest_score(50, 50, 60), 60)
        self.assertEqual(student.get_highest_score(50, 60, 60), 60)
        self.assertEqual(student.get_highest_score(60, 50, 60), 60)
        self.assertEqual(student.get_highest_score(40, 60, 40), 60)
        self.assertEqual(student.get_highest_score(60, 60, 60), 60)

if __name__ == '__main__':
    unittest.main(verbosity=2)
