def solution(args):
    a = []
    inst,k = args[0],args[0]
    for i in args[1:] + [""]:
        if i!= k +1:
            if k == inst:
                a.append( str(inst) )
            elif k == inst + 1:
                a.extend( [str(inst), str(k)] )
            else:
                a.append( str(inst) + "-" + str(k) )
            inst = i
        k = i
    return ",".join(a)