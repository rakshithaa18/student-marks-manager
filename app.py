students = {}

def add_student(name, marks):
    students[name] = marks
    print(f"{name} added with marks {marks}.")

def update_student(name, marks):
    if name in students:
        students[name] = marks
        print(f" {name}'s marks updated to {marks}.")
    else:
        print(" Student not found.")

def delete_student(name):
    if name in students:
        del students[name]
        print(f" {name} deleted from records.")
    else:
        print("Student not found.")

def search_student(name):
    if name in students:
        print(f" {name}'s marks: {students[name]}")
    else:
        print(" Student not found.")

def display_all():
    if not students:
        print(" No student records found.")
    else:
        print("\n Student Records:")
        for name, marks in students.items():
            print(f"- {name}: {marks}")

while True:
    print("\n===== Student Marks Manager =====")
    print("1️ Add Student")
    print("2️ Update Marks")
    print("3️ Delete Student")
    print("4️ Search Student")
    print("5️ Display All")
    print("6️ Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        add_student(name, marks)
    elif choice == '2':
        name = input("Enter student name to update: ")
        marks = input("Enter new marks: ")
        update_student(name, marks)
    elif choice == '3':
        name = input("Enter student name to delete: ")
        delete_student(name)
    elif choice == '4':
        name = input("Enter student name to search: ")
        search_student(name)
    elif choice == '5':
        display_all()
    elif choice == '6':
        print(" Exiting Student Marks Manager. Goodbye!")
        break
    else:
        print(" Invalid choice. Try again!")