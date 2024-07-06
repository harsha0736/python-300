def repeatedSubstringPattern(s: str) -> bool:
    n = len(s)
    
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            substr = s[:length]
            if substr * (n // length) == s:
                return True
    
    return False

s="saisai"
result=repeatedSubstringPattern(s)
print(result)