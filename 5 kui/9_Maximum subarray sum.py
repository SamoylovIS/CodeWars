def max_sequence(arr):
    max = 0
    iter = 0
    for i in arr:
        iter+=i
        if iter<0:
            iter=0
        if iter>max:
            max=iter
    return max