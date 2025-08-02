# Formula of Diameter in a circle= 2 * radius
# Formula of circumference in a circle= 2 * math.pi * radius
# Formula of area of circle= math.pi * radius * radius
import math
radius = float(input("Enter the radius of the circle: "))
diameter = 2* radius
circumference= 2*math.pi*radius
area = math.pi*radius*radius
print("The area of the circle is: ", math.pi,"*", radius,"*",radius,"=", area)
print("The diameter of the circle is: ", 2,"*", radius,"=", diameter)
print("The circumference of the circle is: ", 2,"*", math.pi,"*", radius, "=", circumference)