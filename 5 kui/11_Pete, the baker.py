def cakes(recipe, available):
    k = []
    for i in recipe:
        if i not in available.keys():
            return 0
        else:
            k.append(available[i]//recipe[i])
    f = sorted(k)
    return f[0]


a = {'flour': 500, 'sugar': 200, 'eggs': 1}
b = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}

assert cakes(a, b) == 2

#Best way
#def cakes(recipe, available):
#    try:
#        return min([available[a]/recipe[a] for a in recipe])
#    except:
#        return 0