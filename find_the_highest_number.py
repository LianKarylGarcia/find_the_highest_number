
# Input variables 
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))
num4 = float(input("Input fourth number: "))
num5 = float(input("Input fifth number: "))

# Initial highest number
highest = num1

# Compare  variables to each other
def find_the_highest_number(num1,num2,num3,num4,num5):
    if num2>highest:
        print("The second number is the highest number!!!")
        return num2
    elif num3>highest:
        print("The third number is the highest number!!!")
        return num3
    elif num4>highest:
        print("The fourth number is the highest number!!!")
        return num4
    elif num5>highest:
        print("The fifth number is the highest number!!!")
        return num5
    else: 
        print("The first number is the highest number!!!")
    

# Print what variable is the highest number
find_the_highest_number(num1,num2,num3,num4,num5)
