coo = [0,0]
already_pass = [[0,0]]
nb = 1
res = [x for x in open('input.txt','r').read()]

for k in res:
    if k== "<":
        coo = [coo[0]-1,coo[1]]
        if coo not in already_pass:
            nb +=1
        already_pass.append(coo)

    elif k ==">":
        coo = [coo[0]+1,coo[1]]
        if coo not in already_pass:
            nb +=1
        already_pass.append(coo)
        
    elif k=="^":
        coo = [coo[0],coo[1]+1]
        if coo not in already_pass:
            nb +=1
        already_pass.append(coo)

    elif k == "v":
        coo = [coo[0],coo[1]-1]
        if coo not in already_pass:
            nb +=1
        already_pass.append(coo)
print(nb)

#part2
coo_1 = [0,0]
coo_2 = [0,0]
already_pass = [[0,0]]
nb = 1


for k in range(len(res)):
    if k%2 == 0:
        if res[k] == "<":
            coo_1 = [coo_1[0]-1,coo_1[1]]
            if coo_1 not in already_pass:
                nb +=1
            already_pass.append(coo_1)

        elif res[k] ==">":
            coo_1 = [coo_1[0]+1,coo_1[1]]
            if coo_1 not in already_pass:
                nb +=1
            already_pass.append(coo_1)
            
        elif res[k] =="^":
            coo_1 = [coo_1[0],coo_1[1]+1]
            if coo_1 not in already_pass:
                nb +=1
            already_pass.append(coo_1)

        elif res[k] == "v":
            coo_1 = [coo_1[0],coo_1[1]-1]
            if coo_1 not in already_pass:
                nb +=1
            already_pass.append(coo_1)
    else:
        if  res[k]== "<":
            coo_2 = [coo_2[0]-1,coo_2[1]]
            if coo_2 not in already_pass:
                nb +=1
            already_pass.append(coo_2)

        elif res[k] ==">":
            coo_2 = [coo_2[0]+1,coo_2[1]]
            if coo_2 not in already_pass:
                nb +=1
            already_pass.append(coo_2)
            
        elif res[k] =="^":
            coo_2 = [coo_2[0],coo_2[1]+1]
            if coo_2 not in already_pass:
                nb +=1
            already_pass.append(coo_2)

        elif res[k] == "v":
            coo_2 = [coo_2[0],coo_2[1]-1]
            if coo_2 not in already_pass:
                nb +=1
            already_pass.append(coo_2)
print(nb)
