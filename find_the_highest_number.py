
# Input variables 
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))
num4 = float(input("Input fourth number: "))
num5 = float(input("Input fifth number: "))

# Compare  variables to each other
def find_the_highest_number(num1,num2,num3,num4,num5):
    if num1>num2 and num1>num3 and num1>num4 and num1>num5:
        print("The first number is the highest number!!!")
        return num1
    elif num2>num1 and num2>num3 and num2>num4 and num2>num5:
        print("The second number is the highest number!!!")
        return num2
    elif num3>num1 and num3>num2 and num3>num4 and num3>num5:
        print("The third number is the highest number!!!")
        return num3
    elif num4>num1 and num4>num2 and num4>num3 and num4>num5:
        print("The fourth number is the highest number!!!")
        return num4
    else:
        print("The fifth number is the highest number!!!")
    

# Print what variable is the highest number
find_the_highest_number(num1,num2,num3,num4,num5)
