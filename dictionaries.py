#dictionary = A changeable, unordered collection of unique key:value pairs
#             Fast because they use hashing, allow us to acces a value quickly

capitals= {'USA':'Washington DC',
           'Hungary':'Budapest',
           'China':'Beijing',
           'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China') #deleting the given value
capitals.clear() # clearing dictionary

#print(capitals['Russia'])

print(capitals.get('Germany')) # safer way to print
print(capitals.keys()) # prints only the keys
print(capitals.values()) #prints only the values
print(capitals.items()) #prints everything


for key,value in capitals.items():
    print(key,value)