def shipping_label(*args,**kwargs):# POSITIONAL,KEYWORD--- ARGS,KWARGS
    for arg in args:
        print(arg,end=" ")
    print()#new line for the order 
    for key,value in kwargs.items():
        print(f"{key}:{value}")

shipping_label("Dr","Drake",city="Toronto",country="Canada",product="Ear Buds")