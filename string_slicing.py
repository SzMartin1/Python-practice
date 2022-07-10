#slicing = create a substring by extracting elements from another string
#          indexing[]           or slice()
#          [start:stop:step]

name= "Szabó Martin"

first_name= name[0:5] # vagy name[:5]
last_name = name[6:12] # vagy name[6:]
funky_name = name[0:12:4] # vagy name[::4]
reversed_name = name[::-1] #string visszafele

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "http://google.com" #minden karakternek vagy egy pozitív és egy negatív indexe
website2 = "http://wikipedia.com"

slice=slice(7,-4,) #a negatív index a végéről kezdi, és -1 -el kezdődik

print(website[slice])
print(website2[slice])