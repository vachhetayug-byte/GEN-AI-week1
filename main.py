import json

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.loads(file.read())
    except:
        return {}

def save_students(students):
    with open("students.json", "w") as file:
        file.write(json.dumps(students, indent=4))

def add_student(students):
    name = input("Enter student name: ").strip()

    if name in students:
        print("Student already exists!")
        return

    marks = int(input("Enter marks: "))
    students[name] = marks
    print(f"{name} added successfully.")

def view_students(students):
    if len(students) == 0:
        print("No students found.")
        return

    print("\nStudent Records:")
    for name, marks in students.items():
        print(f"Name: {name} | Marks: {marks}")

def search_student(students):
    name = input("Enter name to search: ").strip()

    if name in students:
        print(f"{name} scored {students[name]} marks")
    else:
        print("Student not found")

def average_marks(students):
    if len(students) == 0:
        print("No records available")
        return

    marks_list = list(students.values())
    avg = sum(marks_list) / len(marks_list)

    print(f"Average Marks: {avg:.2f}")

def main():
    students = load_students()

    while True:
        print("\n===== MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Average Marks")
        print("5. Save and Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            average_marks(students)

        elif choice == "5":
            save_students(students)
            print("Data saved successfully.")
            break

        else:
            print("Invalid Choice")

main()
