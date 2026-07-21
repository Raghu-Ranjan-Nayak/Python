#Set methods in python
set1 = {4,}
set2 = {5,}

#Add elements in sets
set1.add(1)
set1.add(2)
set1.add(3)
print(set1)

set2.add(3)
set2.add(4)
set2.add(5)
print(set2)

#Removed elements from sets
set1.remove(2)
set2.remove(5)
print(set1)
print(set2)

#Pop element from set1
set1.pop()
print(set1)

#Union of set1 and set2
print(set1.union(set2))
print(set1.intersection(set2))

#Clear the sets
print(set1.clear())
print(set2.clear())




