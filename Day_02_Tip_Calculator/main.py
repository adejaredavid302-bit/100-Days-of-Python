print("Welcome to the tip calculator!")
total_bill=float(input(f"What was the total bill? "))
tip=float(input("How much tip would you like to give?10,12,or 15? "))
number_of_people=int(input("How many people would split the bill? "))
calculations=((tip/100 *total_bill)+total_bill)/number_of_people
print(f"Each person should pay ${calculations:.2f}")