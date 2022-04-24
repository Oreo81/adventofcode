post =[0,0] #horizon / vertical
res = [x for x in open('input.txt','r').read().split('\n')]
for k in res:
    val = int(k[len(k)-1])
    if k[0] == 'f':
        post = [post[0]+val,post[1]]
    elif k[0] == 'd':
        post  = [post[0],post[1]+val]
    elif k[0] == 'u':
        post  = [post[0],post[1]-val]

print("Part1:",post,"resultat:",post[0]*post[1])

#-----------------------------------------------

post_2 =[0,0,0] #horizon / vertical / visé
res = [x for x in open('input.txt','r').read().split('\n')]
for k in res:
    val_2 = int(k[len(k)-1])
    if k[0] == 'f' :
        post_2 = [post_2[0]+val_2,post_2[1]+ post_2[2]*val_2,post_2[2]]
    elif k[0] == 'd':
        post_2  = [post_2[0],post_2[1],post_2[2]+val_2]
    elif k[0] == 'u':
        post_2  = [post_2[0],post_2[1],post_2[2]-val_2]

print("Part2:",post_2,"resultat:",post_2[0]*post_2[1])
