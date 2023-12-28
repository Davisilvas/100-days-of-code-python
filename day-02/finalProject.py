print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_to_split = int(input("How many people to split the bill? "))

tip = total_bill * percentage / 100
amount_per_person = (total_bill + tip) / people_to_split

# Another way to calculate the bill with the tip
# (percentage / 100 * total_bill + total_bill) / people_to_split
# amount_per_person = (percentage / 100 * total_bill + total_bill) / people_to_split

print(f"Each person should pay: ${amount_per_person:.2f}")
