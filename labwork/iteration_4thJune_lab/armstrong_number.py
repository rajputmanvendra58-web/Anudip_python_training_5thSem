#Program to check if the number is Armstrong number
#accepting the number from the user
num=int(input("Enter any number:")) 
#storing the original number for comparison later
temp=num
#to find the total number of digits
digits=len(str(num))
sum=0
while temp>0: #process each digit
    digit=temp%10 #for last digit
    sum=sum+(digit**digits)
    temp=temp//10 #remove the last digit of the number
    #now check the sum is equal to the original number
if sum==num:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")