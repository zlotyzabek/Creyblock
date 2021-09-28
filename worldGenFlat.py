import random
import sys
import pickle
import os
import perlin


class New_world:
    def __init__(self):
        self.sizeScreen = 1920, 1080

        self.generateWorldSize = 65536
        self.generateWorldType = "def"


    def biomGenList(self, dlugosc):
        biomList = []
        while len(biomList) <= dlugosc:
            biom = random.randint(1, len(os.listdir(f"assest/structures")))
            for i in range(random.randint(200, 400)):
                biomList.append(biom)

        return biomList

    def generateWorld(self):
        def GenerateTerainGrassland(szerokosc):
            noise = perlin.Perlin(15)
            t = []

            time = [i for i in range(szerokosc)]
            for i in time:
                t.append(int(noise.valueAt(i) * 5))

            return t

        trybGeneratora = self.generateWorldType
        dlugosc = self.generateWorldSize

        if trybGeneratora == "def":
            swiat =  GenerateTerainGrassland(dlugosc)

            biome = self.biomGenList(dlugosc)

            swiatFileToWrite = {}

            def oreAndTreeDiscrybution(swiat):
                swiatFileToWrite[sz] = [0,biome[sz],swiat,0]

            for sz in range(dlugosc):
                oreAndTreeDiscrybution(swiat[sz])

            playerInfo = [int(dlugosc / 2), swiat[int(dlugosc / 2)] + 2, dlugosc, []]
        # SPAWN WORLD SETTER
            try:
                os.makedirs("assest/saves/save")
            except Exception:
                pass

            with open(f'assest/saves/save/worldSave.data', 'wb') as filehandle:
                pickle.dump(swiatFileToWrite, filehandle)

            with open(f'assest/saves/save/playerSave.data', 'wb') as filehandle:
                pickle.dump(playerInfo, filehandle)

gen = New_world()
gen.generateWorld()