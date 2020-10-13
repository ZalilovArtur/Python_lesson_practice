d = int(input())
words = []
error = []
for i in range(d):
    a = input()
    words += [a]
words2 = [x.lower() for x in words]

l = int(input())
note = []
note2 = []
for j in range(l):
    b = input().split()
    note += [b]
    c = [x.lower() for x in b]
    note2 += [c]

for i in range(len(note)):
    for j in range(len(note[i])):
        if note[i][j] not in error:
            if note2[i][j] in words2:
                continue
            if note2[i][j] not in words2:
                error.append(note[i][j])
        else:
            continue

for i in error:
    print(i)




