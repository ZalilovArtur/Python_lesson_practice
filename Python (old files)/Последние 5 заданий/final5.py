with open("dataset_3380_5.txt") as f:
    p = []
    for l in f:
        p.append(l.strip('\n').split('\t'))
b = {"1":[int(0),int(0)],"2":[int(0),int(0)],"3":[int(0),int(0)],"4":[int(0),int(0)],"5":[int(0),int(0)],
     "6":[int(0),int(0)],"7":[int(0),int(0)],"8":[int(0),int(0)],"9":[int(0),int(0)],"10":[int(0),int(0)],"11":[int(0),int(0)]}
for i in range(len(p)):
    for j in range(len(p[i])):
        if p[i][j].isdigit() and p[i][j] == p[i][0]:
            klacc = p[i][j]
            b[str(klacc)][0] += int(1)
            b[str(klacc)][1] += int(p[i][j+2])
        else:
            continue
with open("test.txt","a") as x:
    k = list(b.keys())
    for key in k:
        if b[key][0] == 0:
            x1 = str(key)+" -"
            x.write(str(x1) + '\n')
        else:
            x2 = str(key)+" "+str(b[key][1] / b[key][0])
            x.write(str(x2) + '\n')