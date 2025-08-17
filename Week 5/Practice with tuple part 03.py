x = {'laila': 32, 'Mamun':28, 'Salman': 33}
t= list()
for name,age in x.items():
    t.append((name,age))
print(t)
t = sorted(t, reverse= True)
print(t)
t = sorted(t, reverse= False)
print(t)
