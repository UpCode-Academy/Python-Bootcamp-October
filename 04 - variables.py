# variables are like algebras....
cars = 100
print("There are", cars, "cars in the market.")

spaces_in_a_car = 4.0
drivers = 30
passengers = 90

cars_driven = drivers # each driver drive 1 car,
cars_not_driven = cars - drivers # the cars with no drivers are not driven

carpool_capacity = cars_driven * spaces_in_a_car # total spaces available in the car
average_passengers_per_car = passengers / cars_driven # finding the average

print("There are", cars_not_driven, "cars not driven.")
print("We can transport", carpool_capacity, "total passengers.")
print("On average, we will have", average_passengers_per_car, "in each driven car.")