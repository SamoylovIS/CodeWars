def rgb(r, g, b):
    a = []
    if r<=0:
        a.append("00")
    elif 0< r <10:
        a.append(f"0{r}")
    elif 10<= r <16:
        a.append(f"{hex(r)[0::1]}")
    elif r>255:
        a.append("FF")
    else:
        c = hex(r)[2:]
        a.append(c.upper())
    if g<=0:
        a.append("00")
    elif 0< g <10:
        a.append(f"0{g}")
    elif 10<= g <16:
        a.append(f"{hex(g)[0::1]}")
    elif g>255:
        a.append("FF")
    else:
        d = hex(g)[2:]
        a.append(d.upper())
    if b<=0:
        a.append("00")
    elif 0< b <10:
        a.append(f"0{b}")
    elif 10<= b <16:
        a.append(f"{hex(b)[0::1]}")
    elif b>255:
        a.append("FF")
    else:
        e = hex(b)[2:]
        a.append(e.upper())
    return "".join(a)