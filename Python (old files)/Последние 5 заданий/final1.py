n = int(input())
end = []
massive = ['' for i in range(n)]
for i in range(n):
    massive[i] = input().split(";")
for i in range(n):
    for j in range(4):
        if (massive[i][j] in end) or (massive[i][j].isdigit()):
            continue
        else:
            team = massive[i][j]
            win = 0
            draw = 0
            game = 0
            over = 0
            for i2 in range(n):
                for j2 in range(4):
                    if massive[i2][j2] == team:
                        if ((massive[i2][j2+1] == massive[i2][1]) and (massive[i2][1] > massive[i2][3])) \
                                or ((massive[i2][j2+1] == massive[i2][3]) and (massive[i2][j2+1] > massive[i2][1])):
                            win += 1
                        if ((massive[i2][j2+1] == massive[i2][1]) and (massive[i2][1] < massive[i2][3])) \
                                or ((massive[i2][j2+1] == massive[i2][3]) and (massive[i2][j2+1] < massive[i2][1])):
                            over += 1
                        if massive[i2][1] == massive[i2][3]:
                            draw += 1
                        game += 1
                    else:
                        continue
            print(str(team)+":"+str(game)+" "+str(win)+" "+str(draw)+" "+str(over)+" "+str(win*3+draw))
            end.append(team)





