# Find Maximum Number in File
# File contains lines like:
# makefile
#       Value: 5
#       Value: 12
#       Value: 7
# Find the largest number and print it.
fhand=input('Enter the name of file: ')
try:
    fread= open(fhand)
except:
    print('Invalid file name!')
    quit()
num = None
for line in fread:
    if line.startswith('Value:'):
        colon = line.find(":")
        fnum= line[colon + 1:].strip()
        fnumflt= float(fnum)
        if num is None or num < fnumflt:
            num = fnumflt
print('largest number is: ', num)