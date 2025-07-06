print("student mark list")
marks=[]
for i in range(1,6):
    mark=int(input(f"enter subect makrks {i}"))
    marks.append(mark)
total=sum(marks)
average=total/len(marks)
highest=max(marks)
lowest=min(marks)
if average>=90:
    performence="Excellent"
elif average>=70:
    performence="Good"
else:
    performence="Needs Imporvement"
print("Report")
print("Tolatal marks",total)
print("average marks",average)
print("peformence",performence)
print("Highest marks",highest)
print("Lowest marks",lowest)
