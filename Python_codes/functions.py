#A fuction is a block of reusable code that performs a specific task
#Instead of writing the same code multiple times, we write it once inside a fucntion and call it whenever needed 

#def function_name():
    #code

# def greet():
#     print("welcome to python")
    
#Function calling
# greet()     

# def display():
#     print("Hello")
#     print("Good Morning")

# display()

# print("Welcome")
# print("Welcome")
# print("Welcome")

# def welcome():
#     print("Welcome")


# welcome()
# welcome()
# welcome()    

#Parameters
#This are the variables written inside the function definition
#def function(parameter):

# def greet(name):
#     print("Hello" , name )

# greet("Pranav")    
# "Pranav" -> Arguement
# name -> parameter

#multiple params
# def student(number:int , age: int):
#     print(number)
#     print(age)

# student(age = 36,number =24)#Keyword arguements
# student(24 , 36) #Positional arguements
# # student("Manish",32)
# # student("Shashi",12)

#Return statement sends the results back to wherever the function was called
# def addition_print(a , b):
#     print(a + b)

# result = addition_print(3,2)

# print(result)

# def addition_return(a, b):
#     return a + b

# result = addition_return(5, 5)

# print(result)

#Understand about Local variable and global variable

#*args -> allows to handle multiple arguements

# def number(*numbers):
#     print(numbers)

# number(10,20,30)    
#**kwargs -> alllows to handle multiple positional arguements
# def student(**details):
#     print(details)
# student(name="Pranav", age=12 ,city="Mysore")    

#Advantages of function
#code reusability
#Easy maintainence
#code readability
#Less code
#Easy  debuging 

#write a calcultor application using the fucntions add, sub , divide and multiply