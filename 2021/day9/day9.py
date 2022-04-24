emplacement = [x for x in open('input.txt','r').read().split('\n')]
print(emplacement)

final = []
for nb_element in range(len(emplacement)+2):
    final.append([])

print(final)


for add_num in range(1,len(emplacement)):
    final[add_num].append('A')
    for add_num_encore in emplacement:
        final[add_num].append(add_num_encore)
    final[add_num].append('A')

print(final)
# liis = [[]]
# for ll in len(emplacement):
#     for k in emplacement:
#         liis[ll].append('A')
#         for nb in k:
#             liis[ll].append(nb)
#         liis[ll].append('A')
#     liis.append([])

# print(liis)