from Student import Student

class StructuralTests:
    def test_multiple_condition_coverage(self):
        studentWithGmail = Student(name="John Doe", email="johndoe@gmail.com", age=20)
        assert studentWithGmail.get_platform_username() == "johndoe@gmail.com"

        yahooStudentWithThreeNames = Student(name="John Doe Connor", email="johndoe@yahoo.com", age=20)
        assert yahooStudentWithThreeNames.get_platform_username() == "JDC"

        yahooAdultStudentWithTwoNames = Student(name="John Connor", email="johnconnor@yahoo.com", age=21)
        assert yahooAdultStudentWithTwoNames.get_platform_username() == "JohnConnor"

        yahooTeenStudentWithTwoNames = Student(name="Mark Tyler", email="marktyler@yahoo.com", age=17)
        assert yahooTeenStudentWithTwoNames.get_platform_username() == "MT"

StructuralTests().test_multiple_condition_coverage()