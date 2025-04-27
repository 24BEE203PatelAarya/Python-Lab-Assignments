#11.Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight 
#   line.    


x1 = int(input("Enter the coordinates for x1: "))
x2 = int(input("Enter the coordinates for x2: "))
x3 = int(input("Enter the coordinates for x3: "))
y1 = int(input("Enter the coordinates for y1: "))
y2 = int(input("Enter the coordinates for y2: "))
y3 = int(input("Enter the coordinates for y3: "))

det = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)

if det == 0 :
    print('The points are on same line')
else:
    print('The points are not on same line')

