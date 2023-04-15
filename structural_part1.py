from Student import Student

class TestStudent:

    def test_constructor(self):
        student = Student("John Doe", "johndoe@example.com", 20)
        assert student.name == "John Doe"
        assert student.email == "johndoe@example.com"
        assert student.age == 20

    # this covers statement, condition and decision covarage
    def test_calculate_grade(self):
        student = Student("John Doe", "johndoe@example.com", 20)
        assert student.calculate_grade(80, 90, 85) == 85.0
        assert student.calculate_grade(70, 75, 65) == 70.0

    def test_get_email_domain_statement_coverage(self):
        student = Student("John Doe", "johndoe@example.com", 20)
        assert student.get_email_domain("johndoe@example.com", "@", 1) == "example.com"

    # this covers condition and decision covarage
    def test_get_email_domain_decision_condition_coverage(self):
        student = Student("John Doe", "johndoe@example.com", 20)
        assert student.get_email_domain("johndoe@example.com", "@", 1) == "example.com"

    def test_is_adult_statement_coverage(self):
        student = Student("John Doe", "johndoe@example.com", 20)
        assert student.is_adult(18, 18) == True
        assert student.is_adult(20, 18) == True
        assert student.is_adult(16, 18) == False

    # this covers condition and decision covarage
    # similar function as before just do differentiate between
    # statement and decision/condition covarage
    def test_is_adult_decision_condition_coverage(self):
        student = Student("John Doe", "johndoe@example.com", 20)
        assert student.is_adult(18, 18) == True
        assert student.is_adult(20, 18) == True
        assert student.is_adult(16, 18) == False
        assert student.is_adult(18, 20) == False

    # this covers statement, condition and decision covarage
    def test_calculate_final_grade(self):
        student = Student("John Doe", "johndoe@example.com", 20)
        assert student.calculate_final_grade(80, 90, 85) == 87.5
        assert student.calculate_final_grade(70, 75, 65) == 72.5
        assert student.calculate_final_grade(80, 85, 80) == 82.5

    # this covers statement, condition and decision covarage
    def test_get_highest_score_decision_coverage(self):
        student = Student("John Doe", "johndoe@example.com", 20)
        assert student.get_highest_score(80, 90, 85) == 90
        assert student.get_highest_score(70, 75, 65) == 75
        assert student.get_highest_score(85, 80, 90) == 90
        assert student.get_highest_score(80, 85, 80) == 85


