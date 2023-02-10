# Printing the sum of digits of a number input as a string

num = input("Enter the number = ")
n = int(num)
i = 0
res = 0
while n> 0:
    res += n % 10
    n = int(n / 10);

print(f"Result is {res}")
