import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py <number1> <number2>")
else:
    # Convert command line arguments to floats
    number1 = float(sys.argv[1])
    number2 = float(sys.argv[2])
    
    # Calculate the product
    product = number1 * number2
    
    # Print the result
    print(f"The product of {number1} and {number2} is: {product}")
