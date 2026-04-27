from src.student import Student
from src.course import Course
import json

class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            print(f"Student already exists with ID {student_id}.")
            return
        self.students[student_id] = Student(name, student_id)

    def add_course(self, course_name):
        if course_name in self.courses:
            print(f"Course already exists with name {course_name}.")
            return
        self.courses[course_name] = Course(course_name)
    
    def enroll_student(self, student_id, course_name):
        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            return
        
        if course_name not in self.courses:
            print(f"Course with name {course_name} does not exist.")
            return
        
        self.courses[course_name].add_student(self.students[student_id])
        
    def add_grade(self, student_id, course_name, grade):
        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            return
        if course_name not in self.courses:
            print(f"Course with name {course_name} does not exist.")
            return
        
        self.students[student_id].add_grade(course_name, grade)
    
    def get_student(self, student_id):
        if student_id in self.students:
            return self.students[student_id]
        return None
    
    def get_course(self, course_name):
        if course_name in self.courses:
            return self.courses[course_name]
        return None
    
    def save_data(self, filename):
        data = {'students': {sid: student.to_dict() for sid, student in self.students.items()}}
        with open(filename, 'w') as f:
            json.dump(data, f)
    
    def load_data(self, filename):
        with open (filename, 'r') as a:
            data = json.load(a)
            for sid, student_data in data['students'].items():
                student = Student(student_data['name'], student_data['id'])
                for course, grade in student_data['courses'].items():
                    for g in grade:
                        student.add_grade(course, g)
                self.students[sid] = student