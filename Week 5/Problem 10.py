# Problem 10
# Given mbox-short.txt
# Read a file
# Count how many lines there are
# Count total characters in all lines
# Compute the average length
fhand = input('Enter the file name:')
read= open(fhand)
total_char = 0
total_word = 0
for line in read:
    line = line.split()
    if line == "":
        continue
    words = line.split()
    for word in words:
        total_char += len(word)
        total_word += 1
if total-word > 0:
    average = len(word)
    print('The average is: ', average)
else:
    print('No word found!!')