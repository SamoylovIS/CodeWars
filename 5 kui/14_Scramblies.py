#def scramble(s1, s2):
#    for i in set(s2):
#        if s2.count(i) <= s1.count(i):
#            continue
#        return False
#    return True

def scramble(s1, s2):
    b = [char for char in s1]
    a = [char for char in s2]
    k = []
    for i in a:
        if i in b:
            k.append(i)
            b.remove(i)
    return print(len(a)==len(k))


s1 = 'katas'
s2 = 'steak'

scramble(s1, s2)