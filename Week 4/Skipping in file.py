# In hare you have to a file in the same directory where your programme are running.
fhand = open('data.txt')
for line in fhand:
    line= line.strip()
    if not 'to' in line:
        continue
    print(line)
