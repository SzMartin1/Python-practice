# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped version of a variable can be created




name = "Martin" # ez egy globális változó

def disp_name():
    name="Szabó" # ez egy lokális változó, csak a függvényen belül elérhető
    print(name)

disp_name()
print(name)