# ask for user input on the city they will be flying to and create options for the user to choose from
city_flight = input("Enter the city you will be flying to: Cape Town, Durban or Port Elizabeth ")
# create a list of available cities
available_cities = ["Cape Town", "Durban", "Port Elizabeth"]
# check if the input city is in the list of available cities
if city_flight in available_cities:
    print(f"You have chosen to fly to {city_flight}.")
else:
    print(f"{city_flight} is not an available option. Please choose from Cape Town, Durban or Port Elizabeth.") 
# ask for user input on the number of nights they will be staying in a hotel
num_nights = int(input("How many nights will you be staying in the hotel? "))
# ask for user input on the number of days they will be renting a car
rental_days = int(input("How many days will you be renting a car? "))
# create a function to calculate the hotel cost with the input from num_nights
def hotel_cost(num_nights, hotel_rate=100):
    return num_nights * hotel_rate
hotel_total_cost = hotel_cost(num_nights)
#print a message to the user with the hotel cost
print(f"The total cost of your hotel stay for {num_nights} nights is: R{hotel_total_cost}")
# create a function to calculate the car rental cost with the input from rental_days
def car_rental(rental_days, rental_rate=50):
    return rental_days * rental_rate
car_rental_total = car_rental(rental_days)
#print a message to the user with the car rental cost
print(f"The total cost of your car rental for {rental_days} days is: R{car_rental_total}")
# create a function to calculate the plane cost based on the city_flight input
def plane_cost(city_flight):
    if city_flight == "Cape Town":
        return 500
    elif city_flight == "Durban":
        return 600
    elif city_flight == "Port Elizabeth":
        return 700
    else:
        return 0  # Return 0 if the city is not recognized
plane_cost_total = plane_cost(city_flight)
#print a message to the user with the plane cost
if plane_cost_total > 0:
    print(f"The cost of your flight to {city_flight} is: R{plane_cost_total}")
# create a function to calculate the total cost of the trip
def holiday_cost(hotel_total, car_rental_total, plane_cost_total):
    return hotel_total_cost + car_rental_total + plane_cost_total
# calculate the total cost of the trip
total_cost = holiday_cost(hotel_total_cost, car_rental_total, plane_cost_total)
#print a message to the user with the total cost of the trip
print(f"The total cost of your trip to {city_flight} is: R{total_cost}")
print()
