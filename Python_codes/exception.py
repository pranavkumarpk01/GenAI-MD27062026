#Exception handling?
# Prevent Program crashes
# Display user freiendly messages
# Improve reliability
# Handle unexpected situations gracefully
#try block and except block( they both fucntions help u to handle the exceptions)
#try block -> will place the code which I am uncertain about, the error may occur or may not occur I am not sure, I am jsut trying whether this piece of code willl work or no.
#Except block -> If any issue arises in try block then will handle that in except block
#finally -> irreseptive the code runs, completes or fails finally block will execute


#exmaple code

# num1 = int(input("Enter First Number: "))

# num2 = int(input("Enter Second Number: "))

# result = num1 / num2

# print(result)

# print("Program Finished")

try:

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:
     print("Program ended")    