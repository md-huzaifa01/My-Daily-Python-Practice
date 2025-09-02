n = int(input('Enter the value of n:'))
print(f'Enter {n} numbers:')
numbers= []
for _ in range(n):
    numbers.append(int(input()))
avg = sum(numbers)/n
print('The average value is ', avg)