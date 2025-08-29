row = int(input('Please Enter the for row: '))
number = 1
print('The final floyd triangle is : ')
for i in range(1, row + 1):
    for j in range(1, i+1):
        print(number, end = ' ')
        number = number + 1
    print()