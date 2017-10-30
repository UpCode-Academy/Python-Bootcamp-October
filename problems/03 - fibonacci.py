# what is fibonacci?
# fibonacci is a sequence of numbers that starts with 1, 1 
# and the next number is the sum of the two before that

# example, [1, 1, 2, 3, 5, 8, 13, 21, 34...]

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

def gen_fib(count):
    if count == 0:
        return []
    elif count == 1:
        return [1]
    elif count == 2:
        return [1, 1]
    elif count > 2:
        # append to the list with the new value
        # refer to the list that we are creating using the -1 index to refer to the last element
        # and using the -2 index to refer to the second last element
        fib = [1, 1]
        while len(fib) < count:
            fib.append(fib[-2] + fib[-1])
        return fib
    return []

count = int(input("Enter a number for the Fibonnaci sequence: "))

print(gen_fib(count))