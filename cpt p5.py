def romanToInt(s):
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    n = len(s)
    
    for i in range(n):
        if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            result -= roman_to_int[s[i]]
        else:
            result += roman_to_int[s[i]]
    
    return result

roman_numeral = "VII"
print(romanToInt(roman_numeral))