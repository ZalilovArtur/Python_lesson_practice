n = int(input())
coordinate = [int(i) for i in [0,0]]
for i in range(n):
    a = input().split()
    if a[0] == 'север':
        coordinate[1] += int(a[1])
    if a[0] == 'юг':
        coordinate[1] -= int(a[1])
    if a[0] == 'запад':
        coordinate[0] -= int(a[1])
    if a[0] == 'восток':
        coordinate[0] += int(a[1])
print(coordinate[0],coordinate[1])
