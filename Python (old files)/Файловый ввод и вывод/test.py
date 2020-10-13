with open("dataset_3363_2.txt", "r") as f:
    s = f.readline().strip()
rez = ''
bukva = ''
chel  = ''
i = 0
while i < len(s):
    if s[i].isdigit():
        k = i
        while k < len(s) and s[k].isdigit():
            chel += str(s[k])
            k += 1
        i = k
        rez = rez + bukva * int(chel)
        bukva = ''
        chel = ''
    elif s[i].isalpha():
        bukva += str(s[i])
        i += 1
with open("dataset_3363_2.txt", "w") as x:
    m = x.write(rez)


