#program to check three angles form a triangle or not
angle1 = float(input("Enter the first angle:"))
#validate angle1
if(angle1<=0):
    exit("the angle must be positive")
angle2 = float(input("Enter the Second angle:"))
#validate angle2
if(angle2<=0):
    exit("the angle must be positive")
angle3 = float(input("Enter the Third angle:"))
#validate angle3
if(angle3<=0):
    exit("the angle must be positive")
#verifying triangle formation
if (angle1+angle2+angle3==180):
   #triangle is formed
   #acute angled triangle
   if(angle1<90 and angle2<90 and angle3<90):
    print("Above angles form acute angled triangle")
    #right angled triangle
elif(angle1==90 or angle2==90 or angle3==90):
        print("Above angles form Right angled triangle")
    #obtuse angled triangle
else:
    print("Above angles form obtuse angled triangle")
