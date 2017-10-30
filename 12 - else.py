people = 30
cars = 40
buses = 15

if cars > people:
    print("we should take cars")
elif cars < people:
    print("we should not take cars")
else:
    print("we cannot decide")
    
# buses = 40
if buses > cars:
    print("That's too many buses!")
elif buses < cars:
    print("Maybe we should take the buses!")
else:
    print("we cannot decide")
    
# people = 10
if people > buses:
    print("alright... let's just take the buses!")
else:
    print("fine... let's just stay at home then.")