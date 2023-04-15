from Student import Student

class StructuralTests:
    def test_multiple_condition_coverage(self):
        studentWithGmailOver15 = Student(name="John Doe", email="johndoe@gmail.com", age=20)
        assert studentWithGmailOver15.get_platform_username() == "johndoe@gmail.com"

        studentWithYahooUnder15 = Student(name="John Doe", email="johndoe@yahoo.com", age=14)
        assert studentWithYahooUnder15.get_platform_username() == "johndoe@yahoo.com"

        studentWithGmailUnder15 = Student(name="John Doe", email="johndoe@gmail.com", age=14)
        assert studentWithGmailUnder15.get_platform_username() == "johndoe@gmail.com"

        yahooStudentWithThreeNames = Student(name="John Doe Connor", email="johndoe@yahoo.com", age=20)
        assert yahooStudentWithThreeNames.get_platform_username() == "JDC"

        yahooAdultStudentWithTwoNames = Student(name="John Connor", email="johnconnor@yahoo.com", age=21)
        assert yahooAdultStudentWithTwoNames.get_platform_username() == "JohnConnor"

        yahooTeenStudentWithTwoNames = Student(name="Mark Tyler", email="marktyler@yahoo.com", age=17)
        assert yahooTeenStudentWithTwoNames.get_platform_username() == "MT"

    def test_modified_condition_decision(self):
        studentWithGmailOver15 = Student(name="John Doe", email="johndoe@gmail.com", age=20)
        assert studentWithGmailOver15.get_platform_username() == "johndoe@gmail.com"

        studentWithYahooUnder15 = Student(name="John Doe", email="johndoe@gmail.com", age=14)
        assert studentWithYahooUnder15.get_platform_username() == "johndoe@gmail.com"

        yahooStudentWithThreeNames = Student(name="John Doe Connor", email="johndoe@yahoo.com", age=20)
        assert yahooStudentWithThreeNames.get_platform_username() == "JDC"

        yahooAdultStudentWithTwoNames = Student(name="John Connor", email="johnconnor@yahoo.com", age=21)
        assert yahooAdultStudentWithTwoNames.get_platform_username() == "JohnConnor"

        yahooTeenStudentWithTwoNames = Student(name="Mark Tyler", email="marktyler@yahoo.com", age=17)
        assert yahooTeenStudentWithTwoNames.get_platform_username() == "MT"

StructuralTests().test_multiple_condition_coverage()
StructuralTests().test_modified_condition_decision()