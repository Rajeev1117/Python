#unordered, unchangable, unindexed

set = {"a","b","c","d"}
print(set)

#if we check items are present in set or not
print("a" in set)

#add an item in a set
set.add("e")
print(set)

#remove an item in the set
set.remove("e")
print(set)

#loop through the set
for x in set:
    print(x)

#add two set by using union method
set1 = {"e","f"}
set2 = set.union(set1)
print(set2)

#add two set by using update() method
set.update(set1)
print(set)

