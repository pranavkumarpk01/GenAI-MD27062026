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
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >=50:
#     print("Grade C")
# else:
#     print("The student has been failed in the examination")            

#Take the user input from the console and then based on the input mentioned just mention for that amount how much is the discount applicable    

# Switch statement it allows you to execute different blocks of code based on the matched condition
# so u no need to use multiple if-elif block conditions, you can just use match case  to make the code
# more cleaner and easier to read. 

num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second number:"))
operator = input("Enter operator (+,-,*,%):")

match operator:
   case "+":
       print("Result =" , num1 + num2)
   case "-":
       print("Result =", num1 - num2)
   case "*":
       print("Result *", num1 * num2)
   case "%":
       print("Result %", num1 % num2)
   case "_":
       print("Invalid operator")                

# if-elif best for conitions and ranges , switch it is best used for matching fixed values        
# if-elif u can use for complex expressions, Matches specific patterns
# if-elif its available in all python versions,Available for only Python versions greater than Python 3.10+
# if -elif becomes lengthy when there are multiple conditions,  cleaner for choices