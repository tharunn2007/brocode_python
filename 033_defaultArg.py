# default arguement = A default value for certain parameters
#                      used when argument (what we give as input) is ommitted
#                       makes functions flexible (since not prone t give error if we dont give arguement)

#                TYPES:   positional ,default ,keyword, arbitary






def function(x=1,y=3):#We can give the default arguement already to the function iteself
     print(f"{x},{y}")
function() #REDUCES THE NUMBER OF ARGUEMENTS
#INCASE WE DONT GIVE OUR OWN INPUT
#OUTPUT:1,2
function(3,4) #x,y changes to 3,4
#OUTPUT: 3,4

"""Why we use default arguement?
    We use default arguements when a certain parameter is tend to be
    consistant throughout the function i.e. like in shopping malls the discount tend to be 30 or 40% 
    throughout every customer purchasing"""

#COUNTING TIMER
import time
end=int(input("Timer for:")) # NON DEFAULT ARGUEMENT FIRST AND THEN DEFAULT order OR ELSE SYNTAX ERROR
def count(end,start=1):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
        if i == end:
            print("TIME OVER")
    return start,end
print(count(end))
"""OUTPUT
Timer for:4
1
2
3
4
TIME OVER
(1,4)"""#(1,4) is due to return
# we can change the start even from 0 to other number

#better solution
def count(end, start=0): 
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!") # Prints once after loop finishes
