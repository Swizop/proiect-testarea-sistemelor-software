class Student:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def calculate_grade(self, score1, score2, score3):
        average = (score1 + score2 + score3) / 3
        return average
    
    def get_email_domain(self, email, separator, index):
        parts = email.split(separator)
        domain = parts[index]
        return domain
    
    def is_adult(self, age, threshold):
        return age >= threshold
    
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
