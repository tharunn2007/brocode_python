email=input("You email:") #my email be learnpython@gmail.com
index_=email.index("@")
username=email[:index_]
domain=email[index_:]
print(f"name:{username}|domain:{domain}")