# The formula of area for sphere, A= 4*math.pi*r*r or r^2
# The formula of volume for sphere, V= 4/3 8 math.pi*r*r*r or r^3
import math
radius=float(input("Enter the radius of the sphere: "))
area=4*math.pi*pow(radius,2) # The is another way to do it----radius*radius
print("The area of the sphere is = %.2f" %area)
volume=4/3*math.pi*pow(radius,3)  # Another way to write it---radius*radius*radius
print("The volume of the sphere is =%.2f" %volume)