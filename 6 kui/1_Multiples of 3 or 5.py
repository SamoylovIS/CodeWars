def solution(number):
    b = []
    for i in range(1,number):
        if i % 3 == 0 or i % 5 == 0:
            b.append(i)
    return (sum(b))