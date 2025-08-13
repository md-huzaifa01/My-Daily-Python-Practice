# Problem 9 – Count Specific Email Senders
# Given mbox-short.txt
# Count how many times each email appears in lines starting with "From ".
# Print the counts.
fhand = input('Enter the name of file:')
fread = open(fhand)
count = 0
for line in fread:
    if line.startswith('From:'):
        count += 1

print(count)
