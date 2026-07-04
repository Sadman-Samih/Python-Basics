oparators = input("Enter an oparator (+, -, *, /): ")

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

if oparators == "+":
    result = num1 + num2
    print(f"the result is {result}")
elif oparators == "-":
    result = num1 - num2
    print(f"the result is {result}")
elif oparators == "*":
    result = num1 * num2
    print(f"the result is {result}")
elif oparators == "/":
    result = num1 / num2
    print(f"the result is {result}")
else:
    print("Invalid input")