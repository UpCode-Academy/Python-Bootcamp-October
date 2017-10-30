# functions are important!!!
def add(a, b):
    print("Adding %d + %d" % (a, b))
    return a + b
    
def subtract(a, b):
    print("Subtracting %d - %d" % (a, b))
    return a - b
    
def multiply(a, b):
    print("Muliplying %d * %d" % (a, b))
    return a * b
    
def divide(a, b):
    print("Dividing %d / %d" % (a, b))
    return a / b

# write a simple calculator!
# can you guys create the subtract, miultiply and divide functions!    
    
age = add(30, 5)
print(age)

# test them out here!
print(subtract(25, 10)) # result should be 15
print(multiply(4, 3)) # result should be 12
print(divide(100, 2)) # result should be 50


print("\n\n\n\n\n\n\n")


# this is a puzzle
print(add(12, divide(16, multiply(subtract(3, 2), 4))))
