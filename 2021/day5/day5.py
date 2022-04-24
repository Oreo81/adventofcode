bombe_placement = [x.split(' -> ') for x in open('input.txt','r').read().split('\n')]
for k in bombe_placement:
    k[0] = k[0].split(',')
    k[1] = k[1].split(',')

tableau = [[] for x in range(1000)]
for x in tableau:
    for k in range(1000):
        x.append([0])


#exemple entré list: [['5', '9'],['0', '9']]
def two_point_to_line(list):
    list_of_point =[]
    x1 = int(list[0][0])
    y1 = int(list[0][1])
    x2 = int(list[1][0])
    y2 = int(list[1][1])

    print(abs(x1-x2),abs(y1-y2))

    if x1 == x2:
        if y1 > y2:
            list_of_point.append([x1,y1])
            current = [x1,y1]
            for add in range(y1-y2):
                current[1] -= 1
                list_of_point.append([x1,current[1]])
            return list_of_point
        else:
            list_of_point.append([x1,y1])
            current = [x1,y1]
            for add in range(y2-y1):
                current[1] += 1
                list_of_point.append([x1,current[1]])
            return list_of_point
    elif y1 == y2:
        if x1 > x2:
            list_of_point.append([x1,y1])
            current = [x1,y1]
            for add in range(x1-x2):
                current[0] -= 1
                list_of_point.append([current[0],y1])
            return list_of_point
        else:
            list_of_point.append([x1,y1])
            current = [x1,y1]
            for add in range(x2-x1):
                current[0] += 1
                list_of_point.append([current[0],y1])
            return list_of_point

    elif abs(x1-x2) == abs(y1-y2):
        if x1 > x2 and y1 > y2:
            list_of_point.append([x1,y1])
            current = [x1,y1]
            for add in range(abs(x1-x2)):
                current[0] -= 1
                current[1] -= 1
                list_of_point.append([current[0],current[1]])
            return list_of_point

        elif x1 > x2 and y1 < y2:
            list_of_point.append([x1,y1])
            current = [x1,y1]
            for add in range(abs(x1-x2)):
                current[0] -= 1
                current[1] += 1
                list_of_point.append([current[0],current[1]])
            return list_of_point
        elif x1 < x2 and y1 > y2:
            list_of_point.append([x1,y1])
            current = [x1,y1]
            for add in range(abs(x1-x2)):
                current[0] += 1
                current[1] -= 1
                list_of_point.append([current[0],current[1]])
            return list_of_point
        elif x1 < x2 and y1 < y2:
            list_of_point.append([x1,y1])
            current = [x1,y1]
            for add in range(abs(x1-x2)):
                current[0] += 1
                current[1] += 1
                list_of_point.append([current[0],current[1]])
            return list_of_point

    else:
        return list_of_point


def place_point(tableau,list_point):
    line = []
    for point in list_point:
        if two_point_to_line(point) != []:
            line.append(two_point_to_line(point))
    for lines in line:
        for point in lines:
            tableau[point[0]][point[1]][0] +=1 
        print(lines)
    return tableau

def calcul_nb_more_1(tableau):
    nb_more_1 = 0
    for lines in tableau:
        for point in lines:
            if point[0] > 1:
                nb_more_1 += 1
    return nb_more_1

print(calcul_nb_more_1(place_point(tableau ,bombe_placement)))