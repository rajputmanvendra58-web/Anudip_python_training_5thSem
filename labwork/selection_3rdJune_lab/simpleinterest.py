#wap to calculate simple interest
p=float(input("enter priciple amount:")) #principle amount
if p<0:
    exit("the amount must be positive")
r=float(input("enter the rate of interest:")) #rate of interest
if r<0:
    exit("the interest must be positive")
t=float(input("enter time (in years):"))   #time in years
if t<0:
    exit("the time must be positive")
else:
    #to display simple interest
    print("Simple interest= ",(p*r*t)/100)
