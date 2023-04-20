import pathlib
import sys
import unittest

directory = str(pathlib.Path(__file__).parent.parent.resolve())
sys.path.append(directory)

from Student import Student


class StructuralTests(unittest.TestCase):

    def test_multiple_condition_coverage(self):
        # CONDITIONS: email is yahoo; age over 15; has more than 2 names; age over 18

        # FALSE, FALSE, FALSE, FALSE
        studentWithGmailUnder15 = Student(name="John Doe",
                                          email="johndoe@gmail.com",
                                          age=14)
        self.assertEqual(studentWithGmailUnder15.get_platform_username(), "johndoe@gmail.com")

        # FALSE, FALSE, TRUE, FALSE
        studentGmailUnder15ThreeNames = Student(name="John Doe Little",
                                                email="johndoe@gmail.com",
                                                age=14)
        self.assertEqual(studentGmailUnder15ThreeNames.get_platform_username(), "johndoe@gmail.com")

        # FALSE, TRUE, FALSE, FALSE
        studentGmail16TwoNames = Student(name="John Doe",
                                         email="johndoe@gmail.com",
                                         age=16)
        self.assertEqual(studentGmail16TwoNames.get_platform_username(), "johndoe@gmail.com")

        # FALSE, TRUE, FALSE, TRUE
        studentWithGmailOver15 = Student(name="John Doe",
                                         email="johndoe@gmail.com",
                                         age=20)
        self.assertEqual(studentWithGmailOver15.get_platform_username(),"johndoe@gmail.com")

        # FALSE, TRUE, TRUE, FALSE
        studentGmail16ThreeNames = Student(name="John Doe Matei",
                                           email="johndoe@gmail.com",
                                           age=16)
        self.assertEqual(studentGmail16ThreeNames.get_platform_username(), "johndoe@gmail.com")

        # FALSE, TRUE, TRUE, TRUE
        studentGmail20ThreeNames = Student(name="John Doe Matei",
                                           email="johndoe@gmail.com",
                                           age=20)
        self.assertEqual(studentGmail20ThreeNames.get_platform_username(), "johndoe@gmail.com")

        # TRUE, FALSE, FALSE, FALSE
        studentWithYahooUnder15 = Student(name="John Doe",
                                          email="johndoe@yahoo.com",
                                          age=14)
        self.assertEqual(studentWithYahooUnder15.get_platform_username(), "johndoe@yahoo.com")

        # TRUE, FALSE, TRUE, FALSE
        studentYahooThreeNamesUnder15 = Student(name="John Doe Matei",
                                                email="johndoe@yahoo.com",
                                                age=14)
        self.assertEqual(studentYahooThreeNamesUnder15.get_platform_username(), "johndoe@yahoo.com")

        # TRUE, TRUE, FALSE, FALSE
        yahooTeenStudentWithTwoNames = Student(name="Mark Tyler",
                                               email="marktyler@yahoo.com",
                                               age=17)
        self.assertEqual(yahooTeenStudentWithTwoNames.get_platform_username(), "MT")

        # TRUE, TRUE, FALSE, TRUE
        yahooAdultStudentWithTwoNames = Student(name="John Connor",
                                                email="johnconnor@yahoo.com",
                                                age=21)
        self.assertEqual(yahooAdultStudentWithTwoNames.get_platform_username(), "JohnConnor")

        # TRUE, TRUE, TRUE, FALSE
        yahoo16StudentThreeNames = Student(name="John Connor MARK",
                                           email="johnconnor@yahoo.com",
                                           age=16)
        self.assertEqual(yahoo16StudentThreeNames.get_platform_username(), "JCM")

        # TRUE, TRUE, TRUE, TRUE
        yahooStudentWithThreeNames = Student(name="John Doe Connor",
                                             email="johndoe@yahoo.com",
                                             age=20)
        self.assertEqual(yahooStudentWithThreeNames.get_platform_username(), "JDC")

    def test_modified_condition_decision(self):
        # Decisions: FALSE, FALSE, TRUE. Conditions: FALSE, TRUE, FALSE, TRUE
        studentWithGmailOver15 = Student(name="John Doe",
                                         email="johndoe@gmail.com",
                                         age=20)
        self.assertEqual(studentWithGmailOver15.get_platform_username(), "johndoe@gmail.com")

        # Decisions: FALSE, FALSE, FALSE. Conditions: FALSE, FALSE, FALSE, FALSE
        studentWithYahooUnder15 = Student(name="John Doe",
                                          email="johndoe@gmail.com",
                                          age=14)
        self.assertEqual(studentWithYahooUnder15.get_platform_username(), "johndoe@gmail.com")

        # Decisions: TRUE, TRUE, TRUE. Conditions: TRUE, TRUE, TRUE, TRUE
        yahooStudentWithThreeNames = Student(name="John Doe Connor",
                                             email="johndoe@yahoo.com",
                                             age=20)
        self.assertEqual(yahooStudentWithThreeNames.get_platform_username(), "JDC")

        # Decisions: TRUE, FALSE, TRUE. Conditions: TRUE, TRUE, FALSE, TRUE
        yahooAdultStudentWithTwoNames = Student(name="John Connor",
                                                email="johnconnor@yahoo.com",
                                                age=21)
        self.assertEqual(yahooAdultStudentWithTwoNames.get_platform_username(), "JohnConnor")

        # Decisions: TRUE, FALSE, FALSE. Conditions: TRUE, TRUE, FALSE, FALSE
        yahooTeenStudentWithTwoNames = Student(name="Mark Tyler",
                                               email="marktyler@yahoo.com",
                                               age=17)
        self.assertEqual(yahooTeenStudentWithTwoNames.get_platform_username(), "MT")


if __name__ == '__main__':
    unittest.main()