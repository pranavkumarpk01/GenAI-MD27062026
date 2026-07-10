file = open("notes.txt","w")
file.write("Pranav is the best")
file.close()


#Append
file = open("notes.txt","a")
file.write("\nshashi is the best")
file.close()

#\n is the newline character helps you to push your code to the next line

#why do we need to close our files with the use of file.close() . 
# Memory releaseed if file is closed
#your code corruption
#Resource released