import random

t = [0]


def ifRandomRSet(n, r1, r2):
    if t[-1] == n:
        return random.randrange(r1, r2)
    else:
        return None


def GenerateTerainGrassland(szerokosc):
    r = 0
    for i in range(szerokosc):

        r = ifRandomRSet(0, 0, 2)
        if r is not None:
            t.append(r)

        r = ifRandomRSet(1, 0, 3)
        if r is not None:
            t.append(r)

        r = ifRandomRSet(2, 1, 4)
        if r is not None:
            t.append(r)

        r = ifRandomRSet(3, 2, 5)
        if r is not None:
            t.append(r)

        r = ifRandomRSet(4, 3, 4)
        if r is not None:
            t.append(r)

    return t

def worldStructureSpawning(szerokosc):
    worldStructureSpawningList = []
    for i in range(szerokosc):
        ifTreeSpawn = random.randint(1,2)
        ifOreSpawn = random.randint(1,3)
        randomSpawn = random.randint(1,150)
        try:
            if 0 <= randomSpawn <= 75  and worldStructureSpawningList[i-1] == 0 and ifTreeSpawn == 1:
                worldStructureSpawningList.append(1)
            elif 76 <= randomSpawn <= 89 and ifOreSpawn == 1:
                worldStructureSpawningList.append(2)
            elif 90 <= randomSpawn <= 97 and ifOreSpawn == 1:
                worldStructureSpawningList.append(3)
            elif 98 <= randomSpawn <= 100 and ifOreSpawn == 1:
                worldStructureSpawningList.append(4)
            else:
                worldStructureSpawningList.append(0)
        except Exception:
            worldStructureSpawningList.append(0)

    return worldStructureSpawningList

def structurListEditor(list, szer, wys, rep, torep):
   return str(list[szer][wys])[::-1].replace(rep[::-1] + ",", torep[::-1] + ",", 1)[::-1]

