numlist = list()
while True:
    inp = input('Enter the number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
if numlist:
    average = sum(numlist)/len(numlist)
    print(average)
else:
    print('Invalid input!!')
    quit()
