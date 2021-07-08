import random
import os

class BiomGen:

    def __init__(self, gamePath):
        self.gamePath = gamePath
        self.structursToBiome = {}
        biomes = os.listdir(f"{self.gamePath}/assest/structures")

        for i in range(len(biomes)):
            with open(f"{self.gamePath}/assest/structures/{biomes[i]}/{biomes[i]}.txt", "r") as f:
                structuresTemp = []
                for line in f:
                    tempLineSplit = (line.split(","))
                    tempLineSplit[6] = tempLineSplit[6].split("\n")[0]
                    structuresTemp.append(tempLineSplit + [0])
            self.structursToBiome[biomes[i]] = structuresTemp

    def structurs(self, swiat, biom, worldGen):
        randomSpawn = random.randint(1, 100)
        for i in range(len(self.structursToBiome[biom])):
            biomGen = self.structursToBiome[biom][i]
            if int(biomGen[0]) <= randomSpawn <= int(biomGen[1]):
                worldGen.append([1,biom,swiat,biomGen[2]])

        return worldGen

    def biomGen(self, sz, swiat, biome):
        biomes = {1: self.grass, 2: self.frozen, 3: self.dessert, 4: self.podzol, 5: self.path}
        return biomes[biome](sz, swiat)


    def grass(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(swiat, "grass", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},16")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},14")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},4")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},4")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        return worldGen


    def frozen(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(swiat, "frozen", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},18")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},14")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},12")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},12")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        return worldGen


    def dessert(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(swiat, "dessert", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},3")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},3")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},3")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},4")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        return worldGen


    def podzol(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(swiat, "podzol", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},24")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},14")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},13")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},13")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        return worldGen


    def path(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(swiat, "path", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},17")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},14")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},4")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},4")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        return worldGen