# set = collection whic is unordered, unindexed. No duplicate values
#       faster than a list



utensils= {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

#utensils.update(dishes)

#dinner_table=utensils.union(dishes)

#for x in dinner_table:
 #   print(x)

print(utensils.difference(dishes))

print(utensils.intersection(dishes))