#list = used to store multiple items within a single variable

food =["pizza","hamburger","hotdog","spaghetti","Wienerschnitzel","pudding"]

food[0]="sushi"

#print(food[0])

for x in food:
    print(x)

#useful functions of lists

food.append("ice cream") # hozzáad egy elemet a listához
food.remove("hotdog") # kitörli az adott elemet a listából
food.pop() #kitörli az utolsó elemet
food.insert(0,"cake") #beszurhatunk egy elemet az adott indexbe
food.sort() #sorrendbe rakja az elemeket
food.clear() # kitörli az össszes elemet a listából.
