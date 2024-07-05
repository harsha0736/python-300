def strStr(haystack,needle):
    if needle=="":
        return 0
    if needle not in haystack:
        return -1
    return haystack.index(needle)

haystack="pythoncodeing"
needle="a"
result=strStr(haystack,needle)
print(result)
