#Times Table Grid:

#Given an integer n, write a python application which returns a times table grid for all the integers between 1 and n.
#The grid should be separated by tabs and new lines.

#For example, given n = 4 it should return the grid

#1  2   3   4
#2  4   6   8
#3  6   9   12
#4  8   12  16


#Example 1
n = int(input("Enter number: "))

line = ""

for row in range(1, n+1):
    for column in range(1, n+1):
        line = line + str(row*column) + "\t"
    line = line + "\n"

print(line)

#Example 2
n = int(input("Enter an integer: "))

for row in range(1, n+1):
    for col in range(1, n+1):
        print(row*col, end='\t')
    print()