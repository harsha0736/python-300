def isPalindrome(x):
    
    if x < 0:
        return False
    
    
    s = str(x)
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

x=121
result=isPalindrome(x)
print(result)
