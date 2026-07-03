#Dictonary stores data in the form of Key value pairs
#Each key will be assigned with a value

#Properties
#Mutable
#Keys are unique
#Values can be duplicated
#uses key instead of indexes

# student ={
#     "name":["Pranav","satish","Dhoni"],
#     "age":29,
#     "city":"banglore",
#     "Pincode":563333
# }

# print(student["name"])
# print(student["Pincode"])
# print(student["name"][0])#indiviudally accessing the elements and printing it
# print(student["name"][2])#indiviudally accessing the elements and printing it

#Print all the keys and values

# student ={
#     "name":"Pranav",
#     "age":29,
#     "city":"banglore",
#     "Pincode":563333
# }
# #student.items() help u to fetch complete data of defined dictionary
# for i,j in student.items():
#     print(i,":",j)

#Add a new key

student ={
    "Name": "pranav",
    "Age" :22
}

student["Marks"] = 90

print(student)

#write a program to check if a key exists

# write a program to check key exist or not
student = {'name': 'Pranav', 'age': 25, 'city': 'New York'}   
if 'name' in student:
    print("Key 'name' exists in the dictionary.")
else:
    print("Key 'name' does not exist in the dictionary.")