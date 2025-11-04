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



















