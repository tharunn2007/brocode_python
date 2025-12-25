#Iterables = An object/collection that can return its element one at a time,
#            allowing it to be iterated in a loop

numbers=input("Enter the list as follows: <a,b,c,d> for tuple| [a,b,c,d] for list:")#EVAL()----converts into tuple in default we use square bracket in case of list 
print(numbers)
#input: 1,2,3,4,5       output: (1,2,3,4,5)---a tuple
#input [1,2,3,4,5]      output: [1,2,3,4,5]--- a list
for i in numbers: # i is the iterable in the object collections
    print(i)
    """OUTPUT:
        1
        2
        3
        4
        5 """
for i in reversed(numbers): ### SETS ARE NOT REVERSABLE
    print(i)
    """OUTPUT:
        5
        4
        3
        2
        1"""
    print(i,end="")#NO SPACE
    """OUTPUT
        54321"""
    print(i,end=" ")
    """OUTPUT
        5 4 3 2 1"""
    print(i,end="#")
    """OUTPUT
        5#4#3#2#1# """
 