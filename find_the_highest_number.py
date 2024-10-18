
# Input variables 
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))
num4 = float(input("Input fourth number: "))
num5 = float(input("Input fifth number: "))

# Initial highest number
highest = num1

# Compare  variables to each other
if num2>highest:
    highest = num2
elif num3>highest:
    highest = num3
elif num4>highest:
    highest = num4
elif num5>highest:
    highest = num5
    
# Print what variable is the highest number
print(f"The highest number is: {highest}")
