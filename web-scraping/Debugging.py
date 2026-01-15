### Debugging Fundementals
 # Runtime Errors
 # Synatx Erros
 # Logical Erros

## stack trace / traceback - Errors show in this (terminal)

# print(10/0)
# print(my_variable)

import pdb

print("Start")
x = 5
pdb.set_trace()

y = 0 
y = x / y
