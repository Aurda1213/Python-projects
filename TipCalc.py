print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What % tip would you like to give? %"))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay ${final_amount}")