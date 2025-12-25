#Iterables = An object/collection that can return its element one at a time,
#            allowing it to be iterated in a loop

numbers=eval(input("Enter the list as follows: a,b,c,d")) #EVAL()
for i in numbers: # i is the iterable in the object collections
    print(i)
for i in reversed(numbers): #The list is reversed and its now iterated
    print(i)
 