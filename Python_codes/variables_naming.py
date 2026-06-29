#1Variable name must start with a letter or underscore, followed by letters, numbers, or underscores.
name = "John"  # Valid variable name
age = 30  # Valid variable name
_address = "123 Main St"  # Valid variable name

1name ="John"  # Invalid variable name (starts with a number)


#2Variable name cannot start with a number.
123= 30 #Invalid variable name (starts with a number)

#3Varibke name can contain only letters,numbers, and underscores
#Allowed characters: letters (a-z, A-Z), numbers (0-9), and underscores (_)

#4 Variable names are case-sensitive.
name ="Alice"  # Valid variable name
Name ="Bob"  # Valid variable name (different from 'name')
NAME ="Charlie"  # Valid variable name (different from 'name' and 'Name')

print(name)  # Output: Alice
print(Name)  # Output: Bob
print(NAME)  # Output: Charlie

#5 Do not use Python Keywords as Variable name.
if = 10
for = "Pranav"
class = 10
True = False

#Python keywords are if , else, for, while, class, def, return, import, True , False, None...

#6.Avoid spaces in variable names
student name ="John"
#can do in this way if required
student_name = "John"
studnetname = "John"

#7 Always choose meaningful varible names
a = 20
b = 50000

age = 20
salary = 50000

#8.Follow Python naming convention(Snake Case)
student_name = "Pranav"
total_marks = 450
phone_number = "9432445032"