#function is a block of reusable code
#place () after the function name to invoke it

 #if i want  to print hello there 3 times  - i can either manually print 3 times - use a for loop ----most efficient is by functions

def hellothere():
     print("hellothere")
#invoking the function
hellothere()
hellothere()
hellothere() #we invoked 3 times to print "hellothere"

def hellothere(name):
     print(f"hellothere {name}")
#invoking the function
hellothere("Tharunn") #these are ARGUEMENTS we pass in the value to be substituted that can we used in the function
                    #so the NAME is the parameter and Tharunn is our inut parameter
                    #think of it like f(x)=x^2+2x-1 at x=1,where name is equivalent to the equation and Tharunn is equivalent to x=1
hellothere("Bro")
hellothere("Tony")

"""We can pass in multiple arguements but at the same way the top def functions
 must hvae equal parameters to accept the arguement values """

def cheese(name,age):##2 parameters for taking 2 arguements
     print(f"YOUR {age}, and name is {name}")
cheese("Tony",23)

####ORDER MATTERS IN PARAMETERS AND ARGUEMENTS...be sure to give the input for which parameter to be given properly
"""This is wrong
def cheese(name,age):##2 parameters for taking 2 arguements
     print(f"YOUR {age}, and name is {name}")
cheese(23,"Tony")"""

###IMPORTANT PART AHEAD



#return =  statement used to end a function
        # and send a result back to the function caller- function()---the one we add end of the function to pass in arguements


#ADD AND SUBTRACT 2 NUMBERS
x=int(input("ENter the number 1:"))
y=int(input("Enter the number 2 :"))
def arithmetic(x,y):
    a=x+y
    b=x-y
    return a,b
print(arithmetic(x,y))####ONCE RETURN IS GIVEN WE HAVE TO ASK TO PRINT SINCE IT JUST STORES 
"""OUTPUT:
ENter the number 1:2
Enter the number 2 :3
(5, -1)"""

#return a
#return b   is not valid because once reutrn is given for the first variable then it doesnt come to next and therefore comma used
first=input("Enter first name:").lower()
last=input("Enter last name:")
def fullName(first,last):
     first=first.capitalize()
     last=last.capitalize()
     return first + " " + last
print(fullName(first,last))
     
     
      


    





 