num = int(input('Enter any number: '))
sum = 0
for i in range(1,num):
    if(num % i == 0):
        sum = sum + i
if (sum == num):
    print('Entered number is a perfect number!')
else:
    print('Entered number is not perfect number!')