symbols = input()
symbols2 = input()
word = input()
cipher = input()
word2 = ''
cipher2 = ''
for i in range(len(word)):
    for j in range(len(symbols)):
        if word[i] == symbols[j]:
            word2 += str(symbols2[j])
for i in range(len(cipher)):
    for j in range(len(symbols2)):
        if cipher[i] == symbols2[j]:
            cipher2 += str(symbols[j])
print(word2)
print(cipher2)