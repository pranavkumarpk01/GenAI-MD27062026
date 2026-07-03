#It is an ordered collection of items that can store different data types.Lists are mutable , meaning \
#you can add , or remove items after creating it
#Properties
#1.Ordered
#2.Mutable
#3.Allows duplicate values
#4.Indexed(starts from 0)

# mylist = [10,20,30,40]

# fruits = ['apple','orange','watermelon']
           
# print(fruits)
# print(fruits[2])

# numbers =[10,20,30,40,50,40,50]

# for num in numbers:
#     print(num)

# fruits = ["Apple" , "Banana"]
# #In built method in list called as append
# fruits.append("Mango")
# fruits.remove("Apple")
# print(fruits)

#Find the sum of the defined list
numbers = [5,10,15,20]
total = 0
for num in numbers:
    total = total + num
print(total)