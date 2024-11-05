def main():
    n = int(input("Enter number of students: "))
    
    students = []

    for _ in range(n):
        roll_number = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = tuple(int(input(f"Enter marks for Subject {i}: ")) for i in range(1, 4))
        students.append((roll_number, name, marks))

    print("\nStudents with name 'Python':")
    for student in students:
        if student[1] == "Python":
            print(f"Roll Number: {student[0]}, Marks: {student[2]}")

main()
