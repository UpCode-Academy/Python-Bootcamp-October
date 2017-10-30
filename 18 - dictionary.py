things = ['a', 'b', 'c', 'd'] # list
print(things[1])

things[1] = "z"
print(things)

stuff = {'name': 'ZP', 'age': 29, 'height': 9*19+2} # dictionary

print(stuff['name'])
print(stuff['height'])

stuff['city'] = "Singapore"
print(stuff['city'])

# create a mapping of state to abrv
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in it
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 40)
print("NY State has: ", cities['NY'])
print('OR State has: ', cities['OR'])

print('-' * 40)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])


# do printing by using the state then cities dict
print('-' * 40)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# loop
print('-' * 40)
for state, abrev in states.items():
    print("%s is abbreviated %s" % (state, abrev))

# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }

print('-' * 40)
for abrev, city in cities.items():
    print("%s has the city %s" % (abrev, city))

# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }

print('-' * 40)
for state, abrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abrev, cities[abrev]))

# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }  
    
print('-' * 40)
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas.")
    
city = cities.get("TX", "Does Not Exist")
print("The city for the state 'TX' is: %s" % city)
    
    
    