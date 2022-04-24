fishs = [int(x) for x in open('input.txt','r').read().split(',')]
for day in range(1,257):
    for fish in range(len(fishs)):
        modif = 0
        if fishs[fish] == 0:
            fishs[fish] = 6
            fishs.append(8) 
            modif += 1
        elif fishs[fish] == 8 and modif > 0:
            modif -=1
        else:
            fishs[fish] -= 1


print('part1:',len(fishs))


