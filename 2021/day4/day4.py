play_number = [x[:-1] for x in open('input.txt','r').readlines(1)][0].split(',')
plateau = [x for x in open('input.txt','r').read().split('\n')]
plateau.pop(0)
new_plateau = [x.split() for x in plateau if x != '']
all_game = [[] for x in range(len(new_plateau)//5)]
marker = [[] for x in range(len(new_plateau)//5)]


current_game = 0
while len(new_plateau) > 0:
    for iop in range(0,5):
        all_game[current_game].append(new_plateau.pop(0))
        marker[current_game].append([False]*5)
    current_game +=1

def add_num(num,list):
    for plateau in range(0,len(list)):
        for ligne in range(0,len(list[plateau])):
            for number in range(0,len(list[plateau][ligne])):
                if str(list[plateau][ligne][number]) == str(num):
                    marker[plateau][ligne][number] = True


def board_is_win(board):
    for line in board:
        if line == [True]*5 :
            return True
    for x in range(5):
        line = []
        for l in board:
            line.append(l[x])
        if line == [True]*5 : return True
        else : line = []
    return False

def print_plateau(plateau):
    for i in plateau :
        for j in i :
            print(j)
        print(plateau)

def somme_non_marked(plateau,marked):
    somme = 0
    for x in range(len(plateau)):
        for y in range(len(plateau[x])):
            if not marked[x][y]:
                somme += int(plateau[x][y])
    return somme

win = False
current = 0 

while win == False:
    num = play_number[current]
    add_num(num,all_game)
    for plateau in marker:
        index_plateau = marker.index(plateau)
        win = board_is_win(plateau)
        if win : break
    current += 1

print(num)
print(int(num)*int(somme_non_marked(all_game[index_plateau],marker[index_plateau])))

# print('-------------------------')

plateau_win = []
# while len(plateau_win) != 100:
#     num = play_number[current]
#     add_num(num,all_game)
#     for plateau in range(len(marker)):
#         win = board_is_win(marker[plateau])
#         if win: 
#             plateau_win.append(all_game[plateau])
#             index_plateau = marker.index(marker[plateau])
#             break

current = 0 
for k in range(100):
    num = play_number[current]
    add_num(num,all_game)
    for plateau in range(len(marker)):
        win = board_is_win(marker[plateau])
        if win: 
            plateau_win.append(all_game[plateau])
            index_plateau = marker.index(marker[plateau])
    if len(plateau_win) == 100:
        winner = plateau_win.pop()
        print(winner)

# print(plateau_win)
print(index_plateau)
print(num)
print(int(num)*int(somme_non_marked(plateau_win[-1],marker[index_plateau])))
# print(int(num)*int(somme_non_marked(plateau_win[-1],)))