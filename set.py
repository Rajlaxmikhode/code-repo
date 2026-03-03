collection={2,4.9,51,False,"hello",11}
my_list=list(collection)
print("Accessing set elements by converting it to list:",my_list[2])
'''
Sets are mutable and unordered. 
Since they do not maintain order, you cannot access elements using indexing.
However, you can iterate through them using a loop.
If indexing is required, you must convert the set into a list.
'''

collection2={}#Empty dictionary
collection3=set()#This creates a  set
collection4={2,8,"sharavari",True} 
print(collection)
print(type(collection2))#This will return dict because {} is used to create a dictionary in python 
print(type(collection3))#This will return set because set() is used to create a set in python

#set methods
collection3.add(10)
collection3.add(False)
collection3.add("manav")
collection3.add(4.9)
print(collection.union(collection3))#merges both sets and removes duplicates
print(collection.intersection(collection3))#Prints the common values in both sets
print(collection.difference(collection3))#Prints the values that are not in common in both sets
print(collection.isdisjoint(collection4))#Returns true if there are no common values in both sets
print(collection3.issubset(collection))#Returns True value if collection 3 has value present in collection
print(collection.issuperset(collection3))#Returns True value if collection has value present in collection 3
collection3.update(collection4) #This will add elements of collection 4 to collection 3,unlike  union() it does not return new set
print(collection3)

# update() adds elements of collection4 into collection3 (modifies in place)
# Unlike union(), it does not return a new set.
# Sets automatically remove duplicates.