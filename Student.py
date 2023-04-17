import re


class Student:
    def __init__(self, name, email, age):
        """
        Class which saves basic info about student, also contains each student grades for each semester and subject

        :param name: the name of the student
        :param email: the email of the student
        :param age: the age of the student
        """
        self.name = name
        self.email = email
        self.age = age
        self.grade = {}

    def insert_grade(self, new_grade, subject, semester, replace):
        """
        Inserts a grade for the student for the corresponding semester and subject. If replace evaluates to true
        it can replace the grade if it already exists

        :param new_grade: the new grade to be inserted
        :param subject: the name of the subject for which the grade is for
        :param semester: the semester in which the grade was given
        :param replace: allows to replace the grade if it already exists if it evaluates to true
        :raises ValueError: if new_grade not between 0-100 or subject is empty or semester not between 1-2
        :raises AttributeError: if self.grade[semester][subject] already exists and replace evaluates to false
        """

        if new_grade < 0 or new_grade > 100:
            raise ValueError("Invalid grade! Grade cannot be negative and cannot exceed 100.")
        if len(subject) == 0:
            raise ValueError("Invalid subject! Subject cannot be empty.")
        if semester < 0 or semester > 2:
            raise ValueError("Invalid semester! Semester cannot be negative and cannot exceed 2")
        if semester not in self.grade:
            self.grade[semester] = {}
        if subject not in self.grade[semester] or replace:
            self.grade[semester][subject] = new_grade
        else:
            raise AttributeError(f"Grade for semester: '{semester}' and subject '{subject}' already exists.")

    def get_grade(self, subject, semester, output_format):
        """
        Returns the grade for the student which corresponds to the given semester and subject. If output_format
        evaluates to true then it returns a formatted output which shows detailed information about the query
        (given subject and semester) and the student name

        :param subject: the subject for which to search the grade
        :param semester: the semester in which to search the grade
        :param output_format: allows to format the output to give more details, specifying student name, the given subject and semester if it evaluates to true
        :return: the grade for the student corresponding to the given semester and subject
        :raises ValueError: if semester not in self.grade or subject not in self.grade[semester]
        """
        if semester not in self.grade:
            raise ValueError("Semester not in grades")
        if subject not in self.grade[semester]:
            raise ValueError("Subject not in grades")
        if not output_format:
            return self.grade[semester][subject]
        else:
            return f"Student {self.name} has the grade: {self.grade[semester][subject]} for the subject: {subject} and" \
                   f" semester: {semester}"

    def calculate_grade(self, score1, score2, score3):
        average = (score1 + score2 + score3) / 3
        return average

    def get_email_domain(self, email, separator, index):
        parts = email.split(separator)
        domain = parts[index]
        return domain

    def is_adult(self, age, threshold):
        return age >= threshold

    def get_platform_username(self):
        if self.email.endswith('yahoo.com') and self.age > 15:
            names = self.name.split(" ")
            if len(names) > 2:
                return f"{names[0][0]}{names[1][0]}{names[2][0]}"
            elif self.age > 18:
                return "".join(names)
            else:
                return f"{names[0][0]}{names[1][0]}"
        else:
            return self.email

    def calculate_final_grade(self, score1, score2, score3):
        scores = [score1, score2, score3]
        lowest_score = scores[0]
        for score in scores:
            if score < lowest_score:
                lowest_score = score
        scores.remove(lowest_score)
        final_grade = sum(scores) / len(scores)
        return final_grade

    def get_highest_score(self, score1, score2, score3):
        highest_score = score1
        if score2 > highest_score:
            highest_score = score2
        if score3 > highest_score:
            highest_score = score3
        return highest_score
