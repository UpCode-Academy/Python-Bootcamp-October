# take a list for example
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements
# which are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
    if num < 5:
        print(num)


# Extras 1:
# Instead of printing the elements one by one, 
# make a new list that has all the elements less than 5 
# from this list in it and print out this new list.
l = []
for num in a:
    if num < 5:
        l.append(num)

print(l)


# Extras 2:
# Ask the user for a number 
# and return a list that contains only elements from the original list 
# that are smaller than that number given by the user.
x = []
number = input("What is your number? ")
for num in a:
    if num < int(number):
        x.append(num)

print(x)