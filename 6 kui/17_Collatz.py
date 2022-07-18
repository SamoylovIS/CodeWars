def collatz(n):
    a = []
    a.append(f"{n}")
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            a.append(f"{int(n)}")
        else:
            if n % 2 == 1:
                n = (3 * n) + 1
                a.append(f"{int(n)}")
    return "->".join(a)