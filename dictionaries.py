# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
person = {
  'firstName': "John",
  "lastName" : "Doe",
  "age" : 30
}
print(person)
print(person['firstName'])

print(person.get('lastName'))
person['phone'] = '555-675-0987'

print(person.keys())

print(person.items())

person2 = person.copy()

person2['City'] = 'Boston'
print(person2)

del(person['age'])

print(person) 
person.pop('phone')

print(person)

print(len(person2))

# List of dictionaries
peopleNew = [
  {'name' : 'martha', 'age': 40},
 {'name' : 'Bob', 'age': 21},
 ]

print(peopleNew)