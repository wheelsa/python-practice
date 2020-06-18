# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
fruitTuple = ('apple', 'orange', 'mango')
print(fruitTuple[1])

# cant change
# fruitTuple[1] = "grape"

# fruitTuple[2] = "bread"

# triples with one value should have trailing comma,

fruitTuple2 = ('apple')
print(fruitTuple2)

fruitTuple2 = ('apple',)
print(fruitTuple2)

# delet tuple
del fruitTuple

# A Set is a collection which is unordered and unindexed. No duplicate members.
fruitSet = {"Apple", "Orange", "Mango"} # no duplicate members
print(fruitSet)
print("Apple" in fruitSet)

#add to set
fruitSet.add("Grape")
print(fruitSet)

fruitSet.remove('Grape')

print(fruitSet)

fruitSet.clear

print(fruitSet)

del fruitSet
