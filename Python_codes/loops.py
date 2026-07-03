#Loops -> it allows you to execut a block of code multiple times without writing the same code repeatedly..
#for loop 
#for loop is used when u know how many times you want to repeat a task
#syntax -> for variable in sequence:

# for i in range(5):
#     print(i)


#for i in range(1,6):
#    print(i)
#In the above program you have specified from where the loop should start and should end at which position.

# for i in range(2,11,2):
#     print(i)

#range(start,stop,step) , step is defined to make sure the start value takes subsequent jumps as mentioned in the loop
#Print multiples of 7
# for i in range(7,71,7):
#     print(i)

#while loop it helps you to execute a block of code as long as a condition remains true
# i =1 #Intialisation(Your telling that thr value of i will start form 1)
# while i <=5:
#     print(i)
#     i += 1

# iteration
# i =1     , 1<=5 , print(1) ,i = i+1 , i = 1+1 , i =2 
# i = 2  , 2<=5 , print(2) , i = 2+1 , i =3
# i = 3  , 3<=5 , print(3), i = 3+1 , i=4
# i = 4  , 4<=5,  print(4), i = 4+1 , i=5
# i = 5,   5<=5 , print(5), i = 5=1 , i=6
# i= 6,    6<=5 -> no your loop will break

#Password Retry
# password = "python123"
# user = " "
# while user != password:
#      user = input("Enter Password: ")

# print("Access Granted")

#write a program for ATM pin verification 

#Difference between while and for loop
# Fearture         forloop.                 whileloop
# Iteration.         nown                    unknown
# condtion.       range or sequence.         pure condtion based
# Intialisation    Automatic                 Manually
# update            Automatic                Logically
# infinite loop      low                     high
# Best use          Fixed no of repetations. condition driven repetition

#Nested loops , continue , break , pass
#keywords -> Research and try to understand wat does continue, break and pass does.

# Nested loop -> You define one loop inside another loop.

# for i in range(3):
#     for j in range(2):
#         print(i,j)

#first the execution will start togehter and then post execution the inner loop will complete its fucntionality and then again it will go to outer loop

for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()    

#end() will help u to go to end of the line
