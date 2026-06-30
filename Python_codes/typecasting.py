# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# num1 = int(num1)
# num2 = int(num2)
# print(num1 + num2)

#"10" + "20" = "1020"

#Type casting would help you to convert from one data type to another
#String -> Integer
#Integer -> Float
#Float -> Integer
#Integer -> String 

#Conversion from String to Integer
# age = "22"
# print(type(age))
# age = int(age) #I am converting the data type from string to integer 
# print(type(age))

#Conversion Float to Integer
# price = 99.99
# price = int(price)
# print(price)
#int() removes the decimal part ...It does not the round the number

#Converting Integer to String
# num1 = 56
# num1 = str(num1)
# print(type(num1))
#Converting String to Float

# height = "444"
# height = float(height)
# print(height)
# print(type(height))

#Caluclate Average Marks 
marks1 = float(input("Enter the marks of student1: "))
marks2 = float(input("Enter the marks of student2: "))
marks3 = float(input("Enter the marks of student3: "))

average = (marks1 + marks2 + marks3) / 3
print("Average=", average)