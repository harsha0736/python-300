from collections import Counter
def anagram(s,t):
    if len(s)!=len(t):
        return False
    return Counter(s)==Counter(t)
s="harsha"
t="hahasr"
result=anagram(s,t)
print(result)    