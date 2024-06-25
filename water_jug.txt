x=0
y=0
jug1=int(input('enter size of jug1 :'))
jug2=int(input('enter size of jug2 :'))
req_x=int(input('enter req_x :'))
req_y=int(input('enter req_y :'))
while x!=req_x or y!=req_y:
    n=int(input('rule no:'))
    if n==1:
         x=jug1
         print(x,y)
    elif n==2:
         y=jug2
         print(x,y)
    elif n==3:
         d1=int(input('enter the value :'))
         x=x-d1
         print(x,y)
    elif n==4:
         d2=int(input('enter the value :'))
         y=y-d2
         print(x,y)
    elif n==5:
         x=0
         print(x,y)
    elif n==6:
         y=0
         print(x,y)
    elif n==7:
         y=y-(jug1-x)
         x=jug1
         print(x,y)
    elif n==8:
         x=x-(jug2-y)
         y=jug2
         print(x,y)
    elif n==9:
         x=x+y
         y=0
         print(x,y)
    elif n==10:
         y=x+y
         x=0
         print(x,y)
