#Part 1: Procedural
print("> Day 1 - 2020 product")
f = open("expenses.csv", "r")
entries = f.read()
entriesList = entries.split(";")
for i in range(0,len(entriesList)):
    for j in range(i,len(entriesList)):
        if int(entriesList[i]) + int(entriesList[j])  == 2020:
            print("entrato")
            print(int(entriesList[i])*int(entriesList[j]))

#Part 2: Procedural
print("> Day 1 - 2020 product")
f = open("expenses.csv", "r")
entries = f.read()
entriesList = entries.split(";")
for i in range(0,len(entriesList)):
    for j in range(i,len(entriesList)):
        for k in range(j,len(entriesList)):
            if int(entriesList[i]) + int(entriesList[j]) + int(entriesList[k]) == 2020:
                print("entrato")
                print(int(entriesList[i])*int(entriesList[j])*int(entriesList[k]))


#Level 2: functional
