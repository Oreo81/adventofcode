para =  open('input.txt','r').read()
floor = 0
for x in range(len(para)):
    if para[x] == "(":
        floor +=1
    else:
        floor -=1

    if floor == -1:
        print(x+1)
print(floor)