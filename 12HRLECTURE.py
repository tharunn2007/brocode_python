print("hello world")   #single quotes is valid too 





#variable:a containing vessel for a value(the value can be string,integer,float or boolean)
#variable will behave like the type of value it is assigned to it

string_given="Tharunn123TrueFalse,3.0;:!@#$%^&*(){hey}"   #anything under double quoates or single qouates are string curly bracket thingy will be seen later
print(string_given)
#formatting strings are used to make strings more dynamic and we can add the values of variables inside strings given below an example
print(f"Curly brackets are used to add cariables like this:{string_given}")#f is given before the quotes and curly brackets are used as place holders for variables

integer_given=1234567890#integer is an whole number without decimal point
print(f"Integer value is :{integer_given}")
float_given=3.14159265358979323846#float is a number with decimal point 
print(f"Float value is :{float_given}")
boolean_given=True#boolean is either true or false
print(f"Are you enjoying the lecture?:{boolean_given}")
if boolean_given==True:
    print("Yay! Enjoy the lecture")
else:#here else is used to give an alternative condition if the if condition is false
    print("Boring")






#type casting:converting one data type to another data type
string_to_integer="12345"#string value
    #can be converted with these functions like str(),int(),float(),bool()
string_to_integer=int(string_to_integer)#updated to int
string_to_integer=float(string_to_integer)#updated to float 12345.0
    #approximations in float and int
gpa=3.2
gpa=int(3.2)#updates to 3
gpa2=4.8
gpa2=int(gpa2)#updates to 4....now here we can say that even though decimal is near to 5 its gets rounded to 4 as sunch as a step functions
    
    #concatenation rules:only similar data types can be concatenated or else ERROR
    #FACT: integer and float data types cn be added as listed
    
x=1
y=3.14
print(x+y)  #----- gives OUTPUT:4.14 as a float type







#input() is a function that takes in input from user to be entered....with thin the quotes string sentence can be included
name_input=input("What is your name:")# I can give my name as Tharunn
print(f"Hello there {name_input}!")#------ PRINTS Hello there Tharunn!
#note:normally input() function takes in input as a string in default unless mentioned but we can change it
age_input=int(input("Enter you age:"))
mark_input= float(input("Enter you marks:"))





#~~~~~~~~~PROJECT:MADLIBS~~~~~~~#
#madlibs:you mke up a story using the nouns,adverb,adjective and sort of things likt that and make up a story
adjective1=input("Enter adjective1:")
adjective2=input("Enter adjective2:")
adverb=input("Enter adverb:")
noun=input("Enter noun:")
print(f"Yesterday,I went to {noun}'s house which was very {adjective1}.His mom gave me a glass of juice which was {adverb} and also spoke {adjective2} German.")
#OUTPUT:Yesterday, I went to Arjun's house which was very huge.His mom gave me a glass of juice which was tasty and also spoke good German.
#~~~~~~~~~~OVER~~~~~~~~~~~#






#truncating decimal places using round()function.
Numerator=10
Denominator=3
Division1_gives=Numerator/Denominator
print(Division1_gives)#~~~~~~~OUTPUT= 3.3333333333333335
rounded_Division1_gives=round(Division1_gives,2)#Rounding off to 2 Decimal places
print(rounded_Division1_gives)#~~~~~~~~~OUTPUT= 3.33






#MATH AND MATH MODULE IN PYTHON AND HOW TO USE IT:
#topics:arithmetic operators,math functions and few exercises
plus=0
plus= plus+1 
#IS SAME AS:
plus+=1
#######SAME GOES FOR SUBTRACTION(-=),MULTIPLICATION(*=),DIVISION(/=),POWER(**=),REMINDER MODULUS(%=),

#BUILT IN FUNCTIONS:

#round()----rounds of the decimal places
dsd=2.7185
res=round(dsd,2)
print(res)#----------OUTPUT: 2.7185 ~ 2.718 ~ 2.72(.5 is always substituted to 0)

