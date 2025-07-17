num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
bigger= num1
if (num2>bigger):
    bigger=num2
if (num3>bigger):
    bigger=num3
print("The max number is", bigger)