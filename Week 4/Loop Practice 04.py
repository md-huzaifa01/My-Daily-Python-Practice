# Q4: Print all the odd numbers between 1 and 30 (inclusive) using a for loop.
for num in range(1,31):
    if num % 2 == 0:
        continue
    else:
        print(num)