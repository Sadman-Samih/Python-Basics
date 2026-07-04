weight = float(input("Enter your weight: "))
unit = input("Enter your unit [K/L]: ")

if unit == "K":
    result = weight / 100
    print(f"Your weight is {result}")
elif unit == "L":
    result = weight / 1000
    print(f"Your weight is {result}")