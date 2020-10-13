import collections
with open("dataset_3363_3.txt","r") as x:
    s = x.read().replace("\n"," ").lower().split()
h = collections.Counter()
for i in s:
    h[i] += 1
with open("dataset_3363_3.txt","w") as y:
    key = list(h.keys())
    value = list(h.values())
    max_key = key[value.index(max(value))]
    max_value = max(value)
    n = y.write(str(max_key)+" "+str(max_value))
