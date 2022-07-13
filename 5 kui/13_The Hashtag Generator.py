def generate_hashtag(s):
    if len(s) == 0:
        return False
    a = []
    for i in s.split():
        a.append(i.capitalize())
    k = f"""#{"".join(a)}"""
    if len(k) > 140:
        return False
    else:
        return k

s = " Hello there thanks for trying my Kata"
generate_hashtag(s)