#abs()----modulus funtion in calculus
wer=-9.234
ewr=abs(wer)
print(ewr)#--------OUTPUT: 9.234

#power()-------just same as a**x  but written as pow(a,x)
resu=pow(2,4)
print(resu)#--------OUTPUT: 16

#max()-------maximum value between given value
#min()------minimum value between given value
qw=2
we=3
er=4
print(max(qw,we,er),min(qw,we,er))#------OUTPUT:4 2 

#USING MATH MODULE~~~
#use import math
import math
print(math.pi)#-----OUTPUT:prints pi value 3.1415....15 digits
print(math.e)#------OUTPUT:prints e value 2.718....15 digits
cv=3
sqres=math.sqrt(cv)#--------give any value inside bracket
print(sqres)#--------OUTPUT:1.732....15 digits
resut=math.ceil() # gives the appoximation as 9.1---10 LEAST INTEGER FUNCTION
resut=math.floor()#gives the approximation as 9.8---9 GREATEST INTEGER FUNCTION


#~~~~~CIRCUMFERENCE and AREA CALCULCULATION~~~~~#
import math
radius=float(input("Enter radius"))
circumference=2*math.pi*radius
print(f"The circumference of the circle is {round(circumference,2)} units")
area=math.pi*pow(radius,2)
print(f"THe area of the circle is {round(area,2)} units.sq")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#







#if statement---does some code only IF some condition is True
#else statement----it does the code if the it didnt satisfy the the True if
#elif---(else if)---prints for any intermediate condition to be checked other than if

#---EXAMPLE1:#
age=int(input("Enter your age:"))
if age>= 18:#----Checks if input is 18 and above or not
    print("Valid.You can sign up.")#if yes----this prints
elif age<0:
    print("AGe less than 0 is not possible.")#If user is made mistake to give negative age :P
elif age>100:
    print("Too old to sign up")
else:
    print("Access denied.")#if no---this prints
#NOTE:-----only 1 IF and 1 ELSE can be given all other condtions to be checked with elif statements only

#---EXAMPLE2:#
response=input("Wanna have some food?(Y/N)")
if response=="Y" or response=="y":#we can give either Y or y
    print("Have some.")
elif response=="N" or response=="n":#we can either can N or n
    print("Have a nice day")
else: # for cases other than Y,y,N,n
    print("wrong")

#---EXAMPLE3:#
for_sale=True
if for_sale: #ALREADY ASSIGNEND FOR SALE TO BE TRUE....
    #other way of--- if for_sale==True:
    print("Item for sale:")
else:
    print("Item not for sale")







#~~~~~~~~~~~~PROJECT:PYTHON CALCULATOR~~~~~~~~~#
operator_type=input("Print the operator type:")
n1=float(input("Enter n1:"))
n2=float(input("Enter n2:"))

if operator_type=="+":
    print(f"Addition:{n1+n2}")
elif operator_type=="-":
    print(f"Subtraction:{n1-n2}")
elif operator_type=="*":
    print(f"Multiplication:{n1*n2}")
elif operator_type=="/":
    print(f"Division:{n1/n2}")
