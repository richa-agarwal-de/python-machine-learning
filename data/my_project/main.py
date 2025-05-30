# first way of importing a module
# from my_package import math_operations as m

# another way of importing a module
# import my_package.string_operations as s

# another way of importing 
# from my_package import *

# another way of importing 
import my_package as p

# importing subpackage
# from my_package.sub_package import *

# importing modules from sub package
# import my_package.sub_package as sub

from my_package.sub_package import collection_operations as c

print(p.math_operations.summ(3,4))

print(p.string_operations.strlen('Hello'))

print(c.dummy(10))