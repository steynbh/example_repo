import math
# provide the user with a menu of options either investment calculator or loan calculator
print("Welcome to the Finance Calculator!") 
print("Please choose an option:")
print("1. Investment Calculator - calculate the amount of interest you will earn from an investment")
print("2. Bond Calculator - calculate the amount you will have to pay on a home loan")
choice = input("Enter either investment or bond:")
# if the user types investment, Investment or INVESTMENT, run the investment calculator
if choice.lower() == "investment":
    # ask user to input the principal amount, interest rate, number of years, and compounding frequency
    principal = float(input("Please enter the principal amount (in Rands): "))
    interest_rate = float(input("Please enter the annual interest rate (as a percentage): ")) / 100
    years = int(input("Please enter the number of years: "))
    # ask the user if they want simple or compound interest 
    interest = input("Do you want simple or compound interest? (Enter 'simple' or 'compound'): ").lower()
    # if the user chooses simple interest, calculate the total amount after interest using the formula A = P(1 + rt)
    if interest == "simple":
        total_amount = principal * (1 + interest_rate * years)
        total_interest = total_amount - principal
        print(f"Total amount after {years} years: R{total_amount:.2f}")
        print(f"Total interest earned: R{total_interest:.2f}")

    # else if user chooses compound interest calculate the total amount after interest using the formula A = P(1 + r/n)^(nt)
    elif interest == "compound":
        compounding_frequency = int(input("Please enter the number of times interest is compounded per year (e.g., 1 for annually, 4 for quarterly, 12 for monthly): "))
        # calculate the total amount after interest
    total_amount = principal * (1 + interest_rate / compounding_frequency) ** (compounding_frequency * years)
    
    # calculate the total interest earned
    total_interest = total_amount - principal
    
    print(f"Total amount after {years} years: R{total_amount:.2f}")
    print(f"Total interest earned: R{total_interest:.2f}")
    
    # if the user enters anything else, print an error message
    
    
# else if the user types bond or Bond or BOND run the bond calculator
elif choice.lower() == "bond":
    # ask user to input the present value of the house, annual interest rate, and number of months
    present_value = float(input("Please enter the present value of the house (in Rands): "))
    annual_interest_rate = float(input("Please enter the annual interest rate (as a percentage): ")) / 100
    months = int(input("Please enter the number of months to repay the bond: "))
    
    # calculate the monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12
    
    # calculate the monthly repayment using the formula M = P[r(1 + r)^n] / [(1 + r)^n – 1]
    monthly_repayment = (present_value * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / \
                        ((1 + monthly_interest_rate) ** months - 1)
    
    print(f"Monthly repayment for the bond: R{monthly_repayment:.2f}")
# if the user types anything else, print an error message
else:
    print("Invalid choice. Please enter either 'investment' or 'bond'.")
