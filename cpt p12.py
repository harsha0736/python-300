def strStr(haystack,needle):
    if needle=="":
        return 0
    if needle not in haystack:
        return -1
    return haystack.index(needle)

haystack=input("enter the string:")
needle=input("enter the element of the string:")
result=strStr(haystack,needle)
print(result)
