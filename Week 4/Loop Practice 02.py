while True:
    user_input = input('You said :')
    if user_input == 'r':
        continue
    if user_input == 'stop':
        break
    print('You said:', user_input)