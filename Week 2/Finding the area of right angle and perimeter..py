# We know from the formula of Pythagoras that is: the area of right angle is, A=1/2 or 0.5(Base * Height)
# As like that the formula of perimeter for right angle is= a+b+c
import math
base=float(input("Enter the base of the right angle: "))
height=float(input("Enter the height of the right angle: "))
area=0.5*base*height
print("The area of the right angle is= %.2f" %area)
c=math.sqrt((base*base)+(height*height))
# According to Pythagoras formula c^2=a^2+b^2. By this we can find the other side of right angle.
# if we transfer the sqrt to other side of equal that will be something like this, c=sqrt(a^2+b^2)
print("The other side of right angle is= %.2f" %c)
perimeter=base+height+c
print("The perimeter of the right angle is= %.2f" %perimeter)