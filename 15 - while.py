# in this script, we will learn about while loops
i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)
    
    i = i + 1 # same as i+=1
    print("Numbers now is:", numbers)
    
    print("At the bottom i is %d" % i)
    
    print("\n\n\n\n\n")
    
print("The numbers: ")
for num in numbers:
    print(num)