name=input("enter student name:")
n=int(input("enter number of subjects"))
total=0
for i in range(1,n+1):
    mark=float(input("enter mark"))
    total+=mark
    percentage=total/n
    if percentage>=90:
        grade="A+"
        performance="outstanding"
    elif percentage >=80:
        grade="A"
        performance="Excellent"
    elif percentage>=70:
        grade="B"
        performance="very good"
    elif percentage>=60:
        grade="c"
        performance="good"
    elif percentage>=50:
        grade="D"
        performance="Average"
    else:
        grade="F"
        performance="needs improvement"
print("Academic performance")
print("student name:",name)
print("total marks:",total)
print("grade:",grade)
print("performance:",performance)