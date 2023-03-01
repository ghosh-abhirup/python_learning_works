c = "start"
p=float(0)
while True:
    if c =="start":
        first_num = float(input("What's your first number? "))
    else:
        first_num = p

    print("+\n")
    print("-\n")
    print("*\n")
    print("/\n")
    choice = input("Please choose an operation: ")
    second_num = float(input("What's your second number? "))

    if choice == "+":
        result = first_num + second_num

    elif choice == "-":
        result = first_num - second_num

    elif choice == "*":
        result = first_num * second_num

    else:
        result = first_num / second_num

    print(f"{first_num} {choice} {second_num} = {result}")

    cont = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation ")

    if cont == 'y':
        p = result
        c = "continue"
    else:
        print("/////////////////////////////////////////////////////")
        c="start"
