num = None
print('Before')
for value in [9,41,12,3,74,15]:
    if num is None or num > value:  # In hare it is now execute the smallest number
        # If you want to execute the largest number just chane arrow sign
        num = value
    print(num, value)
print('After', num)