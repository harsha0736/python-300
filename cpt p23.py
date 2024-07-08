import random
def good(x,y):
    print("X:",x)
    print("Y:",y)
    s=x+y
    if s>6:
        print("yes")
    else:
        print("no")
        
X=random.randint(1,6)        
Y=random.randint(1,6)
good(X,Y)
            