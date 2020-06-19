# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

if x == y: 
    print(f'{x} is equal to {y}')

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

if x > 2 and x <= 10:
    print(f'{x} is less then 2 and greater then 10')

if not(x == y):
    print(f'{x} is not equal to {y}')
# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values



# Logical operators (and, or, not) - Used to combine conditional statements




# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]
if x in numbers:
    print(x in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
