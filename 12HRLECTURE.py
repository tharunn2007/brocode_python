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
print(f"The prices with left justify are ({price1:^10}),({price2:^20})")
###OUTPUT: The prices with left justify are ( 3.14159  ),(      -978.65       )

# :+          = use a plus sign to indicate postive value else leaves it
print(f"The prices with left justify are ({price1:+10}),({price2:+20})")
###OUTPUT: The prices with left justify are (  +3.14159),(             -978.65)

# :=          = place the sign to left most position

# :(space)    = insert a space before positive numbers
# :,          = comma seperator






























































