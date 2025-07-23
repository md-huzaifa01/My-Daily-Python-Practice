dis_ft=float(input("Enter the distance in feet: "))
dis_inches= dis_ft/12 # The relationship between feet and inches is (1 feet= 12 inches)
dis_yards=dis_ft/ 3 # The relationship between feet and yards is (1 yards = 36 inches or 3 feet)
dis_mile=dis_ft/5280 # The relationship between feet and miles is ( 1 mile = 5280 yards or 15840 feet or 190080 inches)
print("The distance in inches is: %.4f inches" %dis_inches) # In here, % means that I want to insert a thing
# this % is located, and f means it will show a float number, and .4 means it will show 4 float points after the dot.
print("The distance in yards is: %.4f yards" %dis_yards)
print("The distance in miles is: %.4f miles" %dis_mile)
