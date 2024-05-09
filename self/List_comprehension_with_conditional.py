x = [223,332,226,-999]
y = [(i/10) for i in x if i != -999] # List comprehension with if conditionals
print(y)

#--------------------------------------------
# List comprehension with if else statement

x = [223,445,224,-999,324]
y = [i/10 if i!=-999 else 0 for i in x]
print(y)