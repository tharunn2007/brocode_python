# keyword arguement = arguement preceded by identifier
#                   uses: for better readability
first=input("Enter first name")
last=input("Enter the last name")
greeting=input("Enter the greeting word")

def greet(first,last,greeting,title="Mx"):
    print(f"{greeting}!Nice meeting you {title}.{first} {last}! ")

greet(last,greeting,first,title="Mr") ###  THE MR THAT IS GIVEN HERE IS THE KERWORD ARGUEMENT
#NOTE: For keyword arguements order of our keyword arguement input doesnt really matter because we already assigning value and computer need not confuse for it
#POSITIONAL ARGUEMENTS FIRST AND THEN KEYWORD ARGUEMENTS NEXT

