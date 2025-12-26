#module =   a file containing code you want to include in your program using "import"
# useful to break up a large program reusable seperate files

#   List of modules
print(help("modules"))


#   help from specific module
print(help("math"))


#   import math ---normal
#   Alternative
import math as m        #need not write math this math that every time
print(m.pi)


#importing specific built ins from module
from math import pi
print(pi)  #        just imports the pi built in from math module

from math import e
a,b,c,d,e = 1,2,3,4,5 # e!=2.17...      e==5   dynamically changes
print(e**e)# returns 3125







"""Making your own module:"""

import examplemodule        #module name only letters

print(examplemodule.pi) # 3.1415
print(examplemodule.area(5))    #78.53750000000001
print(examplemodule.sqr(5))     #25
