num = int(input("Choose a number between 1 to 10. "))

if num<5:
    print("Number is in the lower half")
else:
    print("Number is in the upper half")


# Leap year calculation
year = int(input("Give us an year. "))

if year%400 == 0:
    print("Leap year")
elif year%4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
