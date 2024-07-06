def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack:
                return False
            top_element = stack.pop()
            if mapping[char] != top_element:
                return False
        else:
            return False
    
    return len(stack) == 0


s={}
result=isValid(s)
print(result)
