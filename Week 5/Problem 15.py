fhand = open("romeo.txt")
count = dict()
for line in fhand:
    words = line.strip()
    for word in words:
        count[word] = count.get(word, 0) + 1
lst = list()
for key,val in count.items():
    lst.append((key, val))
lst = sorted(lst,reverse=True)
for key, val in lst[10:]:
    print(key, val)
# Short way
print(sorted([(key, val) for key, val in count.items() ]))
