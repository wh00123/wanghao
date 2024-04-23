p = 'ababaaababaa'


def getnext(p, next):
    i = 0
    next[0] = -1
    j = -1
    while i < len(p)-1:
        if j == -1 or p[i] == p[j]:
            i = i+1
            j = j+1
            next[i] = j
        else:
            j = next[j]


next = [-1] * len(p)
getnext(p, next)
print(next)
