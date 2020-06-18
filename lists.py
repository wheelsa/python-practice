# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1,2,3,4,5]

#using a constructor
numbers = list((1,2,3,4,5))
print(type(numbers))


fruits = ["Apple", "Oranges", "Grapes", "Pears", 12]

print(fruits[2])

#Get len
print(len(fruits))

fruits.append('Mangos')

#remove from list
fruits.remove('Grapes')


fruits.insert(2, 'Strawberries')
print(fruits)

#Remove from position
fruits.pop(3)
print(fruits)

fruits.reverse()
print(fruits)

fruits.remove(12)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)
