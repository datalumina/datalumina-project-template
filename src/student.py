class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}
    
    def add_grade(self, course, grade):
        if course not in self.courses:
            self.courses[course] = []
        self.courses[course].append(grade)
    
    def get_average(self, course):
        if course not in self.courses:
            return 0
        return sum(self.courses[course]) / len(self.courses[course])
    
    def get_overall_average(self):
        total_courses = len(self.courses)
        if total_courses == 0:
            return 0
        total_average = 0
        for course in self.courses:
            total_average += self.get_average(course)
        return total_average / total_courses
    
    def to_dict(self):
        return {
            'id': self.student_id,
            'name': self.name,
            'courses': self.courses
        }
    
    def __str__(self): return f"Student: {self.name}, ID: {self.student_id}, Courses: {self.courses}"