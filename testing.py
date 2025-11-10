username=input("Enter your name:")

if len(username)>12:
    print("Too long!")
elif not username.find(" ")==-1:
    print("Not spaces in name")
elif username.isdigit()==True:
    print("No digit in name.")
else:
    print("Name verified!")
