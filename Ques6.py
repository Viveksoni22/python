import math
def Cal_sqrt_and_squre(number):
    square = number**2
    square_root = math.sqrt(number)
    return square ,square_root

number = float(input("Enter the number :"))
square ,square_root =  Cal_sqrt_and_squre(number)

print(f"The square of {number} is: {square}")
print(f"The square root of {number} is: {square_root}")