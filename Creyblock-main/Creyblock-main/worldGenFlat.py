import random
import sys
import pygame
from pygame.locals import *
import main
import pickle
import os


class new_World():
    def __init__(self):
        pygame.init()

        self.sizeScreen = 1920, 1080
        self.screenReal = pygame.display.set_mode((1920, 1080), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.screenReal.copy()
        pygame.display.set_caption("CreyBlock - WorldCreator")
        self.screenReal = pygame.display.set_mode(self.sizeScreen, HWSURFACE | DOUBLEBUF | RESIZABLE)

        self.generateWorldSize = 2
        self.generateWorldType = "def"

        pic = pygame.surface.Surface((50, 50))
        pic.fill((255, 100, 200))

        self.mainWallpeper = pygame.image.load(f'{sys.path[0]}/assest/textures/worldGenWapllpeper.png').convert_alpha()
        self.mainButton = pygame.image.load(f'{sys.path[0]}/assest/textures/mainButtonTexture.png').convert_alpha()

        self.mainFont = pygame.font.Font((f"{sys.path[0]}/assest/fonts/menu.ttf"), 150)
        self.mainFontB = pygame.font.Font((f"{sys.path[0]}/assest/fonts/menu.ttf"), 90)

        self.always()

    def always(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == VIDEORESIZE:
                    self.screenReal = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

            self.drawing()

            self.screenReal.blit(pygame.transform.scale(self.screen, self.screenReal.get_rect().size), (0, 0))
            pygame.display.update()

            self.buttonClick()

    def drawing(self):
        self.screen.blit(self.mainWallpeper, (0, 0))
        self.screen.blit(self.mainFont.render("World Generator", True, (200, 200, 200)), (250, 50))

        # SMALL SIZE BUTTON
        self.screen.blit(pygame.transform.scale(self.mainButton, (400, 120)), (260, 300))
        self.screen.blit(self.mainFontB.render("Small", True, (220, 220, 220)), (325, 320))

        # MEDIUM SIZE BUTTON
        self.screen.blit(pygame.transform.scale(self.mainButton, (400, 120)), (760, 300))
        self.screen.blit(self.mainFontB.render("Medium", True, (220, 220, 220)), (780, 320))

        # LARGE SIZE BUTTON
        self.screen.blit(pygame.transform.scale(self.mainButton, (400, 120)), (1260, 300))
        self.screen.blit(self.mainFontB.render("Large", True, (220, 220, 220)), (1325, 320))

        # GENERATE WORLD BUTTON
        self.screen.blit(pygame.transform.scale(self.mainButton, (1400, 240)), (260, 750))
        self.screen.blit(self.mainFont.render("GENERATE WORLD", True, (220, 220, 220)), (300, 800))



    def buttonClick(self):
        self.sizeScreen = 1920, 1080
        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()[0] * (
                self.sizeScreen[0] / self.screenReal.get_rect().size[0]), pygame.mouse.get_pos()[
                                             1] * (self.sizeScreen[1] /
                                                   self.screenReal.get_rect().size[1])
        if pygame.mouse.get_pressed(3)[0]:
            self.buttonSize()
            self.buttonGenerateWorld()

    def buttonSize(self):
        hitBox = pygame.rect.Rect(260, 300, 400, 120)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            self.generateWorldSize = 4096

        hitBox = pygame.rect.Rect(760, 300, 400, 120)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            self.generateWorldSize = 16384

        hitBox = pygame.rect.Rect(1260, 300, 400, 120)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            self.generateWorldSize = 32192

    def buttonGenerateWorld(self):
        hitBox = pygame.rect.Rect(260, 750, 1400, 240)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
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
                        if 0 <= randomSpawn <= 69  and worldStructureSpawningList[i-1] == 0 and ifTreeSpawn == 1:
                            worldStructureSpawningList.append(1)
                        elif 70 <= randomSpawn <= 80 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(2)
                        elif 81 <= randomSpawn <= 89 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(3)
                        elif 90 <= randomSpawn <= 95 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(4)
                        elif 96 <= randomSpawn <= 98 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(5)
                        elif 99 <= randomSpawn <= 101 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(6)
                        else:
                            worldStructureSpawningList.append(0)
                    except Exception:
                        worldStructureSpawningList.append(0)

                return worldStructureSpawningList

            trybGeneratora = self.generateWorldType
            dlugosc = self.generateWorldSize

            if trybGeneratora == "flat":

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

                swiat = GenerateTerainGrassland(dlugosc)

                swiatFileToWrite = []

                worldStructureSpawningList = worldStructureSpawning(dlugosc)

                def oreAndTreeDiscrybution(swiat):
                    for i in range((34 - swiat) * 96, 0, -96):
                        swiatFileToWrite[sz].append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")

                    if worldStructureSpawningList[sz] == 1:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},treGen")
                    elif worldStructureSpawningList[sz] == 2:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},coaGen")
                    elif worldStructureSpawningList[sz] == 3:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},iroGen")
                    elif worldStructureSpawningList[sz] == 4:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},golGen")
                    elif worldStructureSpawningList[sz] == 5:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},diaGen")
                    elif worldStructureSpawningList[sz] == 6:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},emeGen")
                    else:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},0")

                    swiatFileToWrite[sz].append(f"{sz * 96},{792 - (swiat * 96)},16")
                    swiatFileToWrite[sz].append(f"{sz * 96},{888 - (swiat * 96)},14")
                    swiatFileToWrite[sz].append(f"{sz * 96},{984 - (swiat * 96)},14")
                    swiatFileToWrite[sz].append(f"{sz * 96},{1080 - (swiat * 96)},14")

                    for i in range((56 + swiat)):
                        swiatFileToWrite[sz].append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")

                    swiatFileToWrite[sz].append(f"{sz * 96},{6552},bedGen")

                    #for i in range(0, 57 * 96, 96):
                    #    swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1")

                def swiat0(sz):
                    oreAndTreeDiscrybution(0)

                def swiat1(sz):
                    oreAndTreeDiscrybution(1)

                def swiat2(sz):
                    oreAndTreeDiscrybution(2)

                def swiat3(sz):
                    oreAndTreeDiscrybution(3)

                def swiat4(sz):
                    oreAndTreeDiscrybution(4)

                swiatGenSetting = {0: swiat0, 1: swiat1, 2: swiat2, 3: swiat3, 4: swiat4}

                for sz in range(dlugosc):
                    swiatFileToWrite.append([])
                    swiatGenSetting[swiat[sz]](sz)

                playerInfo = [dlugosc * 48, 600, dlugosc]
            # SPAWN WORLD SETTER
                try:
                    os.makedirs("assest/saves/save")
                except Exception:
                    pass

                with open(f'{sys.path[0]}/assest/saves/save/worldSave.data', 'wb') as filehandle:
                    pickle.dump(swiatFileToWrite, filehandle)

                with open(f'{sys.path[0]}/assest/saves/save/playerSave.data', 'wb') as filehandle:
                    pickle.dump(playerInfo, filehandle)

                main.Main()