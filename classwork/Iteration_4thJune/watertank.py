#Program for water tank filling
water_level=0   #initial water level is 0
while(water_level<100): #the tank will fill upto 100 litres
    water_level+=10
    print("Water is filling..Current water level: ",water_level,"Litres")
print("Water tank is Full.")