def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Function to display all students
def display_students(students):
    print("\n--- Student Grades ---")
    for name, marks in students.items():
        print(f"{name}: {marks} ({calculate_grade(marks)})")

# Main program
students = {}
print("----- Grade Management System -----")

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = float(input("Enter marks (0-100): "))
        students[name] = marks
        print(f"Student '{name}' added successfully!")
    elif choice == '2':
        if students:
            display_students(students)
        else:
            print("No student records found.")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")