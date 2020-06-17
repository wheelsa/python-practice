# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''
# 
"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# x = 1      # int
# y = 2.5    # float
# name = 'Seth' # string
# isCool = True # bool
# print(x + y + name + isCool)

#Multiple Assignments

x, y, name, isCool = (1, 2.5, "Seth", True)

print(x, y, name, isCool)

a = x + y

print(a)

print(type(a))

x = str(x)
y = int(y)
print(type(x))
print(type(y))

print(y)