def is_palindrome(s):
    s = s.lower()
    alphanumeric_s = [c for c in s if c.isalnum()]
    return alphanumeric_s == alphanumeric_s[::-1]

s="a man,a plan ,a canal,panama"

result=is_palindrome(s)
print(result)