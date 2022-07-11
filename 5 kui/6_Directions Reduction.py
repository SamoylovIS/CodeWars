def dirReduc(arr):
    geo = {'NORTH': 'SOUTH',
           'SOUTH': 'NORTH',
           'WEST': 'EAST',
           'EAST': 'WEST'}
    way = []
    for i in arr:
        if way and way[-1] == geo[i]:
            way.pop()
        else:
            way.append(i)
    return way