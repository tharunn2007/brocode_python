import time
end=int(input("Timer for:")) #  DEFAULT ARGUEMENT FIRST AND THEN NON DEFAULT order OR ELSE SYNTAX ERROR
def count(end,start=1):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
        if i == end:
            print("TIME OVER")
    return start,end
print(count(end))



