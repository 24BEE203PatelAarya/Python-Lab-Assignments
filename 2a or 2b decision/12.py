#12. Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies 
#   inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) ) 
    
import math

x = float(input("Enter x-coordinate of the point: "))
y = float(input("Enter y-coordinate of the point: ")) 
cx =  float(input("Enter x-coordinate of the circle's centre: "))
cy =  float(input("Enter y-coordinate of the circle's centre: "))
r =  float(input("Enter radius of the circle: "))

distance = math.sqrt(pow(x-cx,2) + pow(y-cy,2))

if distance < r:
    print("The point is inside the circle") 
elif distance == r:
        print("The point is on the circle")
else:
        print("The point is outside the circle")
