words = ['nice', 'look', 'fine', 'nice', 'many']
us = input('Enter the replace word: ')
for word in range(len(words)):
    if words[word] == 'nice':
        words[word] = us
print(word)