import sys
import threading

import pygame
from pygame.locals import *
from pygame.math import Vector2
import pyautogui

# Creyblock



class Main:

    def __init__(self):

        pygame.init()

        self.screenReal = pygame.display.set_mode((pyautogui.size()[0], pyautogui.size()[1]), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.screenReal.copy()

        pic = pygame.surface.Surface((50, 50))
        pic.fill((255, 100, 200))

        # TEXTURES AND STRINGS PRINT
        self.mainWallpeper = pygame.image.load('assest/textures/mainWallpeper.png').convert_alpha()
        self.mainButton = pygame.image.load('assest/textures/mainButtonTexture.png').convert_alpha()
        self.mainFontB = pygame.font.SysFont("Showcard Gothic", 202)
        self.mainFont = pygame.font.SysFont("Showcard Gothic", 200)

        self.always()

        # BUTTON HITBOX
        self.buttonSinglePlayerHitbox = pygame.draw.rect(self.screen, (0, 0, 0), pygame.rect.Rect(560, 500, 800, 100))

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
        # WALPAPER
        self.screen.blit(self.mainWallpeper, (0, 0))

        # CAPITION
        self.screen.blit(self.mainFontB.render("Creyblock", True, (10, 10, 10)), (370, 105))
        self.screen.blit(self.mainFont.render("Creyblock", True, (250, 250, 250)), (370, 110))

        # BUTTONS
        self.screen.blit(self.mainButton, (560, 500))
        self.screen.blit(self.mainButton, (560, 650))
        self.screen.blit(self.mainButton, (560, 800))

    def buttonClick(self):
        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed(3)[0]:
            self.buttonSinglePlayer()

    def buttonSinglePlayer(self):
        hitBox = pygame.draw.rect(self.screen, (0, 0, 0), pygame.rect.Rect(560, 500, 800, 100))
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            Game()
            sys.exit()

class Game:

    def __init__(self):

        # CONFIG
        self.saveTimeWorld = 3   # Time in minutes how many times the world should record. Set to 0 to disable.

        pygame.init()

        self.programRun = 1

        self.block = []

        self.clock = pygame.time.Clock()
        self.delta = 0.00

        self.saveToTime = 0
        self.saveImageDisplay = 0

        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()

        self.blockFileRead = []

        self.selectBlock = 2

        # LOADING WORLD
        with open("assest/saves/save.mov", "r") as f:
            readTEMP = str(f.read()).split('\n')[:-1]

        for i in range(3, int(len(readTEMP))):
            self.blockFileRead.append(int(readTEMP[i].split(",")[0]))
            self.blockFileRead.append(int(readTEMP[i].split(",")[1]))
            self.blockFileRead.append(int(readTEMP[i].split(",")[2]))


        # SCREEN
        self.sizeScreen = pyautogui.size()[0], pyautogui.size()[1]
        self.screenReal = pygame.display.set_mode(self.sizeScreen, HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.screenReal.copy()

        # PHYSIC

        # CORDYNATS
        self.PosCam = Vector2(int(readTEMP[0].split(",")[0]) * -1, int(readTEMP[0].split(",")[1]))

        # COLIZION
        self.blockCollizionDetect = [0, 0, 0, 0]

        # TEXTURES
        self.dirt = pygame.image.load('assest/textures/dirt.png').convert_alpha()
        self.log = pygame.image.load('assest/textures/log.png').convert_alpha()
        self.grass = pygame.image.load('assest/textures/grass.png').convert_alpha()
        self.stone = pygame.image.load('assest/textures/stone.png').convert_alpha()
        self.leaves = pygame.image.load('assest/textures/leaves_oak.png').convert_alpha()
        self.planks = pygame.image.load('assest/textures/planks.png').convert_alpha()
        self.diamond = pygame.image.load('assest/textures/diamond_ore.png').convert_alpha()
        self.iron = pygame.image.load('assest/textures/iron_ore.png').convert_alpha()
        self.coal = pygame.image.load('assest/textures/coal_ore.png').convert_alpha()
        self.typeBlockTexture = {1: self.stone, 2: self.dirt, 3: self.grass, 4: self.log, 5: self.leaves, 6: self.planks, 7: self.coal, 8: self.iron, 9: self.diamond}
        for i in range(1, len(self.typeBlockTexture) + 1):
            self.typeBlockTexture[i] = pygame.transform.scale(self.typeBlockTexture[i], (96, 96))

        self.head = pygame.image.load('assest/textures/player/head.png').convert_alpha()
        self.head = pygame.transform.scale(self.head, (64, 64))

        self.legs = pygame.image.load('assest/textures/player/legs.png').convert_alpha()
        self.legs = pygame.transform.scale(self.legs, (20, 32))

        self.skyColor = 60, 210, 220
        self.errorTextures = 255, 0, 255
        self.chest = 150, 100, 50
        self.body = 150, 100, 50

        del readTEMP

        self.always()

    def always(self):
        while self.programRun == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.savingWorld()
                    self.programRun = 0

                elif event.type == VIDEORESIZE:
                    self.screenReal = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

            self.delta += self.clock.tick()/1000.0
            while self.delta > 1 / 480.0:
                self.ticking()
                self.delta -= 1 / 480.0

            self.screen.fill(self.skyColor)
            self.drawing()
            self.screenReal.blit(pygame.transform.scale(self.screen, self.screenReal.get_rect().size), (0, 0))
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
            swiatFileToWrite = []

            for i in range(0, int(len(self.blockFileRead)), 3):
                swiatFileToWrite.append(f"{self.blockFileRead[i]},{self.blockFileRead[i + 1]},{self.blockFileRead[i + 2]}\n")

            with open("assest/saves/save.mov", "w") as f:
                f.write(f"{self.PosCam.x * -1},{self.PosCam.y}\n")
                f.write("0,0\n")
                f.write("0,0\n")
                f.writelines(swiatFileToWrite)

            self.saveImageDisplay = 0

    def drawing(self):
        try:
            self.blockCollizionDetect = [0, 0, 0, 0]
            for i in range((int((-1 * self.PosCam.x - 200))), (int((-1 * self.PosCam.x + 2120)))):
                if -100 < int(self.blockFileRead[i * 3]) + self.PosCam.x < 2020 and -100 < int(
                        self.blockFileRead[i * 3 + 1]) + self.PosCam.y < 1180:
                    block = (pygame.Rect(int(self.blockFileRead[3 * i]) + self.PosCam.x,
                                         int(self.blockFileRead[(3 * i) + 1]) + self.PosCam.y, 96, 96))
                    self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()[0] * (
                            self.sizeScreen[0] / self.screenReal.get_rect().size[0]), pygame.mouse.get_pos()[1] * (
                                                             self.sizeScreen[1] / self.screenReal.get_rect().size[1])
                    self.blockRemovingAndSetter(i, block)

                    try:
                        self.screen.blit(self.typeBlockTexture[self.blockFileRead[3 * i + 2]], (
                            int(self.blockFileRead[3 * i]) + self.PosCam.x,
                            int(self.blockFileRead[(3 * i) + 1]) + self.PosCam.y))
                        if block.colliderect(pygame.Rect(936, 491, 48, 1)) == 1:
                            self.blockCollizionDetect[2] += 1
                        if block.colliderect(pygame.Rect(927, 500, 1, 48)) == 1:
                            self.blockCollizionDetect[0] += 1
                        if block.colliderect(pygame.Rect(992, 500, 1, 48)) == 1:
                            self.blockCollizionDetect[1] += 1
                        if block.colliderect(pygame.Rect(936, 556, 48, 1)) == 1:
                            self.blockCollizionDetect[3] += 1

                    except Exception:
                        pass

            self.drawGui()
            self.drawBody()
        except Exception:
            pass

    def drawBody(self):
        self.screen.blit(self.head, (928, 492))
        self.screen.blit(self.legs, (930, 556))
        self.screen.blit(self.legs, (970, 556))

    def drawGui(self):
        if self.saveImageDisplay == 1:
            savingGui = (pygame.Rect(98, 98, 48, 48))
            pygame.draw.rect(self.screen, self.chest, savingGui)

    def blockRemovingAndSetter(self, blockIdNumber, block):
        collide = block.collidepoint(self.xPosMouse, self.yPosMouse)
        if pygame.mouse.get_pressed(3)[0] and self.blockFileRead[3 * blockIdNumber + 2] != 0 and collide:
                self.blockFileRead[blockIdNumber * 3 + 2] = 0

        elif pygame.mouse.get_pressed(3)[2] and self.blockFileRead[3 * blockIdNumber + 2] == 0 and collide:
                self.blockFileRead[blockIdNumber * 3 + 2] = self.selectBlock

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[97] and self.blockCollizionDetect[0] < 1:
            self.PosCam.x += 1
            if keys[pygame.K_LSHIFT]:
                self.PosCam.x += 1

        elif keys[100] and self.blockCollizionDetect[1] < 1:
            self.PosCam.x += -1
            if keys[pygame.K_LSHIFT]:
                self.PosCam.x -= 1

        if self.blockCollizionDetect[3] < 1:
            self.PosCam.y -= 1

        elif keys[119] and self.blockCollizionDetect[2] < 1 and self.blockCollizionDetect[3] > 0:
            threading.Thread(target=self.controlsJump()).start()

        if keys[49]:
            self.selectBlock = 1

        elif keys[50]:
            self.selectBlock = 2

        elif keys[51]:
            self.selectBlock = 3

        elif keys[52]:
            self.selectBlock = 4

        elif keys[53]:
            self.selectBlock = 5

        elif keys[54]:
            self.selectBlock = 6

        elif keys[55]:
            self.selectBlock = 7

        elif keys[56]:
            self.selectBlock = 8

        elif keys[57]:
            self.selectBlock = 9

    def controlsJump(self):
        for i in range(30):
            self.PosCam.y += 1

if __name__ == "__main__":
    Main()