print("Generator Świata")
print("Wybierz tryb generowania świata flat/def")
trybGeneratora = input("--> ")
if trybGeneratora == "flat":
    print("Wpisz na ile kratek ma być świat(Szerokosć)")
    dlugosc = int(input("->"))

    def swiat0(sz):
        for i in range(35 * 96, -96, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{696 - i},0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 69 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    swiatFileToWrite = []

    for sz in range(dlugosc):
        swiatFileToWrite.append([])
        swiat0(sz)

    saveTemp = []

    for szerokosc in range(dlugosc):
        for wysokosc in range(96):
            saveTemp.append(swiatFileToWrite[szerokosc][wysokosc])

    f = open("assest/saves/save.mov", "w")

    f.writelines(saveTemp)

elif trybGeneratora == "def":
    print("Wpisz na ile kratek ma być świat(Szerokosćcc)")
    dlugosc = int(input("->"))

    swiat = GenerateTerainGrassland(dlugosc)

    swiatFileToWrite = []

    worldStructureSpawningList = worldStructureSpawning(dlugosc)

    def swiat0(sz):
        for i in range(34 * 96, 0, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{696 - i},0\n")
        if worldStructureSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},696,4\n")
        elif worldStructureSpawningList[sz] == 2:
            swiatFileToWrite[sz].append(f"{sz * 96},696,coalGen\n")
        elif worldStructureSpawningList[sz] == 3:
            swiatFileToWrite[sz].append(f"{sz * 96},696,ironGen\n")
        elif worldStructureSpawningList[sz] == 4:
            swiatFileToWrite[sz].append(f"{sz * 96},696,diamondGen\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},696,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 57 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    def swiat1(sz):
        for i in range(33 * 96, 0, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{600 - i},0\n")
        if worldStructureSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},600,4\n")
        elif worldStructureSpawningList[sz] == 2:
            swiatFileToWrite[sz].append(f"{sz * 96},600,coalGen\n")
        elif worldStructureSpawningList[sz] == 3:
            swiatFileToWrite[sz].append(f"{sz * 96},600,ironGen\n")
        elif worldStructureSpawningList[sz] == 4:
            swiatFileToWrite[sz].append(f"{sz * 96},600,diamondGen\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},600,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},696,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 57 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    def swiat2(sz):
        for i in range(32 * 96, 0, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{504 - i},0\n")
        if worldStructureSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},504,4\n")
        elif worldStructureSpawningList[sz] == 2:
            swiatFileToWrite[sz].append(f"{sz * 96},504,coalGen\n")
        elif worldStructureSpawningList[sz] == 3:
            swiatFileToWrite[sz].append(f"{sz * 96},504,ironGen\n")
        elif worldStructureSpawningList[sz] == 4:
            swiatFileToWrite[sz].append(f"{sz * 96},504,diamondGen\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},504,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},600,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},696,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 57 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    def swiat3(sz):
        for i in range(31 * 96, 0, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{408 - i},0\n")
        if worldStructureSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},408,4\n")
        elif worldStructureSpawningList[sz] == 2:
            swiatFileToWrite[sz].append(f"{sz * 96},408,coalGen\n")
        elif worldStructureSpawningList[sz] == 3:
            swiatFileToWrite[sz].append(f"{sz * 96},408,ironGen\n")
        elif worldStructureSpawningList[sz] == 4:
            swiatFileToWrite[sz].append(f"{sz * 96},408,diamondGen\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},408,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},504,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},600,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},696,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 57 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    def swiat4(sz):
        for i in range(30 * 96, 0, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{312 - i},0\n")
        if worldStructureSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},312,4\n")
        elif worldStructureSpawningList[sz] == 2:
            swiatFileToWrite[sz].append(f"{sz * 96},312,coalGen\n")
        elif worldStructureSpawningList[sz] == 3:
            swiatFileToWrite[sz].append(f"{sz * 96},312,ironGen\n")
        elif worldStructureSpawningList[sz] == 4:
            swiatFileToWrite[sz].append(f"{sz * 96},312,diamondGen\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},312,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},408,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},504,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},600,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},696,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 57 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    swiatGenSetting = {0: swiat0, 1: swiat1, 2: swiat2, 3: swiat3, 4: swiat4}

    for sz in range(dlugosc):
        swiatFileToWrite.append([])
        swiatGenSetting[swiat[sz]](sz)

    saveTemp = []

    for szerokosc in range(dlugosc):
        for wysokosc in range(96):
            if swiatFileToWrite[szerokosc][wysokosc].split(",")[2].split("\n")[0] == "4":
                treeSize = random.randint(1, 5)
                with open(f"assest/structures/trees/size{treeSize}.txt", "r") as f:
                    for line in f:
                        tempLineSplit = (line.split(","))
                        tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                        try:
                            swiatFileToWrite[szerokosc + int(tempLineSplit[0])][wysokosc + int(tempLineSplit[1])] = \
                            structurListEditor(swiatFileToWrite, szerokosc + int(tempLineSplit[0]), wysokosc + int(tempLineSplit[1]), tempLineSplit[2], tempLineSplit[3].split("\n")[0])
                        except Exception:
                            pass

        for wysokosc in range(96):
            if swiatFileToWrite[szerokosc][wysokosc].split(",")[2].split("\n")[0] == "coalGen":
                coalSize = random.randint(1, 4)
                coalDown = random.randint(10, 50)
                with open(f"assest/structures/ores/coalSize{coalSize}.txt", "r") as f:
                    swiatFileToWrite[szerokosc][wysokosc] = \
                        structurListEditor(swiatFileToWrite, szerokosc, wysokosc, "coalGen", "0,")
                    for line in f:
                        tempLineSplit = (line.split(","))
                        tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                        try:
                            swiatFileToWrite[szerokosc + int(tempLineSplit[0])][wysokosc + int(tempLineSplit[1]) + coalDown] = \
                            structurListEditor(swiatFileToWrite, szerokosc + int(tempLineSplit[0]), wysokosc + int(tempLineSplit[1]) + coalDown, tempLineSplit[2], tempLineSplit[3])

                        except Exception:
                            pass

            elif swiatFileToWrite[szerokosc][wysokosc].split(",")[2].split("\n")[0] == "ironGen":
                ironSize = random.randint(1, 3)
                ironDown = random.randint(10, 50)
                with open(f"assest/structures/ores/ironSize{ironSize}.txt", "r") as f:
                    swiatFileToWrite[szerokosc][wysokosc] = \
                        structurListEditor(swiatFileToWrite, szerokosc, wysokosc, "ironGen", "0,")
                    for line in f:
                        tempLineSplit = (line.split(","))
                        tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                        try:
                            swiatFileToWrite[szerokosc + int(tempLineSplit[0])][wysokosc + int(tempLineSplit[1]) + ironDown] = \
                            structurListEditor(swiatFileToWrite, szerokosc + int(tempLineSplit[0]), wysokosc + int(tempLineSplit[1]) + ironDown, tempLineSplit[2], tempLineSplit[3])

                        except Exception:
                            pass

            elif swiatFileToWrite[szerokosc][wysokosc].split(",")[2].split("\n")[0] == "diamondGen":
                diamondSize = random.randint(1, 2)
                diamondDown = random.randint(10, 50)
                with open(f"assest/structures/ores/diamondSize{diamondSize}.txt", "r") as f:
                    swiatFileToWrite[szerokosc][wysokosc] = \
                        structurListEditor(swiatFileToWrite, szerokosc, wysokosc, "diamond", "0,")
                    for line in f:
                        tempLineSplit = (line.split(","))
                        tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                        try:
                            swiatFileToWrite[szerokosc + int(tempLineSplit[0])][wysokosc + int(tempLineSplit[1]) + diamondDown] = \
                            structurListEditor(swiatFileToWrite, szerokosc + int(tempLineSplit[0]), wysokosc + int(tempLineSplit[1]) + diamondDown, tempLineSplit[2], tempLineSplit[3])

                        except Exception:
                            pass


# SPAWN WORLD SETTER
    f = open("assest/saves/save.mov", "w")

    f.write(f"{dlugosc * 48},600\n")

    for szerokosc in range(dlugosc):
        for wysokosc in range(96):
            saveTemp.append(swiatFileToWrite[szerokosc][wysokosc])

    f.write("0,0\n")
    f.write("0,0\n")
    f.writelines(saveTemp)