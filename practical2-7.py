#Check if year is leap year or not
angle1 = float(input("Enter the first angle of the triangle"))
angle2 = float(input("Enter the second angle of the triangle"))
angle3 = float(input("Enter the third angle of the triangle"))
if angle1>0 and angle2>0 and angle3>0 and (angle1 + angle2 + angle3) == 180:
    print("The triangle is valid")
else:
    print("The triangle is not valid")
     
 

