lst = dict()
lst['mamun'] = 43
lst['laila'] = 34
lst['salman'] = 43
for name,age in lst.items():
    print(name, age)
tup = lst.items()
print(tup)
sorted(tup)
print(tup)