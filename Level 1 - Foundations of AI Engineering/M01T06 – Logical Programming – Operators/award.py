# ask user to input their triathlon time in minutes for each of the three events
swim_time = int(input("Please enter your swim time in minutes: "))
cycle_time = int(input("Please enter your cycle time in minutes: "))
run_time = int(input("Please enter your run time in minutes: "))
# calculate the total time taken for the triathlon
total_time = swim_time + cycle_time + run_time
# if the total time is less than or equal to 100 minutes, print award: provintial colours 
if total_time <= 100:
    print("Award: Provincial Colours")
# else if the total time is equal to or more than 101 minutes or equal to or less than 105 minutes, print award: provincial half colours
elif 101 <= total_time <= 105:
    print("Award: Provincial Half Colours")
# else if the total time is equal to or more than 106 minutes or equal to or less than 110 minutes, print award: provincial scroll
elif 106 <= total_time <= 110:
    print("Award: Provincial Scroll")
# else the total time is more than 111 minutes, print award: no award
else:
    print("Award: No Award")
