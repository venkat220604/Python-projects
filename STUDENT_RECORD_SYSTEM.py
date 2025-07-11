class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        return sum(self.marks)/len(self.marks)
    def result(self):
        return "Pass" if self.average() >= 35 else "Fail"
    def save_to_file(self):
        with open("student_records.txt","a") as f:
            f.write(f"{self.name} - {self.marks}\n")
s1=Student("Dheeraj",[85,90,80])
s1.save_to_file()
with open("student_records.txt","r") as f:
    print(f.read())