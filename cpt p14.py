def longestcommonPrefix(strs):
    if not str:
        return""
    prefix=strs[0]
    for i in range(len(strs)):
         while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strs=["flower","flow","flight"]  
result=longestcommonPrefix(strs)   
print(result)   

    







                 