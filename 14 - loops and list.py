# look at the data type of list
# "words" is a string
# "abc" is a string
# "xyz" is a string
# 1 is an integer
# 1.0 is a float/decimal
# "11" is a string

the_count = [1, 2, 3, 4, 5] # this is a list
print(the_count[1])

fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# looping through lists
for num in the_count:
    print("This is count %d" % num)
    
for fruit in fruits:
    print("A fruit of type: %s" % fruit)
    
for x in change:
    print("I got %r" % x)
    
# building a list
elements = []

for i in range(0, 6):
    print("Adding %d to the list." % i)
    elements.append(i)
    
print(elements)

elements.append(6)

print(elements)

elements.append("dogs")

print(elements)







