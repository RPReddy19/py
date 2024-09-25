"""
Assignment-1:
WAP to assign 3 values (string, int, float)
to 3 variables (Student_name, Roll_Number, Percentage_of_marks).
print the values using print function.
"""
print("Assignment:1")
Student_name=input("Enter student name: ")
Roll_Number=int(input("Enter Roll Number: "))
percentage=float(input("Enter Percentage of marks: "))
print(Student_name,Roll_Number,percentage)
"""
Assignment-2:
WAP to assign value 6 to two different variables (example: a1, b1) 
using single line of code.
Check the variable values and memory address.
"""
print("Assignment:2")
a1=b1=6
print("a1=",a1,"b1=",b1)
assert id(a1)==id(b1), "a1 and b1 variable are in different location"
"""
Assignment-3:
WAP to assign multiple values to multiple variables
in single line of code
"""
print("Assignment:3")
name,age,per="vishnu",24,89.67
print(name,age,per)
