def order_weight(strng):
    a = []
    k = strng.split()
    for i in k:
        count_i = sum(list(map(int, str(i))))
        a.append([count_i, i])
    a.sort()
    return ' '.join([i[1] for i in a])
