print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as = tip // 100
total_bill = bill + bill * tip_as
bill_pp = tip % 100
tip = bill * tip / 100
print(float(total = tip + bill))


