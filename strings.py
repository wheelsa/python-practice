# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


# String Formatting

# String Methods


name = "Brad"
age = 37
print("Hello " + name + str(age))

# string formatting

# Arguments by position

print('{}, {}, {}'.format('a','b','c'))

print('{1}, {2}, {0}'.format('a','b','c'))

# Arguments by name

print('My name is {name} and I am {age}'.format(name=name, age=age))

# F strings (only in 3.6+)
print(f'My name is {name} and I am {age}')

# string methods

s = "Hello there world"
 
 # Capitalize first letter
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())

print(len(s))

#Replace
print(s.replace('world', 'everyone'))

sub = "H"

print(s.count(sub))




