import threading
import random
import pickle

import pygame
from pygame.locals import *
from pygame.math import Vector2
import pyautogui
import sys


class Game:

    def __init__(self):

        # CONFIG
        self.saveTimeWorld = 3   # Time in minutes how many times the world should record. Set to 0 to disable.

        pygame.init()

        # LOADING WORLD
        with open('assest/saves/save/worldSave.data', 'rb') as filehandle:
            self.blockFileRead = pickle.load(filehandle)

        with open('assest/saves/save/playerSave.data', 'rb') as filehandle:
            self.playerInfo = pickle.load(filehandle)

        self.programRun = 1

        self.block = []

        self.clock = pygame.time.Clock()
        self.delta = 0.00

        self.saveToTime = 0
        self.saveImageDisplay = 0

        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()

        self.selectBlock = 2

        # SCREEN
        self.sizeScreen = 1920, 1080
        self.screenReal = pygame.display.set_mode((1920, 1080), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.screenReal.copy()
        pygame.display.set_caption("CreyBlock - GAME")
        self.screenReal = pygame.display.set_mode(self.sizeScreen, HWSURFACE | DOUBLEBUF | RESIZABLE)

        self.fullscreen = 0

        # CORDYNATS
        self.PosCam = Vector2(int(self.playerInfo[0]) * -1, int(self.playerInfo[1]))

        # COLIZION
        self.blockCollizionDetect = [0, 0, 0, 0, 0, 0, 0, 0]

        # EQU
        #self.minEqShow = 1
        self.maxEqShow = 0

        # TEXTURES
        with open("assest/textures/texturesBlockLoad.txt", "r") as f:
            readTEMPtextures = str(f.read()).split('\n')[:-1]
        self.typeBlockTextureBlock = {}
        self.typeBlockTextureInventory = {}
        for i, list in enumerate(readTEMPtextures):
            if list.split(",")[1] == "c":
                self.typeBlockTextureBlock[i + 1] = [pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha().convert(), (96, 96)), list.split(",")[2]]
                self.typeBlockTextureInventory[i + 1] = pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha().convert(), (64, 64))
            if list.split(",")[1] == "a":
                self.typeBlockTextureBlock[i + 1] = [pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha(),(96, 96)), list.split(",")[2]]
                self.typeBlockTextureInventory[i + 1] = pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha(), (64, 64))

        self.head = pygame.image.load('assest/textures/player/head.png').convert_alpha().convert()
        self.head = pygame.transform.scale(self.head, (64, 64))

        self.hotBarTexture = pygame.image.load('assest/textures/hotBar.png').convert()
        self.hotBarTexture = pygame.transform.scale(self.hotBarTexture, (1000, 100))

        self.eqTexture = pygame.image.load('assest/textures/equipment.png').convert_alpha()
        self.eqTexture = pygame.transform.scale(self.eqTexture, (1000, 381))

        self.eqSelectTexture = pygame.image.load('assest/textures/selection_equipment.png').convert_alpha()
        self.eqSelectTexture = pygame.transform.scale(self.eqSelectTexture, (76, 76))

        self.mEqShowItems = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.skyColor = 60, 210, 220
        self.errorTextures = 255, 0, 255
        self.chest = 150, 100, 50
        self.body = 150, 100, 50

        self.eqItemsID = [[],[],[], [], [] ,[] ,[] ,[] ,[] ,[] ,[]]

        self.eqItemsID[0] = [1,2,3,4,5,6,7,8,9,10]
        self.eqItemsID[1] = [11,12,13,14,15,16,17,18,19,20]
        self.eqItemsID[2] = [21,0,0,0,0,0,0,0,0,0]
        self.eqItemsID[3] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.eqItemsID[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.eqItemsID[5] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.eqItemsID[6] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.eqLine = 0

        self.itemClick = 0

        self.oneMouseClick = 0


        self.fallSpeed = 6.00

        self.always()

    def always(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.savingWorld()
                    sys.exit()

                elif event.type == pygame.VIDEORESIZE:
                    self.screenReal = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.oneMouseClick = 1

                    if event.button == 4:
                        if self.maxEqShow == 0:
                            self.selectBlock += 1
                            if self.selectBlock == 10:
                                self.selectBlock = 0
                        elif self.maxEqShow == 1:
                            self.eqLine -= 1
                            if self.eqLine == -1:
                                self.eqLine = 0
                    if event.button == 5:
                        if self.maxEqShow == 0:
                            self.selectBlock -= 1
                            if self.selectBlock == -1:
                                self.selectBlock = 9

                        elif self.maxEqShow == 1:
                            self.eqLine +=1



                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.maxEqShow == 0:
                        if self.blockCollizionDetect[4] > 0 and self.blockCollizionDetect[2] < 1 and self.blockCollizionDetect[7] > 0:
                            threading.Thread(target=self.controlsJumpLow()).start()
                        elif self.blockCollizionDetect[4] > 0 and self.blockCollizionDetect[2] < 1 and self.blockCollizionDetect[8] > 0:
                            threading.Thread(target=self.controlsJumpMedium()).start()
                        elif self.blockCollizionDetect[4] > 0 and self.blockCollizionDetect[2] < 1:
                            threading.Thread(target=self.controlsJumpHigh()).start()


                    for i in range(49, 58):
                        if event.key == i:
                            self.selectBlock = i - 49


                    if event.key == pygame.K_0:
                        self.selectBlock = 9

                    elif event.key == pygame.K_TAB:
                        if self.maxEqShow == 0:
                            self.maxEqShow = 1
                        else:
                            self.maxEqShow = 0

            self.delta += self.clock.tick()/1000.0
            while self.delta > 1 / 60.0:
                self.ticking()
                self.delta -= 1 / 60.0

            self.drawing()
            self.screenReal.blit(pygame.transform.scale(self.screen, self.screenReal.get_rect().size), (0, 0))
            self.colides()
            pygame.display.update()

    def ticking(self):
        self.controls()
        if self.saveToTime >= self.saveTimeWorld * 7200:
            threading.Thread(target=self.savingWorld).start()

        self.saveToTime += 1

    def savingWorld(self):
        if self.saveTimeWorld != 0:
            self.saveImageDisplay = 1
            self.saveToTime = 0
            swiatFileToWrite = self.blockFileRead

            playerInfo = [int(self.PosCam.x * -1), int(self.PosCam.y), self.playerInfo[2]]
        # SPAWN WORLD SETTER
            with open('assest/saves/save/worldSave.data', 'wb') as filehandle:
                pickle.dump(swiatFileToWrite, filehandle)

            with open('assest/saves/save/playerSave.data', 'wb') as filehandle:
                pickle.dump(playerInfo, filehandle)

            self.saveImageDisplay = 0

    def drawing(self):
        self.blockCollizionDetect = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.screen.fill(self.skyColor)
        for szer in range(int((-1 * self.PosCam.x - 400) / 96), int((-1 * self.PosCam.x + 2320) / 96)):
            for wys in range(96):
                try:
                    self.worldGen(szer, wys)
                    if -100 < int(self.blockFileRead[szer][wys].split(",")[0]) + self.PosCam.x < 2020 and -100 < int(
                            self.blockFileRead[szer][wys].split(",")[1]) + self.PosCam.y < 1180:


                        block = (pygame.Rect(int(self.blockFileRead[szer][wys].split(",")[0]) + self.PosCam.x,
                                             int(self.blockFileRead[szer][wys].split(",")[1]) + self.PosCam.y, 96, 96))


                        self.blockRemovingAndSetter((szer, wys), block)

                        if self.blockFileRead[szer][wys].split(",")[2] != "0":
                            self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()[0] * (
                                    self.sizeScreen[0] / self.screenReal.get_rect().size[0]), pygame.mouse.get_pos()[
                                                                 1] * (self.sizeScreen[1] /
                                                                       self.screenReal.get_rect().size[1])
                            self.screen.blit(self.typeBlockTextureBlock[int(self.blockFileRead[szer][wys].split(",")[2])][0], (
                                int(self.blockFileRead[szer][wys].split(",")[0]) + self.PosCam.x,
                                int(self.blockFileRead[szer][wys].split(",")[1]) + self.PosCam.y))

                            if self.typeBlockTextureBlock[int(self.blockFileRead[szer][wys].split(",")[2])][1] == "c":
                                if block.colliderect(pygame.Rect(936, 491, 48, 1)) == 1:
                                    self.blockCollizionDetect[2] += 1
                                    # UP
                                if block.colliderect(pygame.Rect(936, 450, 48, 1)) == 1:
                                    self.blockCollizionDetect[7] += 1
                                    # UP 2
                                if block.colliderect(pygame.Rect(936, 354, 48, 1)) == 1:
                                    self.blockCollizionDetect[8] += 1
                                    # UP 3
                                if block.colliderect(pygame.Rect(927, 500, 1, 48)) == 1:
                                    self.blockCollizionDetect[0] += 1
                                    # LEFT
                                if block.colliderect(pygame.Rect(992, 500, 1, 48)) == 1:
                                    self.blockCollizionDetect[1] += 1
                                    # RIGHT
                                if block.colliderect(pygame.Rect(921, 500, 1, 48)) == 1:
                                    self.blockCollizionDetect[5] += 1
                                    # LEFT 2
                                if block.colliderect(pygame.Rect(998, 500, 1, 48)) == 1:
                                    self.blockCollizionDetect[6] += 1
                                    # RIGHT 2
                                if block.colliderect(pygame.Rect(936, 552, 48, 1)) == 1:
                                    self.blockCollizionDetect[3] += 1
                                    # DOWN

                                if block.colliderect(pygame.Rect(936, 560, 48, 1)) == 1:
                                    self.blockCollizionDetect[4] += 1
                                    # DOWN 2
                except Exception:
                    pass
        self.drawGui()

    def drawBody(self):
        self.screen.blit(self.head, (928, 492))

    def drawGui(self):
        self.drawBody()

        self.screen.blit(self.hotBarTexture, (460, 920))

        for i in range(10):
            if self.mEqShowItems[i] != 0:
                self.screen.blit(self.typeBlockTextureInventory[self.mEqShowItems[i]], (485 + (i * 99), 941))

        self.screen.blit(self.eqSelectTexture, (479 + (self.selectBlock * 99), 935))

        if self.maxEqShow == 1:
            self.screen.blit(self.eqTexture, (460, 420))

            hitboxesEq = []
            for wysEq in range(3):
                for szerEq in range(10):
                    if self.mEqShowItems[szerEq] != 0:
                        if self.eqItemsID[wysEq + self.eqLine][szerEq] > 0:
                            self.screen.blit(self.typeBlockTextureInventory[self.eqItemsID[wysEq + self.eqLine][szerEq]], (511 + (szerEq * 92.8), 502 + (wysEq * 92)))

                        if pygame.Rect(511 + (szerEq * 92.8), 502 + (wysEq * 92), 64, 64).collidepoint(self.xPosMouse, self.yPosMouse) and self.oneMouseClick == 1:
                            self.oneMouseClick = 0
                            self.itemClick = self.eqItemsID[wysEq + self.eqLine][szerEq]

            if self.itemClick != 0:
                self.screen.blit(self.typeBlockTextureInventory[self.itemClick], (self.xPosMouse - 32, self.yPosMouse - 32))

                if self.oneMouseClick == 1:
                    self.oneMouseClick = 0
                    for i in range(10):
                        if pygame.Rect(485 + (i * 99), 941, 64, 64).collidepoint(self.xPosMouse, self.yPosMouse):
                            self.mEqShowItems[i] = self.itemClick
                            self.itemClick = 0
                            break
                    self.itemClick = 0






        if self.saveImageDisplay == 1:
            savingGui = (pygame.Rect(98, 98, 48, 48))
            pygame.draw.rect(self.screen, self.chest, savingGui)

    def worldGen(self, szer, wys):
        def structurListEditor(list, szer, wys, rep, torep):
            return str(list[szer][wys])[::-1].replace(rep[::-1] + ",", torep[::-1] + ",", 1)[::-1]

        def oreGenerating(maxSize, minH, maxH, oreName, type):
            Size = random.randint(1, maxSize)
            Down = random.randint(minH, maxH)
            with open(f"assest/structures/{type}/{oreName}Size{Size}.txt", "r") as f:
                self.blockFileRead[szer][wys] = \
                    structurListEditor(self.blockFileRead, szer, wys, f"{oreName}Gen", "0")
                for line in f:
                    tempLineSplit = (line.split(","))
                    tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                    try:
                        self.blockFileRead[szer + int(tempLineSplit[0])][
                            wys + int(tempLineSplit[1]) + Down] = \
                            structurListEditor(self.blockFileRead, szer + int(tempLineSplit[0]),
                                               wys + int(tempLineSplit[1]) + Down,
                                               tempLineSplit[2], tempLineSplit[3])
                    except Exception:
                        pass

        if self.blockFileRead[szer][wys].split(",")[2] == "treGen":
            oreGenerating(5, 0, 0, "tre", "trees")

        elif self.blockFileRead[szer][wys].split(",")[2] == "coaGen":
            oreGenerating(4,10,50,"coa", "ores")

        elif self.blockFileRead[szer][wys].split(",")[2] == "iroGen":
            oreGenerating(3, 10, 50, "iro", "ores")

        elif self.blockFileRead[szer][wys].split(",")[2] == "iroGen":
            oreGenerating(2, 10, 50, "gol", "ores")

        elif self.blockFileRead[szer][wys].split(",")[2] == "diaGen":
            oreGenerating(2, 10, 50, "dia", "ores")

        elif self.blockFileRead[szer][wys].split(",")[2] == "emeGen":
            oreGenerating(1, 10, 50, "eme", "ores")

    def blockRemovingAndSetter(self, blockColor, block):
        collide = block.collidepoint(self.xPosMouse, self.yPosMouse)
        if pygame.mouse.get_pressed(3)[0] and self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[2] != "0" and collide and self.maxEqShow == 0:
            temp = [self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[0], self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[1]]
            self.blockFileRead[blockColor[0]][blockColor[1]] = f"{temp[0]},{temp[1]},0"

        elif pygame.mouse.get_pressed(3)[2] and self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[2] == "0" and collide and self.maxEqShow == 0:
            collideHuman = block.colliderect(pygame.Rect(928, 492, 64, 64))
            if not collideHuman:
                temp = [self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[0], self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[1]]
                self.blockFileRead[blockColor[0]][blockColor[1]] = f"{temp[0]},{temp[1]},{self.mEqShowItems[self.selectBlock]}"

    def colides(self):
        if self.blockCollizionDetect[0] > 0:
            self.PosCam += Vector2(-6, 0)

        if self.blockCollizionDetect[1] > 0:
            self.PosCam += Vector2(6, 0)

    def controls(self):
        keys = pygame.key.get_pressed()

# RIGH AND LEFT
        if self.maxEqShow == 0:
            if keys[97] and self.blockCollizionDetect[0] < 1 and self.blockCollizionDetect[5] < 1 and self.PosCam.x < -1 * (((96 * self.playerInfo[2]) / 2) - ((96 * self.playerInfo[2]) / 2)):
                self.PosCam += Vector2(6, 0)
                if keys[pygame.K_LSHIFT]:
                    self.PosCam += Vector2(6, 0)

            if keys[100] and self.blockCollizionDetect[1] < 1 and self.blockCollizionDetect[6] < 1 and self.PosCam.x - 1920 > -1 *(((96 * self.playerInfo[2]) / 2) - ((96 * (self.playerInfo[2] * -1))/2 )):
                self.PosCam += Vector2(-6, 0)
                if keys[pygame.K_LSHIFT]:
                    self.PosCam += Vector2(-6, 0)

    # GRAVITY AND UP self.fallSpeed
        if self.blockCollizionDetect[3] > 0:
            self.PosCam += Vector2(0, 6)

        elif self.blockCollizionDetect[4] < 1:
            self.PosCam += Vector2(0, self.fallSpeed * -1)
            self.fallSpeed *= 1.04
            if self.fallSpeed > 20.0:
                self.fallSpeed = 20.0

        elif self.blockCollizionDetect[2] > 0:
            self.PosCam += Vector2(0, -6)

        elif self.blockCollizionDetect[4] > 0:
            self.fallSpeed = 6.00

    def controlsJumpHigh(self):
        for i in range(220):
            self.PosCam += Vector2(0, 1)

    def controlsJumpMedium(self):
        for i in range(128):
            self.PosCam += Vector2(0, 1)

    def controlsJumpLow(self):
        for i in range(32):
            self.PosCam += Vector2(0, 1)