else:
    print("Basic calculator only so only limited to 4 basic arithmetic operations.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#







#~~~~~~~~~~~~~~~~~PROJECT:WEIGHT CONVERSION~~~~~~~#
conversion_unit=input("ENter the type of SI unit of value (kg/lb):")
value=float(input("Enter the value:"))
if conversion_unit=="kg" or conversion_unit=="KG":
    kg_to_lb= value*2.204623
    print(f"THe value in|kg:{round(value,3)}|lb:{round(kg_to_lb,3)}")
elif conversion_unit=="lb" or conversion_unit=="LB":
    lb_to_kg= value/2.204623
    print(f"THe value in|lb:{round(value,3)}|kg:{round(lb_to_kg,3)}")
else:
    print("Not under the regulated weight conversion unit")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#









#LOGICAL OPERATORS:used in conditional statements
#             and---checks 2 or more conditions to proceed if True
#             or---checks atleast one condiion to be True to proceed
#             not---True if condtion is False,and vice versa

temp=25#lets say
if temp>0 and temp<=30:#Prints statement only if temp is greater than zero and less than 30 as well
    print("The temperature is good.")
elif temp<0 or temp>30:#prints statement either if the temperature is sub zero or more than 30
    print("Extreme Temperature.")
else:
    pass#pass is used just for the sake of dummy 

#use of not is more different 
sunny=True
if sunny:
    print("Its sunny outside")
else:
    print("Its cloudy outside")

cloudy=True
if not cloudy:#input=true but output is false 
    print("Its not cloudy")
else:
    print("Its cloudy")









#Condtional expression= A oneline shortut for the if-else statement(ternary operator)
#                    print/assign one of the two values based on a condition
#                    X if <condition> else Y
number=5
print("Positive" if number>0 else "Negative")
resultt="Even" if number%2==0 else "Odd"
print("Resultt")#~~~~~~~OUTPUT:Odd

number2=6
number3=7
max_num= number2 if number2>number3 else number3
min_num=number2 if number2<number3 else number3
print(max_num,min_num)#~~~~~~~~OUTPUT:7 6












#BUILT IN STRING FUNCTIONS AND METHODS:
name= "Bro Code"

#        string length---len()
str_len=len(name)
print(str_len)#~~OUTPUT:8    (The blankspace is also considered as a charecter)

#       name.find()---gives the first occurance INDEX VALUE of a given charecter
found=name.find("o")
print(found)#~~OUTPUT:2  the second index value 0,1,2 
                                            #   B,r,o
found2=name.find("z")
print(found2)   #OUTPUT:-1   if it didnt recognise the charecter in the given string it PRINTS -1 and NOT AN ERROR 

#      name.rfind()---gives the last occurance INDEX VALUE of given charecter
found3=name.rfind("o")
print(found3)  #OUTPUT: 5 [B,r,o, ,C,o=5,d,e]
#again returns -1 if the charecter not found

#      name.capitalize()---captitalize the first charecte in a string
name2="bro code"
capitaliz=name2.capitalize()
print(capitaliz)#---- OUTPUT:Bro code

#     name.upper()---upper case transformed for every charecter
uppered=name.upper()
print(uppered)#   OUTPUT: BRO CODE    (even if the name was BrO cOdE---changes to BRO CODE)

#     name.lower()---everything is lower
lowered=uppered.lower() #uppered=BRO CODE
print(lowered)#   OUTPUT:bro code

#     name.isdigit()---True if the string ONLY contains integer else False
#True for INTEGERES ONLY...False for FLOAT as float contains a decimal point
#   Bro Code--False,Bro123--False,123--True,123.92--False


#     name.isalpha()---True if string ONLY contains alphabetical charecters..else false
# Bro Code---False(cointains blankspace),Bro123--False(numbers),BroCOde--True

#     count()----Counts the reoccuring of the specific charecters in a string
#Example:
ph_no="1-234-453-21-324-1242"
result2=ph_no.count("-")
print(result2) #~~~OUTPUT: 5

#     replace()---Replaces one type of string to another type
result3=ph_no.replace("-"," ")
print(result3)#~~~OUTPUT: 1 234 453 21 324 1242

result4=ph_no.replace("-","")
print(result4)#~~~OUTPUT: 1234453213241242

#FOR NEED OF ANY HELP: help()
# for list of comprehensive string methods that you can use we can use help()
print(help(str))
#OUTPUT:.....dont get scared...
"""
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |  
 |  count(self, sub, start=0, end=9223372036854775807, /)
 |      Return the number of non-overlapping occurrences of substring sub in string
 |      s[start:end].
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |  
 |  endswith(self, suffix, start=0, end=9223372036854775807, /)
 |      Return True if the string ends with the specified suffix, False otherwise.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |  
 |  find(self, sub, start=0, end=9223372036854775807, /)
 |      Return the lowest index in the string where substring sub is found.
 |  
 |  format(self, /, *args, **kwargs)
 |      Return a formatted version of the string using format() style.
 |  
 |  format_map(self, mapping, /)
 |      Return a formatted version of the string using a mapping dictionary.
 |  
 |  index(self, sub, start=0, end=9223372036854775807, /)
 |      Like find(), but raise ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |  
 |  islower(self, /)
 |      Return True if all cased characters in the string are lowercase and there is
 |      at least one cased character, False otherwise.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |  
 |  isprintable(self, /)
 |      Return True if all characters in the string are printable, False otherwise.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |  
 |  isupper(self, /)
 |      Return True if all cased characters in the string are uppercase and there is
 |      at least one cased character, False otherwise.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |  
 |  removeprefix(self, prefix, /)
 |      Return a string with the given prefix string removed if present.
 |  
 |  removesuffix(self, suffix, /)
 |      Return a string with the given suffix string removed if present.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |  
 |  rfind(self, sub, start=0, end=9223372036854775807, /)
 |      Return the highest index in the string where substring sub is found.
 |  
 |  rindex(self, sub, start=0, end=9223372036854775807, /)
 |      Like rfind() but raise ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator, starting from
 |      the right.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |  
 |  startswith(self, prefix, start=0, end=9223372036854775807, /)
 |      Return True if the string starts with the specified prefix, False otherwise.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a titlecased version of the string.
 |  
 |  translate(self, table, /)
 |      Return a copy of the string in which each character has been mapped through the
 |      given translation table.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
None
"""


#~~~~~~~~~~~~~~~PROJECT:USER NAME VALIDATION~~~~~~~~~~~~~~#
#username nor more than 12 charecters
#username must not contain spaces
#username must not contain digits

username=input("Enter your name:")

if len(username)>12:
    print("Too long!")
elif not username.find(" ")==-1:#if it didnt find anythin it prints -1 BUT we added with a not statment therefore it the given condition comes out opposite then it prints the statement
    print("Not spaces in name")
elif username.isdigit()==False:
    print("No digit allowed in name.")
else:
    print("Name verified!")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#










#indexing = accessing INDIVIDUAL elements using the sequence using [](aka. indexing operator)
# indexing operator-----[start:end:step]   ###(IMPORTANT PART)
cred_no="123-41-1221-12451"
#~~~~~~~~0---------------17   in forward it starts from zero
#~~~~~~~-18-------------(-1)  in reverse it starts from -1
print(cred_no[3])#OUTPUT: -
print(cred_no[-3])#OUTPUT: 4
print(cred_no[0:5])#prints from index zero-TO index 4 EVERYTHING UNDER 5 ##OUTPUT: 123-4
print(cred_no[0:8:2])#print and skips with 2 value in step ##OUTPUT: 134-   doesnt go to 8
print(cred_no[8:0:-2])#- step gives reverse counting---OUTPUT:2-43
#NOTE:
cred_no[0:7]==cred_no[:7] # not neccessary to give number if we indexing is starting at the beginning
cred_no[6:] # starts with 6 and prints till the end of the string ## OUTPUT:1-1221-12451
print(cred_no[::-1]) #START TO END but in reversed complete ##OUTPUT: 15421-1221-14-321

#Hope you could make more ways of indexing with these sample....










#~~~~~~~~~~~PROJECT:EMAIL SLICER~~~~~~~~~~~~~~~~~~~~#
email=input("You email:") #my email be learnpython@gmail.com
index_=email.index("@")
username=email[:index_]
domain=email[index_:]
print(f"name:{username}|domain:{domain}")
# OUTPUT: name:learnpython|domain:gmail.com
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#









#formatted specifiers = {:<flags>} format a value based on what flags are inserted
#USED IN THE CONTACT OF "f" string (just like the formatted strings that we see in print())
#NOTE:The format specifiers SHOULD be included in the place holders of f string ONLY.
price1=3.14159
price2=-978.65
price3=12.34

# .(number)f  = round of the the given "number" decimal places
print(f"The prices are {price1:.3f},{price2:.3f}")
###OUTPUT: The prices are 3.142,-978.650

# :(number)   = allocate that many spaces( EXPLANATION:If we give the number,the given output of the data would have been filled with that many spces so its length is the number we have given)
print(f"The prices with spaces are ({price1:10}),({price2:20})")
###OUTPUT: The prices with spaces are (   3.14159),(             -978.65)   #hope u get it
                                       # 10 length   #20 length

# :0(number)        = allocate and zero pad that many spaces (same as previous but adds zero instead of spaces)
print(f"The prices with zeropads are ({price1:010}),({price2:020})")
###OUTPUT: The prices with zeropads are (0003.14159),(-0000000000000978.65)~~Negative sign goes out

# :<(number)        = left justify (does the same as :(number) but all the spaces added in after our given charecters)
print(f"The prices with left justify are ({price1:<10}),({price2:<20})")
###OUTPUT: The prices with left justify are (3.14159   ),(-978.65             )

# :>(number)        = right justify 
#NOTE: right justify is same as .(number)f 


# :^(number)        = center align(numbers are centered in spaces)
print(f"The prices with center aligned spaces are ({price1:^10}),({price2:^20})")
###OUTPUT: The prices with left justify are ( 3.14159  ),(      -978.65       )

# :+          = use a plus sign to indicate postive value else leaves it
print(f"The prices with positive value indication are ({price1:+10}),({price2:+20})")
###OUTPUT: The prices with sign indication are (  +3.14159),(             -978.65)

# :=          = place the sign to left most position
print(f"The prices with left sign justify are ({price1:=10}),({price2:=20})")
###OUTPUT: The prices with left justify of signs are (   3.14159),(-             978.65)

# :(space)    = insert a space before positive numbers
print(f"The prices with spaces are ({price1: 10}),({price2: 20})")
###OUTPUT: SAME AS :(number)

# :,          = comma seperator that makes the numbers like 100044 as 100,044
price4=23412352.232
price5=-25231345
print(f"The prices with comma seperated are ({price4:,}),({price5:,})")
###OUTPUT: The prices with comma seperated are (23,412,352.232),(-25,231,345)


#MIXED FORMAT SPECIFIERS in python---uses multiple specifiers to use at a same time
print(f"The price4 with using mixed format specifiers are({price4:+,.2f})")
###OUTPUT: The price4 with using mixed format psecifiers are (+23,412,352.23)<------
                                                                                  #|
print(f"The price4 with using mixed format specifiers are({price4:+,.2f,^20})")#   |
#ERROR!!! can do only maximum upto 3 format specifiers in the above given problem -|
















#while loop statements
#  while loop= execute some code WHILE some condition is True

#one of the thing is to repeat the code again until its true 
import math
while True:
    just_something= int(input("ENter a number"))
    if just_something%2==0:
        print(f"The number is even and its root is:{math.sqrt(just_something):.3f}")
    else:
        print(f"The number is odd and its cube is:{math.pow(just_something,3):^20}")
    break

###OUTPUT:
#   ENter a number2
#   The number is even and its root is:1.414
#   ENter a number3
#   The number is odd and its cube is:        27.0        
#   ENter a number 

#It asks the enter the number for every single time...


#this is infinitely repeating unless we doesnt designate it to some other number of times to be repeated.
#how exactly it is different from for loop?  
#for loop iterate over a sewquence but while loop is printing when the condtions is true and stops when it becomes false

ntimes=input("NUmber of times you want to print the greeting..:")
i=0 #unlike for loop we gotta define the variables
while i<ntimes:
    print(f"Hello there {i+1}")
    i+=1
###OUTPUT:
#  NUmber of times you want to print the greeting..:5
#  Hello there 1
#  Hello there 2
#  Hello there 3
#  Hello there 4
#  Hello there 5

#the code ends before the i reach 5 and the loop ends in while

#example:
name323=input("Enter:")
while name=="":
    print("Disnt enter the name")
    name323=input("ENter name:")#if we dont give this staement then this creats an infinite loop and that is not good
print(F"hello {name323}") #asks the name repeatedly until something is written in the input

#NOTE: it is ALWAYS IMPORTANT TO WRITE AN EXIT STATEMENT so not to cause an infinite recurring loop


food=input("Wanna eat something? (y/n)")
while not food == "n":
    print("So what is your faourite and")
    food=input("Enter the food name you like or even then if you wanna quit:(y/n)")
print("Bye")
###OUTPUT:
#   Wanna eat something? (y/n)y
#   So what is your faourite and
#   Enter the food name you like or even then if you wanna quit:(y/n)n
#   Bye











#NOTE: You gotta do ALL projects by yourself without the tutorial!!









#~~~~~~~~~~~~~~~~~PROJECT:COMPOUND INTEREST CALCULATOR~~~~~~~~~~#
n_people=int(input("Enter for the number of the people to calculate:"))
i=0

while i<n_people:
    principle_investment=float(input("Enter the investment of yours:"))

    rate_frequency=input("Enter the rate calculated(monthly/yearly):")
    if rate_frequency=="yearly":
        n_times=1
    elif rate_frequency=="monthly":
        n_times=int(input("Enter the number of times rate calculated in a year:"))
    else:
        print("Invalid.Please try again!")
        rate_frequency=input("Enter the rate calculated(monthly/yearly):")

    rate=float(input("ENter the rate of interest:"))

    time_yearly=int(input("ENter the number of years you gonna be payin the ecompund interest for in years:"))

    compund_amount=principle_investment*((1+((rate/100)/n_times))**(time_yearly*n_times))
    compound_interest=compund_amount-principle_investment

    print(f"User name: {i+1}|Compound amount accumulated:{compund_amount:,.3f}|Compound interest:{compound_interest:,.3f}")

    i+=1
    #you can actually do a lot better code with this
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#











#for loops:execute a code of block for fixed number of times we can use range,len,sequence,etc.

#for loops are better at executing than while loops when WE KNOW to iterate FIXED number of times

#break statement----doesnt let the other statements to be executed once this statement ot be executed in a loop.

#nested loop = loop within a loop
#outter loop:
#   inner loop:

for x in range(1,10):
    print(x,end="")#----end gives the loop execution pattern
#OUTPUT~~~ 123456789
    print(x,end=" ")
#OUTPUT~~~ 1 2 3 4 5 6 7 8 9
    print(x,end="\n")
""" 
OUTPUT:
1
2
3
4
5
6
7
8
9
"""
#NESTED LOOP:
# in nested for loops the variable counters should not be the same 

for i in range(3):
    for j in range(1,6):
        print(x,end="")
#OUTPUT:123451234512345


#Pattern based problems are very good to solve loops and nested loops
#
##
###
####
#####
####
###
##
#    patterns like this and so on!!






#~~~~~~~~~~~~~~~~~~~~~~~~COUNTUDOWN TIMER PROGRAM~~~~~~~~~~~~~~#
#USES AN INBUILT FUNCTION MODULE 


import time
variable_time=int(input("Enter how long IN SECONDS you want to sleep:"))
for x in range(variable_time,0,-1):
    print(x)
    time.sleep(1)#program sleeps or doesnt show anything for a given amount of seconds...
print("TIMES UP!")

#GAVE 3
"""OUTPUT:
Enter how long IN SECONDS you watn to sleep:  
3
2
1
TIMES UP!
"""

#for showing like xx:yy:zz
import time
inp_time=int(input("enter the timer:"))
for x in range(inp_time,0,-1):
    seconds=x%60  #incase if the seconds left is 70 then it shows 70%60 which is 10
    hours=x//3600 #counts the full hours
    minutes=(x%3600)//60 #counts the minutes aside from full hours by giving the modulo
    time.sleep(1)
print("TIMES UP")#after the countdown over this line executes that is why it is outside

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

























#collections= single "variable" used to store multiple values
# List= []----Ordered,mutable,duplicates OK
# Set=  {}----unordered,immutable(add/remove OK),duplicates NO
# Tuples= ()--Ordered,immutable,DUplicates OK. FASTER IN TERMS OF ELEMENT ACCESS due to immutability that doesnt cause complexitites


#_______________LISTS_____________#

list_eg=["a","b","c","d"]
#list and tuples also have indexing from 0 to n-1 is n is the number of elements
#accessing out of the index range GIVES IndexError
#TO CHECK WHAT KIND OF FUNCTIONS CAN LIST PERFORM::

print(dir(list_eg))
"""OUTPUT:
delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']"""

print(help(list_eg))
#helps with the attibutes and elements we could work upon

print(len(list_eg))#length of list

print("e" in list)#boolean true or false  here its false
  #normal access <list name>[]
#NOTE: for NESTED LISTS accessing doen throuh list[i][j],ith element in main list and jth element in the sublist/tuple

print(list_eg.append("e"))#appends list element to LAST INDEX PLACE


list_eg.remove("b")#REMOVES b     PARAMETER REQUIREMENT IS MANDATORY else TypeError

list_eg.insert(1,"b")  #inserts b into INDEX 1

list_eg.sort()# SORTS either in ASCENDING alphabetical or number order
#NOTE: for descending order its 
list_eg.sort(revrese=True)


#genreally reversing a  functions list in 180
list_eg.reverse()  #---- Gives:  ["d","c","b","a"]

#finding index of a functions
print(list.index("a"))# prints 0
#IF there is no index is given ERROR

#if the value in the given list doesnt exist....THEN PRINTS ValueError


#counting the recurrances of a element in a list 
print(list_eg.count("a")) # returns 1   (since we have only 1 a in our list)


print(list_eg.len())  #finds the length of the list

#pop() removes the element at the specific index.IF no index value is given then it pops the LAST element AND PRINTS
list_2=[1,2,3,4,5,6,7,"qwd"]
popped=list_2.pop()
print(popped) #OUTPUT-qwd
print(list_2) #OUTPUT-[1,2,3,4,5,6,7]
list_2.pop(4)
print(list_2)#OUTPUT--[1,2,3,4,6,7]
#VERY IMPORTANT

list.clear()#CLEARS EVERY ELEMNTS leaving the list alone

#____________SETS____________#
#SET takes in ONLY UNIQUE ELEMENTS
list_eg2=[1,2,3,45,56,1,3]
exampleset=set(list_eg2)
print(exampleset)#OUTPUT----{2,1,3,45,56}


#FOR GETTING WHAT methods can be used
print(dir(exampleset))
print(help(exampleset))

#We can check if there is an element in a set by <name> in exmpleset (just as for list) True/False boolean answer given

#TYPE ERROR RISES IF WE ASK FOR INDEX
print(exampleset[0])#OUTPUT---TypeError

#add("your input"),remove("you input") can be Done
 
exampleset.pop()#randomly removes any element rom the set

exampleset.clear()#clears EVERY ELEMENT from the set and returns only empty set


 
#_________TUPLES_____________#
#Most functions used in lists can be usd but rather it cant duplicate 
#CONCATENATION,MULTIPLICATION of tuples are VALID since we are not changing the original tuple but rather new tuple to be created
#tuples are iteratable as well and FASTER compared to list


#NOTE: How to add things into tuple??
#make the tuple as a list as list(<tuple name>),and add into the list and again convert it back to tuple.
#Same thing goes to sets as well but 
#_______________________________#

 

###PYTHON 2D COLLECTIONS based on the ested lists in a list
#have a pattern of matrix
matrix_list=[[1,2,3]
             [4,5,6]
             [7,8,9]]
matrix_list[0][0]#output-1 

for i in matrix_list:
    for j in i:
        print(j,end=" ")
    print() #outside the loop to print newline for every in nested list is being edded one time





asd=[],asw=()
zip({asd},{asw}) #zip is an function that helps in  iterating mutiple variables at once



#~~~~~~~~~~~~~~~~~~~QUIZ GAME~~~~~~~~~~~~~~~~~~#
print("CONTAINS NEGATIVE MARKING")
questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ", "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))



