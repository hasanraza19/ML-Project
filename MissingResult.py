filepath = "C:/users/hasan/desktop/data/Dataset1.txt"
filewrite = "C:/users/hasan/desktop/Dataset1.txt"

file= open(filepath, 'r')
listoflines = []

for i in file:
    words = i.split()
    listy = []
    for j in words:
        listy.append(j.strip())
    listoflines.append(listy)

#print(str(len(listoflines)))
#print(str(len(listoflines[0])))
# print(listoflines[4][6])


def eucDist(a, b):
    distance = 0
    for i in range(len(a)):
        m = a[i]
        n = b[i]
        if float(m) == float(1.00000000000000e+99):
            m = 0
        if float(n) == float(1.00000000000000e+99):
            n = 0

        z = float(m) - float(n)
        z = z**2
        distance = distance + z
    return (distance ** 0.5)



#print("YEAH: " + str(eucDist([1,0,3], ["1.00000000000000e+99",2,3])))

for i in range(len(listoflines)):
    for j in range(len(listoflines[i])):
        if float(listoflines[i][j]) == float(1.00000000000000e+99):
            distances = []
            for x in range(len(listoflines)):
                distances.append (float(eucDist(listoflines[i], listoflines[x])))

            distances = sorted(distances)

            iterator = 1


            while float(listoflines[i][j]) == float(1.00000000000000e+99):
                index = 0
                currentdist = distances[iterator]
                for mm in range(len(distances)):
                    if currentdist == distances[mm]:
                        index = mm

                listoflines[i][j] = listoflines[index][j]
                #print(str(listoflines[index][j]))
                iterator = iterator + 1
                #print("reached!")

with open(filewrite, 'w') as f:
    for i in range(len(listoflines)):
        for j in range(len(listoflines[i])):
            f.write(listoflines[i][j] + "\t")
        f.write("\n")


