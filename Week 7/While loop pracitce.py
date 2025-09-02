# Taking so much input and then finding the summation using while loop.
print('Enter the value of n: ', end='')
n= int(input())
print('Enter ' +str(n)+ 'numbers:')
numbers   = []
i = 0
while i<n:
    numbers.insert(i, int(input()))
    i = i+ 1
sum= 0
while i<n:
    sum = sum+ numbers[i]
    i= i+1
avg = sum/n
print('\nThe average value is: ', avg)


