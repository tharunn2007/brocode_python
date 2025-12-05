#   *args   =   allows you to pass multiple non-key arguements
# **kwargs  =   allowd you to pass multiple keyword arguements
#               *unpacking operator

"""Arbitrary means varying amount of arguements.We do not know how many
arguements the user is going to pass in to invoke a function """
#each of the args and kwargs is prefixed with un unpacking operator(*) yes just an asterisks

# args store the parameters as tuple whereas kwargs as in dictionary


def add(a,b):
    return a+b
print(add(1,2))