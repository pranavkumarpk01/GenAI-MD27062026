#if condition -> If statement executes a block of code only when the condiiton is true.

# age = int(input("Enter your age: "))
# if age >=18:
#     print("you are eligible to vote")


# balance = float(input("Enter your account balance: "))    

# if balance >= 1000:
#     print("You are eligible for a loan")

#if-else condition -> some based on the input value, it has options to select two paths

# number = int(input("Enter a number: "))
# if number % 2 ==0:
#     print("The number is even")
# else:
#     print("The number is odd")

# age = int(input("Enter your age: "))
# if age >=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")    

#if-elif-else condition -> It is used to check multiple conditions and executes the first matching block
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >=50:
    print("Grade C")
else:
    print("The student has been failed in the examination")            