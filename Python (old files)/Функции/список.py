l = [1,2,3,4,5,6]
g = [1,2,3,4,5,6]
h = [1,2,3,4,5,6]

def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            l[i] //= 2
            i += 1
        else:
            del (l[i])
    return l
print(modify_list(l))

def modify_list2(g):
    x = [int(i // 2) for i in g if i % 2 == 0]
    g = x
    return g
print(modify_list2(g))

def modify_list3(h):
    x = []
    for i in h:
        if i % 2 == 0:
            i //= 2
            x.append(i)
        else:
            continue
    return x
print(modify_list3(h))
