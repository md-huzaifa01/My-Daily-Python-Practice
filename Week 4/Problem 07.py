# Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of
# those values and produce an output as shown below. Do not use the sum() function
# or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name
fhand = input("Enter the file name: ")
try:
    fread = open(fhand)
except:
    print("Invalid file name")
    quit()
count = 0
total = 0.0
for line in fread:
    if line.startswith('X-DSPAM-Confidence:'):
        colon = line.find(':')
        num = line[colon + 1:].strip()
        numflt= float(num)
        count += 1
        total += numflt
if count > 0:
    average  = total/count
    print('The average is', average)
else:
    print('No line found')