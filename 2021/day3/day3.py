#Part 1
list_input = [x for x in open('input.txt','r').read().split('\n')]
gamma = ""
epsilon = ""

valeur_find = [0,0]
for bit in range(0,12):
    for bin_in_list in list_input:
        if bin_in_list[bit] == '0': valeur_find[0] += 1
        else: valeur_find[1] += 1
    gamma += str(valeur_find.index(max(valeur_find)))
    epsilon += str(valeur_find.index(min(valeur_find)))
    valeur_find = [0,0]

print('part1:',int(gamma, 2)* int(epsilon, 2))

#----------------------------------------------------------------
#Part 2
list_input = [x for x in open('input.txt','r').read().split('\n')]

def max_in_bin(mlist,index):
    valeur_find = [0,0]
    for k in mlist:
        if k[index] == '0': valeur_find[0] += 1
        else: valeur_find[1] += 1
    if valeur_find[0] == valeur_find[1]: return 2
    else: return valeur_find.index(max(valeur_find))

def test(my_list,oxy_or_co2):
    current = 0
    while len(my_list) > 1:
        new_list = my_list
        my_list = []
        bit = max_in_bin(new_list,current)

        if bit == 2 and oxy_or_co2 == "oxy":
            for bin_in_list in new_list:
                if bin_in_list[current] == '1':
                    my_list.append(bin_in_list)
        
        elif bit != 2 and oxy_or_co2 == 'oxy':
            for k in new_list:
                if k[current] == str(bit):
                    my_list.append(k)

        if bit == 2 and oxy_or_co2 == "co2":
            for bin_in_list in new_list:
                if bin_in_list[current] == '0':
                    my_list.append(bin_in_list)

        elif bit != 2 and oxy_or_co2 == 'co2':
            for k in new_list:
                if k[current] != str(bit):
                    my_list.append(k)
        current += 1
    return my_list

print('part2:',int(test(list_input,'oxy')[0], 2)* int(test(list_input,'co2')[0], 2))

