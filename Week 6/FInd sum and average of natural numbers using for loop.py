num= int(input('Enter any number: '))
total=0
for value in range(1, num + 1):
    total = total + value
average = total/num
print('Summation of natural numbers from 1 to {0} = {1}'.format(num,total))
print('Average of natural numbers form 1 to {0} = {1}'.format(num,average))