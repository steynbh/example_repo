# Create a program that will read from the text file inventory.txt and perform the following on the data to prepare for presentation to your managers:

#2. Inside the file, you will find a class named Shoe with the following attributes: country, code, product, cost, quantity

# Inside this class define the following methods: 
    # get_cost – Returns the cost of the shoes.
    # get_quantity – Returns the quantity of the shoes.
    # __str__ – This method returns a string representation of a class instance in the following format: "Country: {country}, Code: {code}, Product: {product}, Cost: {cost}, Quantity: {quantity}"
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# Outside this class create a shoes_list variable with an empty list. This variable will be used to store a list of shoe objects
shoes_list = []

# define the following functions outside the class:
# read_shoes_data – This function will open the file inventory.txt and read the data from this file, then create a shoe object with this data and append this object to the shoe list. One line in this file represents data to create one object of shoes. You must use the try-except blocks in this function for error handling. Remember to skip the first line using your code.
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(',')
                shoes_list.append(Shoe(country, code, product, float(cost), int(quantity)))
    except FileNotFoundError:
        print("The file inventory.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# capture_shoes – This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object inside the shoe list.
def capture_shoes():
    try:
        country = input("Enter the country: ")
        code = input("Enter the code: ")
        product = input("Enter the product name: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))
        shoes_list.append(Shoe(country, code, product, cost, quantity))
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# view_all – This function will iterate over the shoe list and print the details of the shoes returned from the __str__ function.
def view_all():
    if not shoes_list:
        print("No shoes available.")
        return
    for shoe in shoes_list:
        print(shoe)

#re_stock – This function will find the shoe object with the lowest quantity, which are the shoes that need to be restocked. Ask the user if they want to add this quantity of shoes and then update it. This quantity should be updated on the file for this shoe.
def re_stock():
    if not shoes_list:
        print("No shoes available to restock.")
        return
    min_quantity_shoe = min(shoes_list, key=lambda shoe: shoe.get_quantity())
    print(f"Shoe with lowest quantity: {min_quantity_shoe}")
    try:
        additional_quantity = int(input("Enter the quantity to add for restocking: "))
        min_quantity_shoe.quantity += additional_quantity
        # Update the file
        with open('inventory.txt', 'w') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")  # Write header
            for shoe in shoes_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        print("Restock successful.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# search_shoe – This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
def search_shoe():
    if not shoes_list:
        print("No shoes available to search.")
        return
    code = input("Enter the shoe code to search: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")

# value_per_item – This function will calculate the total value for each item. Please keep the formula for value in mind; value = cost * quantity. Print this information on the console for all the shoes.
def value_per_item():
    if not shoes_list:
        print("No shoes available to calculate value.")
        return
    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Shoe: {shoe.product}, Value: {value}")

# highest_qty – Write code to determine the product with the highest quantity and print this shoe as being for sale.
def highest_qty():
    if not shoes_list:
        print("No shoes available to determine highest quantity.")
        return
    max_quantity_shoe = max(shoes_list, key=lambda shoe: shoe.get_quantity())
    print(f"This shoe is for sale: {max_quantity_shoe}")

# Now create a menu that executes each function above. This menu should be inside the while loop.
def main_menu():
    while True:
        print("\nShoe Inventory Management")
        print("1. Read Shoes Data")
        print("2. Capture Shoes")
        print("3. View All Shoes")
        print("4. Re-stock Shoes")
        print("5. Search Shoe by Code")
        print("6. Calculate Value per Item")
        print("7. Show Highest Quantity Shoe")
        print("8. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            read_shoes_data()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            view_all()
        elif choice == '4':
            re_stock()
        elif choice == '5':
            search_shoe()
        elif choice == '6':
            value_per_item()
        elif choice == '7':
            highest_qty()
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()


