#type casting = convert the darta type of a value to another type

x = 1   #int
y = 2.0 #float
z = "3" #string

y=int(y)   # permanent change
z = int(z) # permanent change
x = float(1)

print(x)
print(y) #not permanent change
print(z*4)

# typecasters: str(), int(), float() etc..

print("X is "+str(x))
print("Y is ",+ str(y))
print("Z is ", +str(z))

# csak akkor konkatenálhatjuk az x, y, és z változókat printen belül, ha stringgé castoljuk őket
