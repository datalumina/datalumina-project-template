from src.gradebook import Gradebook


def print_menu():
    print("\n====Student Grade Tracker====")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Add Grade")
    print("5. View Student Grades")
    print("6. Exit")


def main():
    gradebook = Gradebook()
    try:
        gradebook.load_data("data/gradebook.json")
    except FileNotFoundError:
        print("No saved data found, starting fresh.")
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            student_name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            gradebook.add_student(student_id, student_name)
        elif choice == "2":
            course_name = input("Enter course name: ")
            gradebook.add_course(course_name)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            gradebook.enroll_student(student_id, course_name)
        elif choice == "4":
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.add_grade(student_id, course_name, grade)
        elif choice == "5":
            student_id = input("Enter student ID to view: ")
            student = gradebook.get_student(student_id)
            if student:
                print(f"Grades for {student.name} (ID: {student.student_id}): ")
                for course, grade in student.courses.items():
                    print(f"{course}: {grade}")
        else:
            try:
                gradebook.save_data("data/gradebook.json")
            except Exception as e:
                print(f"Error saving data: {e}")
            break


if __name__ == "__main__":
    main()
