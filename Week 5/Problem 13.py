count = dict()
line = input("Enter a line of text: ")
words = line.split()
print('\nThe Words is ', words)
print('Counting')
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)
