print("Welcome to the Tip Calculator")
bill=float(input("What was the total bill?"))
tip=float(input ("How much tip would you like to give? 10, 12, or 15?"))
people=float(input ("How many people to split the bill? "))
bill_one= bill + tip
bill_final=bill_one / people
bill_final_rounded= round(bill_final, 2)
print(f"Each person should pay: {bill_final_rounded}")
