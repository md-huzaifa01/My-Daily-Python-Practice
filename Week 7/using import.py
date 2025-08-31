# In Hare, I had done it by taking input, not using import().
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.strip()
    if re.search('From: ', line):

        print(line)
