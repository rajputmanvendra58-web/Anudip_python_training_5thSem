print("------Triangle--------")
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
#find parameter
perimeter = a + b + c
#find semi parameter for area
s = perimeter / 2
#display area and parameter
print("first side ",a ," second side ",b ,"third side ",c )
print("Perimeter of triangle =", perimeter)
print("Area of triangle =",(s * (s - a) * (s - b) * (s - c))**0.5)
