# create a list called menu that has four items on the menu
menu = ["coffee", "tea", "milo", "water"]
# create a dictionary called stock that shows the stock of each item
stock = {"coffee": 10, "tea": 10, "milo": 10, "water": 10}
# create a dictionary called price that shows the price of each item
price = {"coffee": 2.50, "tea": 1.50, "milo": 3.00, "water": 1.00}
# calculate the value of the total stock
total_stock = sum(stock[item] * price[item] for item in menu)
# print the total stock value
print("Total stock value: R", total_stock)