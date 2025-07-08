n=int(input("ENTER NUMBER OF STUDENTS"))
with open("attendendence.txt","w") as file:
    for _ in range(n):
        name = input("ENTER STUDENT NAME")
        status=input("Present(p)/ Absent(A)")
        file.write(f"{name}-{status}\n")
print("attendendence Saved ")
with open("attendendence.txt","r")as file:
    print("ATTEDENDCE REPORT\n")
    print(file.read())
   
    
