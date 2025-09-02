print('Enter the value of n: ', end='')
n= int(input())
print('Enter ' +str(n)+ 'numbers:')
numbers   = []
for i in range(n):
    numbers.insert(i, int(input()))
sum= 0
for i in range(n):
    sum = sum+ numbers[i]
avg = sum/n
print('\nThe average value is: ', avg)
