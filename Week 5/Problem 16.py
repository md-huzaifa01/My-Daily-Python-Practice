# Calculate the multiplication and sum of two numbers.
# Given two integer numbers, write a Python program to return their product only if the product is equal to
# or lower than 1000. Otherwise, return their sum.
#Given 1: number1 = 20, number2 = 30, Expected Output: The result is 600
# Given 2: number1 = 40, number2 = 30, Expected Output: The result is 70
def multi_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
result = multi_or_sum(20,30)
print('The result is ', result)
result = multi_or_sum(40,30)
print('The result is ', result)