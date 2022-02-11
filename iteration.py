#We will write a while loop which asks for the users name, 
#then prints the user's name followed by "is awesome!" 5 times.

count = 0 

while count < 5:
    name = input("Please enter your name: ")
    print(name, "is awesome!")
    count += 1
