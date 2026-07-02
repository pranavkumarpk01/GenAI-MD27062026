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
password = "python123"
user = " "
while user != password:
     user = input("Enter Password: ")

print("Access Granted")

#write a program for ATM pin verification 