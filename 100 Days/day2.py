print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? \n")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_Of_People = input("How many people to split the bill? ")

percentage_calc = ((int(tip_percentage) / 100) * float(total_bill)) + float(total_bill)
calculation = percentage_calc / int(num_Of_People)

print(f"Each person has to  pay: ${round(calculation, 2)}")




