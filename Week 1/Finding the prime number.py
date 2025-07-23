num=int(input("Enter a number: "))
flag= False # Flag is a variable which are mainly use for bolian like true or false

if num > 1: # A prime number of course bigger then 1
    for i in range(2,num):
        if (num % i) == 0:
            flag = True

    if flag: # when the condition is true that means the number user type that was not prime because it dividable.
        print("The number is not prime.")
    else:
        print("The number is prime.")
else:
    print("The number is not prime.") # if the number is less then 1.