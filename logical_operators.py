#logical operators (and,or,not) are used to check if two or more conditional statements are true 
temperature=int(input("What is the temperature outside?: "))


# AND és OR
#if temperature >= 0 and temperature <=30:
 #   print("The weather is great outside.")
  #  print("Go outside and have fun!")
#elif temperature <= 0 or temperature > 30:
 #   print("The weather is bad today.")
  #  print("You shall stay inside my lad!")

#NOT logical operator example
#a NOT logikai operátor a true értéket false-ra állítja, a false értéket pedig true-ra

if not(temperature>=0 and temperature<=30):
    print("The weather is bad today!")
    print("You shall stay inside my lad!")
elif not (temperature <= 0 or temperature > 30):
    print("The weather is great today!")
    print("Go outside and have fun!")