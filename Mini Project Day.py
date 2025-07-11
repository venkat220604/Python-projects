class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def to_string(self):
        return f"{self.name},{self.roll},{self.marks}\n"    
def add_student():
    name =input("Enter Name")
    roll = input("Enter Roll No")
    marks = input("Enter Marks")
    s=Student(name,roll,marks)
    with open("student.txt","a") as f:
        f.write(s.to_string())
    print("Student Added ! \n")
def display_all():
    print("\n All students")
    with open("students.txt","r") as f:
        print(f.read())
def search_student():
    search_name=input("enter name to search")
    found = False

    with open("students.txt","r") as f:
        for line in f :
            if search_name.lower() in line.lower():
             print("Found :",line.strip())
             found = True
    if not found:
        print("Student not Found. \n")
while True:
    print("\n === STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search Student")
    print("4. Exit")
    choice = input("Enter choice from (1-4)")
    if choice == "1" :
        add_student()
    elif choice == "2" :
        display_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting.. bye")
        break
    else:
        print("Invalid choice")