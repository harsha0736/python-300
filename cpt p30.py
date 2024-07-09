def is_vowel(char):
    return char in 'aeiou'
T = int(input().strip())
for _ in range(T):
    S = input().strip()
    found_happy = False
    for i in range(len(S) - 2):  
        if is_vowel(S[i]) and is_vowel(S[i+1]) and is_vowel(S[i+2]):
            found_happy = True
            break
    if found_happy:
        print("HAPPY")
    else:
        print("SAD")
