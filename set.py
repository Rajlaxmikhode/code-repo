collection={2,4.9,1,False,"hello",1}
collection2={}
collection3=set()
collection4={2,8,"sharavari",True} #this will create an empty set in python
print(collection)
print(type(collection2))#this will return dict because {} is used to create a dictionary in python 
print(type(collection3))#this will return set because set() is used to create a set in python

#set methods
collection3.add(10)
collection3.add(False)
collection3.add("manav")
collection3.add(4.9)
print(collection.union(collection3))#merges both sets and removes duplicates
print(collection.intersection(collection3))#prints the common values in both sets
print(collection.difference(collection3))#prints the values that are not in common in both sets
print(collection.isdisjoint(collection4))#returns true if there are no common values in both sets
print(collection3.issubset(collection))#returns True value if collection 3 has value present in collection
print(collection.issuperset(collection3))#returns True value if collection has value present in collection 3
print(collection3.update(collection4))#this will ad values of collection 4 to collection 3 not similar to union as it adds duplicates as well
