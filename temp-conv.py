unit = str(input("Is the unit C or F? : "))
temp = float(input("What is the temperature? : "))

if unit == "C" :
    result = (temp * 9 / 5) + 32
    print(f"The temperature is {result} C")
elif unit == "F" :
    result = (temp - 32) * 5 / 9
    print(f"The temperature is {result} F")
else:
    print("Invalid input")