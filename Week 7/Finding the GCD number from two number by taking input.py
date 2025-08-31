# Taking two numbers from the user and then deciding what the GCD is.
def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return x
num1= int(input('Enter the first number: '))
num2= int(input('Enter the second number: '))
print('The GCD of {0} and {1} is: '.format(num1,num2), end = '')

print(computeGCD(num1,num2))
