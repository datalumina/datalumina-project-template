class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = {}
    
    def add_student(self, student):
        self.students[student.student_id] = student 
    
    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
    
    def get_class_average(self):
        total_students = len(self.students)
        if total_students == 0:
            return 0
        avg = 0
        for student in self.students.values():
            avg += student.get_overall_average()
        return avg / total_students
    
    def get_student(self, student_id):
        if student_id in self.students:
            return self.students[student_id]
        return None
    
    def __str__(self):
        return f"Course: {self.course_name}, Students: {len(self.students)}"