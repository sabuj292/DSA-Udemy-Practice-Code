
# finding out the summation of digits of 
# number that may be floating 
# or integer or positive or negative
def sum_of_digits_float(number):
    # Convert the floating-point number to a string
    number_str = str(number)
    
    # Initialize a variable to store the sum
    total_sum = 0
    
    # Iterate through the characters in the string
    for char in number_str:
        # Check if the character is a digit
        if char.isdigit():
            # Convert the character to an integer and add it to the sum
            total_sum += int(char)
    
    return total_sum

# Example usage:
float_number = input("Enter a number : ")

result = sum_of_digits_float(float_number)
print(result)  # This will print the sum of the digits, which is 21 for the example number 123.456

