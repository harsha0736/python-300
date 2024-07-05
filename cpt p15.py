def powof2(n):
    if n<=0:
        return False
    i=0
    while 2**i<=n:
        if 2**i==n:
            return True
        i+=1
    return False

n=int(input("enter your number:"))
result=powof2(n)
print(result)   