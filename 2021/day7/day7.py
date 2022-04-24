mouvements = [int(x) for x in open('input.txt','r').read().split(',')]

def part1(list):
    cout = []
    for alligenement in range(len(list)):
        nb = 0
        for mouve in list:
            nb += abs(mouve - alligenement)
        cout.append(nb)
    return min(cout)

def part2(list):
    cout = []
    for alligenement in range(len(list)):
        nb = 0
        for mouve in list:
            nb += somme_conse(abs(mouve - alligenement))
        cout.append(nb)
    return min(cout)

def somme_conse(n):
    somme = 0
    for i in range(1, n+1):
       somme=somme+i
    return somme

print("Part 1:",part1(mouvements))
print("Part 2:",part2(mouvements))
