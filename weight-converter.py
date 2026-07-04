weight = float(input("Enter your weight: "))
unit = input("Enter your unit [K/L]: ")

if unit == "K":
    result = weight * 2.205
    unit = "Kgs"
    print(f"Your weight is {result} {unit}")
elif unit == "L":
    result = weight / 2.205
    unit = "Lbs"
    print(f"Your weight is {result} {unit}")
else :
    print("Invalid input")