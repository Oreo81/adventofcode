res = [int(x) for x in open('input.txt','r').read().split('\n')]
print(len([x for x in range(len(res)-1) if res[x+1] > res[x]]))
print(len([x for x in range(len(res)-3) if res[x+1]+res[x+2]+res[x+3] > res[x]+res[x+1]+res[x+2]]))