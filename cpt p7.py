def length_of_last_word(s):
    s = s.strip()
    last_space_index = s.rfind(' ')
    if last_space_index == -1:
        return len(s)
    else:
        return len(s) - last_space_index - 1


s="hello NRIIT CSE"
result= length_of_last_word(s)
print(result)

