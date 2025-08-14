list3 = ['Our', 'computers', 'are', 'fast', 'and', 'have', 'vasts', 'amounts', 'of', 'memory', 'and', 'could',
         'be', 'very', 'helpful', 'to', 'us', 'if', 'we', 'only', 'knew', 'the', 'language', 'to']
targ = input('Enter the word: ')
for w in list3:
    check = (w == targ)
    print(w,'-----',check)
