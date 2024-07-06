def addStrings(num1: str, num2: str) -> str:
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        sum_digits = digit1 + digit2 + carry
        result.append(str(sum_digits % 10))
        carry = sum_digits // 10
        
        i -= 1
        j -= 1
    
    return ''.join(result[::-1])

num1="111"
num2="22"
result=addStrings(num1: str, num2: str)
print(result)