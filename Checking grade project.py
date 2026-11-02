#Checking grade of College student
def checkingGrades(marks):
    if marks < 0 or marks > 100:
        print("Invalid percentage! Enter marks from 0 to 100.")
    elif marks > 90:
        print("Grade-A")
    elif marks > 80:
        print("Grade-B")
    elif marks > 70:
        print("Grade-C")
    elif marks > 60:
        print("Grade-D")
    elif marks > 50:
        print("Grade-E")
    else:
        print("Re-Appear")


print("Welcome to B.Tech Grade Checker!")

try:
    marks = float(input("Enter your B.Tech percentage: "))
    checkingGrades(marks)
except ValueError:
    print("Invalid input! Please enter a number.")
