#class -> It is a blueprint or template used to create objects
#Advantages
#1.Reusability
#2.Easy to manage
#3.Cleaner code
#4.Real world Represenation

#Import would help u to fetch the fucntionality of other files into the main file
from calculator import Calculator
from student import Student
from employee import Employee

#Creating objects inorder to access the functions defined under each classes
cal = Calculator()
std = Student()
emp = Employee()

cal.add(10,20)
cal.multiply(40,6)

std.display_name()
std.display_age()
std.display_marks()


emp.employee_name()
emp.salary()

