import random

class biomGen:

    def __init__(self, gamePath):
        self.gamePath = gamePath
        self.structursToBiome = {}
        biomes = ["grass", "frozen", "dessert", "podzol", "path"]

        for i in range(len(biomes)):
            with open(f"{self.gamePath}/assest/structures/structurGenWorld/{biomes[i]}.txt", "r") as f:
                structures = []
                for line in f:
                    tempLineSplit = (line.split(","))
                    tempLineSplit[2] = tempLineSplit[2].split("\n")[0]
                    structures.append([int(tempLineSplit[0]), int(tempLineSplit[1]), tempLineSplit[2]])
            self.structursToBiome[biomes[i]] = structures

    def structurs(self, sz, swiat, biom, worldGen):
        randomSpawn = random.randint(1, 100)
        for i in range(len(self.structursToBiome[biom])):
            biomGen = self.structursToBiome[biom][i]
            if biomGen[0] <= randomSpawn <= biomGen[1]:
                worldGen.append([1,biom,swiat,biomGen[2]])

        return worldGen

    def biomGen(self, sz, swiat, biome):
        biomes = {1: self.grass, 2: self.frozen, 3: self.dessert, 4: self.podzol, 5: self.path}
        return biomes[biome](sz, swiat)


    def grass(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(sz, swiat, "grass", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},16")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},14")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},4")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},4")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        #worldGen.append(f"{sz * 96},{6552},bedrock")
        return worldGen


    def frozen(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(sz, swiat, "grass", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},18")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},14")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},12")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},12")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        #worldGen.append(f"{sz * 96},{6552},bedrock")
        return worldGen


    def dessert(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(sz, swiat, "grass", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},3")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},3")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},3")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},4")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        #worldGen.append(f"{sz * 96},{6552},bedrock")
        return worldGen


    def podzol(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(sz, swiat, "grass", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},24")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},14")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},13")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},13")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        #worldGen.append(f"{sz * 96},{6552},bedrock")
        return worldGen


    def path(self, sz, swiat):
        worldGen = []
        worldGen = self.structurs(sz, swiat, "grass", worldGen)
        for i in range((34 - swiat) * 96, -96, -96):
            worldGen.append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")
        worldGen.append(f"{sz * 96},{792 - (swiat * 96)},17")
        worldGen.append(f"{sz * 96},{888 - (swiat * 96)},14")
        worldGen.append(f"{sz * 96},{984 - (swiat * 96)},4")
        worldGen.append(f"{sz * 96},{1080 - (swiat * 96)},4")
        for i in range((57 + swiat)):
            worldGen.append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")
        #worldGen.append(f"{sz * 96},{6552},bedrock")
        return worldGen