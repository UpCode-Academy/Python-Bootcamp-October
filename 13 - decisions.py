# second simple program

print("You just entered a dark room... There are two doors.... Which will you choose? Door #1 or Door #2?")
door = input(">. ")

if door == "1":
    print("Door 1 was chosen.")
    
    print("""
    There's a giant bear here eating a cheese cake. What do you do?
    1. Take the cake.
    2. Scream at the bear.
    """)
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)
    
elif door == "2":
    print("Door 2 was chosen.")
else:
    print("You stumbled around and fell on a knife and died. Good job!")