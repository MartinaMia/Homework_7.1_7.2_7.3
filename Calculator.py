first_number = int(input("Choose your first number"))    # input("Choose your first number")     # int(1)

second_number = int(input("Choose your second number"))   # input("Choose your second number")   # int(2)

operator = input("Choose an operator")        # input("Choose an operator")   # operators might be "+", "-", "*" or "/"

if operator == "+":
    print(first_number + second_number)

elif operator == "-":
    print(first_number - second_number)

elif operator == "*":
    print(first_number * second_number)

elif operator == "/":
    print(first_number / second_number)

else:
    print("Error - choose a right operator")




