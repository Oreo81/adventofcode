#part1 
res = [str(x).split('x') for x in open('input.txt','r').read().split('\n')]
current = 0
for k in res:
    a = int(k[0])*int(k[1])
    b =int(k[1])*int(k[2])
    c = int(k[0])*int(k[2])
    cal = 2*a + 2*b + 2*c
    current += cal + min(a,b,c)

print(current)

#part2 

current = 0
for k in res:
    order = [int(k[0]),int(k[1]),int(k[2])]
    order.sort()


    cal = order[0]+order[0]+order[1]+order[1]
    ruban = int(k[0])*int(k[1])*int(k[2])
    current += cal +ruban

print(current)