bill = float(input("What was the total bill? "))
percentage = int(input("What percentage of tip would you like to give? 10, 12 or 15 = "))
split = int(input("How many parts should the bill split? "))

tip = bill*(percentage/100)

total = bill + tip

amountPer = total/split
finalAmountPerPerson = "{:.2f}".format(round(amountPer,2))
print(f"Each person should pay: {finalAmountPerPerson}")