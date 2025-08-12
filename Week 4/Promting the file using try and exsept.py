file_name= input('Enter the name of file:')
try:
    fhand = open(file_name)
except:
    print('File can not found', file_name)
    quit()
count = 0
for line in fhand:
    if line.startswith('I'):
        count = count + 1
print('There was', count, 'I character in', file_name)