answers = ["C", "D", "A", "A", "B"]
Score = 0
question_num = 0
count_correct=0
count_incorrect=0
for q in questions:
    print("______________________________")#as a part of partitioning the questions
    print(q)
for o in options:
    print(o)

guesses=input("Enter the options from question 1 to 5 to be entered as _,_,_,_,_:").upper().split(",")

for i,j in zip(answers,guesses): 
    if i==j:
        Score+=1
        count_correct+=1
    else:
        Score-=0.25
        count_incorrect+=1

    print(f"Answer: {i}, Guess: {j}")
print(f"FINAL SCORE:{Score}")
print(f"Correct:{count_correct}|Incorrect:{count_incorrect}")
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




















#_________DICTIONARIES___________#
# dictionary = a collection of {key:value} pairs
# ordered and mutable.No duplicates (EVERY KEY MUST BE UNIQUE EVEN THOUGH VALUES CAN BE SAME)


ascii_dict={"A":65,"B":66,"C":67,"D":68}

print(dir(ascii_dict))#lists the attributes on the dictionary can be done
print(help(ascii_dict))#explanation of the attributes

#get()- used to get the value of the specific key 
print(ascii_dict.get("A"))
#IF THE KEY NOT PRESENT- returns None

#update()- ADDS  key value pair to last (IF IT IS NEW KEY) ELSE(UPDATES EXISTING KEY)
ascii_dict.update({"F":69})#adds F as 69th ascii
ascii_dict.update({"A":61})#----updates ascii of A as 61 OBVIOUSLY NOT TRUE

