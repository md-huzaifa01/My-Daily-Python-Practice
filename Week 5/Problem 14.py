name = input('Enter the name of file: ')
fread = open(name)
count = dict()
for line in fread:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
bigcount = None
bigword = None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword  = word
print(word, count)
