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
        self.sizeScreen = pyautogui.size()[0], pyautogui.size()[1]
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
                self.typeBlockTextureBlock[i + 1] = pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha().convert(), (96, 96))
                self.typeBlockTextureInventory[i + 1] = pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha().convert(), (64, 64))
            if list.split(",")[1] == "a":
                self.typeBlockTextureBlock[i + 1] = pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha(),(96, 96))
                self.typeBlockTextureInventory[i + 1] = pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha(), (64, 64))

        self.itemAndBlockID = {}

        for i in range(len(self.typeBlockTextureInventory)):
            self.itemAndBlockID[self.typeBlockTextureInventory[i + 1]] = {self.typeBlockTextureBlock[i + 1]}

        self.head = pygame.image.load('assest/textures/player/head.png').convert_alpha().convert()
        self.head = pygame.transform.scale(self.head, (64, 64))

        self.hotBarTexture = pygame.image.load('assest/textures/hotBar.png').convert()
        self.hotBarTexture = pygame.transform.scale(self.hotBarTexture, (1000, 100))

        self.eqTexture = pygame.image.load('assest/textures/equipment.png').convert_alpha()
        self.eqTexture = pygame.transform.scale(self.eqTexture, (1379, 580))

        self.eqSelectTexture = pygame.image.load('assest/textures/selection_equipment.png').convert_alpha()
        self.eqSelectTexture = pygame.transform.scale(self.eqSelectTexture, (76, 76))

        self.mEqShowItems = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.skyColor = 60, 210, 220
        self.errorTextures = 255, 0, 255
        self.chest = 150, 100, 50
        self.body = 150, 100, 50

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
                    if event.button == 4:
                        self.selectBlock += 1
                        if self.selectBlock == 11:
                            self.selectBlock = 1
                    if event.button == 5:
                        self.selectBlock -= 1
                        if self.selectBlock == -1:
                            self.selectBlock = 9

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

                    #elif event.key == pygame.K_TAB:
                    #    if self.maxEqShow == 0:
                    #        self.maxEqShow = 1
                    #    else:
                    #        self.maxEqShow = 0

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
                        self.screen.blit(self.typeBlockTextureBlock[int(self.blockFileRead[szer][wys].split(",")[2])], (
                            int(self.blockFileRead[szer][wys].split(",")[0]) + self.PosCam.x,
                            int(self.blockFileRead[szer][wys].split(",")[1]) + self.PosCam.y))
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
        self.drawGui()

    def drawBody(self):
        self.screen.blit(self.head, (928, 492))

    def worldGen(self, szer, wys):
        if self.blockFileRead[szer][wys].split(",")[2] == "treeGen":
            treeSize = random.randint(1, 5)
            with open(f"assest/structures/trees/size{treeSize}.txt", "r") as f:
                for line in f:
                    tempLineSplit = (line.split(","))
                    tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                    try:
                        self.blockFileRead[szer + int(tempLineSplit[0])][
                            wys + int(tempLineSplit[1])] = \
                            self.structurListEditor(self.blockFileRead, szer + int(tempLineSplit[0]),
                                               wys + int(tempLineSplit[1]), tempLineSplit[2],
                                               tempLineSplit[3].split("\n")[0])
                    except Exception:
                        pass

        elif self.blockFileRead[szer][wys].split(",")[2] == "coalGen":
            coalSize = random.randint(1, 4)
            coalDown = random.randint(10, 50)
            with open(f"assest/structures/ores/coalSize{coalSize}.txt", "r") as f:
                self.blockFileRead[szer][wys] = \
                    self.structurListEditor(self.blockFileRead, szer, wys, "coalGen", "0")
                for line in f:
                    tempLineSplit = (line.split(","))
                    tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                    try:
                        self.blockFileRead[szer + int(tempLineSplit[0])][
                            wys + int(tempLineSplit[1]) + coalDown] = \
                            self.structurListEditor(self.blockFileRead, szer + int(tempLineSplit[0]),
                                               wys + int(tempLineSplit[1]) + coalDown,
                                               tempLineSplit[2], tempLineSplit[3])

                    except Exception:
                        pass

        elif self.blockFileRead[szer][wys].split(",")[2] == "ironGen":
            ironSize = random.randint(1, 3)
            ironDown = random.randint(10, 50)
            with open(f"assest/structures/ores/ironSize{ironSize}.txt", "r") as f:
                self.blockFileRead[szer][wys] = \
                    self.structurListEditor(self.blockFileRead, szer, wys, "ironGen", "0")
                for line in f:
                    tempLineSplit = (line.split(","))
                    tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                    try:
                        self.blockFileRead[szer + int(tempLineSplit[0])][
                            wys + int(tempLineSplit[1]) + ironDown] = \
                            self.structurListEditor(self.blockFileRead, szer + int(tempLineSplit[0]),
                                               wys + int(tempLineSplit[1]) + ironDown,
                                               tempLineSplit[2], tempLineSplit[3])

                    except Exception:
                        pass

        elif self.blockFileRead[szer][wys].split(",")[2] == "diamondGen":
            diamondSize = random.randint(1, 2)
            diamondDown = random.randint(10, 50)
            with open(f"assest/structures/ores/diamondSize{diamondSize}.txt", "r") as f:
                self.blockFileRead[szer][wys] = \
                    self.structurListEditor(self.blockFileRead, szer, wys, "diamondGen", "0")
                for line in f:
                    tempLineSplit = (line.split(","))
                    tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                    try:
                        self.blockFileRead[szer + int(tempLineSplit[0])][
                            wys + int(tempLineSplit[1]) + diamondDown] = \
                            self.structurListEditor(self.blockFileRead, szer + int(tempLineSplit[0]),
                                               wys + int(tempLineSplit[1]) + diamondDown,
                                               tempLineSplit[2], tempLineSplit[3])

                    except Exception:

                        pass

    def drawGui(self):
        self.drawBody()

        self.screen.blit(self.hotBarTexture, (460, 920))

        for i in range(10):
            if self.mEqShowItems[i] != 0:

                self.screen.blit(self.typeBlockTextureInventory[self.mEqShowItems[i]], (485 + (i * 99), 941))

        self.screen.blit(self.eqSelectTexture, (479 + (self.selectBlock * 99), 935))

        if self.maxEqShow == 1:
            self.screen.blit(self.eqTexture, (200, 160))

        if self.saveImageDisplay == 1:
            savingGui = (pygame.Rect(98, 98, 48, 48))
            pygame.draw.rect(self.screen, self.chest, savingGui)

            #self.itemAndBlockID

    def blockRemovingAndSetter(self, blockColor, block):
        collide = block.collidepoint(self.xPosMouse, self.yPosMouse)
        if pygame.mouse.get_pressed(3)[0] and self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[2] != "0" and collide:
            temp = [self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[0], self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[1]]
            self.blockFileRead[blockColor[0]][blockColor[1]] = f"{temp[0]},{temp[1]},0"

        elif pygame.mouse.get_pressed(3)[2] and self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[2] == "0" and collide:
            collideHuman = block.colliderect(pygame.Rect(928, 492, 64, 64))
            if not collideHuman:
                temp = [self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[0], self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[1]]
                self.blockFileRead[blockColor[0]][blockColor[1]] = f"{temp[0]},{temp[1]},{self.mEqShowItems[self.selectBlock]}"

    def structurListEditor(self, list, szer, wys, rep, torep):
        return str(list[szer][wys])[::-1].replace(rep[::-1] + ",", torep[::-1] + ",", 1)[::-1]

    def colides(self):
        if self.blockCollizionDetect[0] > 0:
            self.PosCam += Vector2(-6, 0)

        if self.blockCollizionDetect[1] > 0:
            self.PosCam += Vector2(6, 0)

    def controls(self):
        keys = pygame.key.get_pressed()

# RIGH AND LEFT

        if self.maxEqShow == 0:
            if keys[97] and self.blockCollizionDetect[0] < 1 and self.blockCollizionDetect[5] < 1:
                self.PosCam += Vector2(6, 0)
                if keys[pygame.K_LSHIFT]:
                    self.PosCam += Vector2(6, 0)

            if keys[100] and self.blockCollizionDetect[1] < 1 and self.blockCollizionDetect[6] < 1:
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