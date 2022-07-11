import collections as col

def anagrams(word, words):
    a = []
    cnt = col.Counter()
    for i in word:
        cnt[i] += 1
    sr = col.Counter()
    for i in words:
        for j in i:
            sr[j]+=1
        if sorted(cnt) == sorted(sr) and len(word) == len(i):
            a.append(i)
            sr.clear()
        if sorted(cnt) != sorted(sr) or len(word) != len(i):
            sr.clear()
    return print(a)

#Best_way
#def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]