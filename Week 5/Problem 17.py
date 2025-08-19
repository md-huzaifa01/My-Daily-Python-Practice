# Write Python code to iterate through the first 10 numbers and, in each iteration,
# print the sum of the current and previous number.
print('Printing current and previous number and their sum in a range(10)')
previous_number = 0

# Looping the things from 1
for i in range(0,11):
    x_sum= previous_number + i
    print('Current Number: ', i , 'Previous Number: ', previous_number, 'and the sum is: ', x_sum)
    # modify the previous number and set in to the current number.
    previous_number = i