#10. Given the length and breadth of a rectangle, write a program to find whether the area of the 
#    rectangle is greater than its perimeter.    

length = int(input("Enter leangth of the rectangle: "))
breadth = int(input("Enter breadth of the rectangle: "))
             
area = length*length
perimeter = 2*length + 2*breadth

if(area>perimeter):
             print("The area is greater than perimeter and area is: ",area)
else:
    print("The perimeter is greater than area and perimeter is: ",perimeter)