#pop()-  removes a key value pair
ascii_dict.pop("A")

#popitem()- removes the lates key value pair
ascii_dict.popitem()  #removes F:69 which was the  latest entry

#clear()  - cleears everything inside the dictionary


#####CONFUSING PARTS#####

#keys() 
keys= ascii_dict.keys()
print(keys)
#OUTPUT~~~ dict_keys(['A', 'B', 'C', 'D'])   keys are considered as object and therefore is in list format...WILL BE LEARNT IN POOP
#this can be used to iterate in a for loop
for i in keys:
    print(keys[0])
    #OUTPUT: prints A

#items()-returns the items in TUPLE format
d = {'A': 'Python', 'B': 'Java', 'C': 'C++'}

# using items() to get all key-value pairs
items = d.items()

print(items)
#OUTPUT__ dict_items([('A', 'Python'), ('B', 'Java'), ('C', 'C++')])




 #~~~~~~~~~~~~~~~~~~CONCESSION STAND~~~~~~~~~~~~~~~~~#
menu = {"pizza": 3.00,  "nachos": 4.50,"popcorn": 6.00,"fries": 2.50,"chips": 1,"pretzel": 3.50,"soda": 3.00,"lemonade": 4.25}
cart = {}
total = 0.0

print("_______MENU ITEMS AVAILABLE__________")
for key,value in menu.items(): # (key,value) in items that is given
    print(f"{key:.^10}:{value:.2f}/-")
print("______________________________________")

for foods in menu:
    food_inp=input(f"Would you like to buy {foods}(y/n)").upper()
    if food_inp=="Y":
        quantity_inp=int(input(f"How many of {foods} you would like to buy:"))
        cart.update({foods:quantity_inp})
        total+=menu.get(foods)*quantity_inp
    else:
        pass #if we break then it wont iterate for the next food item
    
print("PURCHASE OVER!THANK YOU FOR PURCHASING AT IMAX!",end="\n")
print(f"YOUR PURCHASE BILL|Total Cost={total:.2f}/-")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
















  























































