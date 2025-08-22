import math
n = int(input('Enter the number of terms: '))
sum = 1
for i in range(1, n+1):
    sum = sum+ (1/math.factorial(i))
print('The summation of series is: ', round(sum,2))