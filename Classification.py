filepath = "C:/users/hasan/desktop/data/TrainData1.txt"
labelfilepath = "C:/users/hasan/desktop/data/TrainLabel1.txt"
testdatapath = "C:/users/hasan/desktop/data/TestData1.txt"
filewrite = "C:/users/hasan/desktop/RazaClassification1.txt"
file= open(filepath, 'r')
file2= open(labelfilepath, 'r')
file3= open(testdatapath, 'r')
listoflines = []
listofclasses = []


def maxClass(x):
    max = float(x[0])
    for i in range(0,len(x)):
        if float(x[i]) > max:
            max = float(x[i])

    for i in range(0, len(x)):
        if float(x[i]) == max:
            return i + 1


def findStdev(x, y):
    if(len(x) <= 1):
        return 1 #FIX THIS
    sum = 0.0
    listo = []
    for i in range(0,len(x)):
        neg = x[i] - y
        neg = neg**2
        listo.append(neg)
    q = findMean(listo)
    return q ** 0.5


def findMean(x):
    sum = 0.0
    for i in range(0,len(x)):
        sum = sum + x[i]
    return sum / (len(x) - 1 )


import math
def probability(x, u, s):
    exp = math.exp(-(math.pow((x-u), 2) / (2 * math.pow(s, 2))))
    a = (1 / (math.sqrt(2 * math.pi) * s)) * exp
    return a





for i in file:
    words = i.split("\t")
    listy = []
    for j in words:
        listy.append(j.strip())
    listoflines.append(listy)

for i in file2:
    listofclasses.append(i.strip())

listofmeans = []
index = 0

for i in range(0, len(listoflines[0])):
    sum = 0.0
    correction = 0
    for j in range(0, len(listoflines)):

        if float(listoflines[j][i]) != float(1.00000000000000e+99):
            sum = sum + float(listoflines[j][i])
        else:
            correction = correction+1

    avg = sum/(len(listoflines) - correction)
    listofmeans.append(avg)


for i in range(len(listoflines)):
    for j in range(len(listoflines[i])):
        if float(listoflines[i][j]) == float(1.00000000000000e+99):
            listoflines[i][j] = listofmeans[j]

print("There are " + str(len(listoflines[0])) + " attributes")

# print("TESTO   " + str(listoflines[3][3]))

setofclasses = set()
for i in listofclasses:
    setofclasses.add(i.strip())
numofclasses = (len(setofclasses))
print(len(setofclasses))



classsep = []

for i in range(1,numofclasses+1):
    classsep.append([])
    for j in range(0, len(listoflines)):
        if i == float(listofclasses[j]):
            classsep[i-1].append(listoflines[j])

# print("number of thing:" + str(len(classsep)))
# print("number of thing:" + str(len(classsep[0])))
# print("number of thing:" + str(len(classsep[1])))

arrayofinf = []

for p in range(0,len(classsep)):
    arrayofinf.append([])
    for i in range(0, len(listoflines[0])):
        sum = 0.0
        for j in range(0, len(classsep[p])):
            sum = sum + float(classsep[p][j][i])

#        avg = sum / len(classsep[p])
        arrayofinf[p].append(avg)


# print(arrayofinf[0][0])



arrayofinf2 = []

for p in range(0,len(classsep)):
    arrayofinf2.append([])
    for i in range(0, len(listoflines[0])):
        listo = []
        sum = 0.0
        for j in range(0, len(classsep[p])):
            listo.append(float(classsep[p][j][i]))

        stdev = findStdev(listo,arrayofinf[p][i])
        arrayofinf2[p].append(stdev)



# print(arrayofinf2[1][3])



testdata = []

for i in file3:
    words = i.split("\t")
    listy = []
    for j in words:
        listy.append(j)
    testdata.append(listy)


listofpredictions = []

for i in range(0,len(testdata)):
    listq = []
    for j in range(0,numofclasses):


        prob = 1
        for k in range(0,len(testdata[0])):
            prob = prob * probability(float(testdata[i][k]), float(arrayofinf[j][k]), float(arrayofinf2[j][k]))
        listq.append(prob)
    listofpredictions.append(listq)


# print(listofpredictions[0][1])
print("CLASSIFIED: ")
listofclass = []

for i in range(0,len(listofpredictions)):
    listofclass.append(maxClass(listofpredictions[i]))

for i in range(len(listofclass)):
    print (listofclass[i])


with open(filewrite, 'w') as f:
    for i in range(len(listofclass)):
        f.write(str(listofclass[i])+"\n")



# for x in listoflines:
#     count = 0
#     for y in listoflines[count]:
#         print(y)
#         count = count + 1


# print(file.read())
# for i in file:
#     words = i.split("\t")
#     count = 0
#     for j in words:
#         count = count + 1
#     print(count)

