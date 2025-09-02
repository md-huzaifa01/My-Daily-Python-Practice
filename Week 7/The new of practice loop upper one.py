n= int(input('Enter the value of n:'))
numbers= list(map(int, input(f'Enter {n} numbers seperated by space: ').split()))
if len(numbers) != n:
    print('You did not enter exactly', n, 'numbers')
else:
    print('The average value is :', sum(numbers)/n)