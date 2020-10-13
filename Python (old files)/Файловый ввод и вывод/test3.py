with open('dataset_3363_4.txt','r') as x:
    s = x.read().replace("\n",",").split(",")
book = []
math = 0
fiz = 0
rus = 0
j = 0
for i in range(len(s)-1):
    book += s[i].split(";")
    arfm = (int(book[1]) + int(book[2]) + int(book[3])) / 3
    with open('data.txt', 'a') as y:
        y.write(str(arfm) + '\n')
    math += int(book[1])
    fiz += int(book[2])
    rus += int(book[3])
    book = []
    j += 1
math /= j
fiz /= j
rus /= j
r = open('data.txt', 'a')
r.write(str(math)+' '+str(fiz)+' '+str(rus))

