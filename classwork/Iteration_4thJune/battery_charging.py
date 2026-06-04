#Program for displaying battery charging status
charging_level = 20 #initial charging level is 20%
electricity_status = input("Is the electricity available? (yes/no):")  # to check if there is electricity or not?
if(electricity_status.lower()!="yes"):
    exit("Electricity is not available. Cannot charge the battery.")
while(charging_level<100):
    print("Battery is charging level:", charging_level, "%")
    charging_level+=10
print("Battery is fully charged")     #displaying all the battery level
