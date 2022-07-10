from email.errors import MultipartInvariantViolationDefect


print("Variables")
# variables = a container for a value. Behaves like the value that it contains.
#string datatype
first_name = "Martin"
last_name = "Szabó"
full_name = first_name +" "+last_name
print("Hello, my name is " +full_name)
#print(type(name))========> kiírja, hogy a változónk milyen változó.
#int datatype
age = 21
age += 1
print(age)
print(type(age))
# a "" jelek között lévő értékek stringek lesznek
print("My age is"+str(age))
# ahhoz hogy az int tipusu értéket hozzáfűzzük ahhoz amit írtunk, castolni kell stringgé
# float datatype
height = 173.54
print(height)
print(type(height))
print("My height is"+str(height))
# ahhoz hogy az float tipusu értéket hozzáfűzzük ahhoz amit írtunk, castolni kell stringgé
#boolean datatype
human = True
print (human)
print(type(human))
print("Am i a human?"+str(human))
# ahhoz hogy az int tipusu értéket hozzáfűzzük ahhoz amit írtunk, castolni kell stringgé