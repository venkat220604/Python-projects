student = {
    "name" : "Dheeraj",
    "roll" : 121,
    "marks" : [90,85,88,91,78],
}
for key,value in student.items():
    print(f"{key} -> {value}")
print(f"Total marks : {sum(student['marks'])}")
avg=sum(student["marks"])/len(student["marks"])
print(f"avgerage:{avg}")
if avg > 35:
    print("pass")
else:
    print("Fail")