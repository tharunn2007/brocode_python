#   *args   =   allows you to pass multiple non-key arguements
# **kwargs  =   allowd you to pass multiple keyword arguements
#               *unpacking operator

"""Arbitrary means varying amount of arguements.We do not know how many
arguements the user is going to pass in to invoke a function """
#each of the args and kwargs is prefixed with un unpacking operator(*) yes just an asterisks

# args store the parameters as tuple whereas kwargs as in dictionary


def add(a,b):
    return a+b
print(add(1,2,3)) #OUTPUT:ERROR ONLY 2 POSTIONAL BUT 3 GIVEN
  

"""ARGS EXAMPLE"""

def add(*args):#NOT NECESSARY TO TYPE IN *args we can also put *nus,*xyz BUT "*" is important
    #args---treated as tuple
    total=0
    for arg in args:
        total += arg
    return total
print(add(1,2,3,4))
#OUTPUT: 10


"""KWARGS EXAMPLE"""
def address(**kwargs):
    #kwargs--- treated as dictionary
    for key,value in kwargs.items():
        print(f"{key}:{value}")

address(country="India",state="TN",city="Coimbatore")

#LIST OF DICTIONARY FUNCTIONS: 
#   for value in kwargs.values()----list of values
#   for key in kwargs.keys()-------- list of keys
#   for key,value in kwargs.items()----list of nested tuples having (key,value) so both can be accessed at same time



#~~~~~~~~~~~~~SHIPPING LABEL~~~~~~~~~~~~~~~~~#
#ships to the person and the address is given for shipping
def shipping_label(*args,**kwargs):# POSITIONAL,KEYWORD--- ARGS,KWARGS
    for arg in args:
        print(arg,end=" ")
    print()#new line for the order 
    for key,value in kwargs.items():
        print(f"{key}:{value}")

shipping_label("Dr","Drake",city="Toronto",country="Canada",product="Ear Buds")

#OUTPUT
"""
Dr Drake 
city:Toronto
country:Canada
product:Ear Buds
"""




