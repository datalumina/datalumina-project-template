# 📚 Student Grade Tracker

A command line application that manages students, courses, and grades. Built in Python using object-oriented programming.

---

## 📋 Overview

This app lets you add students, enroll them in courses, record their grades, and view averages — all from the terminal. Data is saved to a JSON file so nothing is lost when you close the app.

---

## 📁 Project Structure

```
student-grade-tracker/
│
├── src/
│   ├── student.py         # Student class
│   ├── course.py          # Course class
│   ├── gradebook.py       # Core logic
│   └── utils.py           # Helper functions
│
├── data/
│   └── students.json      # Saved student data
│
├── main.py                # Entry point / menu
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/student-grade-tracker.git
cd student-grade-tracker
```

**2. Run the app**
```bash
python main.py
```

No external libraries needed — just Python 3!

---

## ✨ Features

- Add and remove students
- Create courses and enroll students
- Record grades per course
- View average grade per course
- View overall GPA per student
- Saves and loads data from JSON automatically

---

## 🧱 How It's Built

The project is split into 4 classes:

| File | Class | Responsibility |
|---|---|---|
| student.py | `Student` | Stores name, ID, and grades per course |
| course.py | `Course` | Stores enrolled students, calculates class average |
| gradebook.py | `Gradebook` | Manages all students and courses, handles saving/loading |
| utils.py | — | Converts grades to letters, calculates GPA |

---

## 📊 Example Output

```
==== Student Grade Tracker ====
1. Add Student
2. Add Course
3. Enroll Student
4. Add Grade
5. View Student Report
6. Exit

Enter choice: 5

Student: Alice Johnson (S001)
  Math:     Average: 88.5  (B)
  English:  Average: 85.25 (B)
  Science:  Average: 88.75 (B)
Overall GPA: 87.5 (B+)
```

---

## 🛠️ Technologies Used

- **Python 3**
- **JSON** — for data storage
- **OOP** — classes and methods throughout

---

## 👤 Author

Gurnoor Pannu — [GitHub](https://github.com/Gpannu77)