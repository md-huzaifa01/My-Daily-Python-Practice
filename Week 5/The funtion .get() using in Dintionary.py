count = dict()
names = ['mehedi', 'salman', 'apil', 'mehedi', 'mamun', 'apil']
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count.get(name,0) + 1
print(count)