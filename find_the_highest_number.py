
# Input variables 
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))
num4 = float(input("Input fourth number: "))
num5 = float(input("Input fifth number: "))

# Compare  variables to each other
def find_the_highest_number(num1,num2,num3,num4,num5):
    highest=num1 # initial highest

    if num2>highest:
        highest=num2
    else: 
        highest=num1

    if num3>highest:
        highest=num3
    else:
        highest=num2

    if num4>highest:
        highest=num4
    else:
        highest=num3

    if num5>highest:
        highest=num5
    else: 
        highest=num4
        
    return highest

# To call the function we used
highest_number = find_the_highest_number(num1,num2,num3,num4,num5)

# To print the highest number
print(f"The highest number is: {highest_number}")
