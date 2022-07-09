import string

def is_pangram(s):
    d = []
    for i in s.lower():
        if i in string.ascii_lowercase and i not in d:
            d.append(i)
    if len(d) == 26:
        return True
    return False