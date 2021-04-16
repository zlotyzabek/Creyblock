import sys
import threading

import pygame

# Creyblock



class Main:

    def __init__(self):

        pygame.init()

        size = 1920, 1080
        self.screen = pygame.display.set_mode(size)

        # TEXTURES AND STRINGS PRINT
        self.mainWallpeper = pygame.image.load('textures/mainWallpeper.png').convert_alpha()
        self.mainButton = pygame.image.load('textures/mainButtonTexture.png').convert_alpha()
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

            self.drawing()

            pygame.display.flip()

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

        #pygame.draw.rect(self.screen, (0, 0, 0), pygame.rect.Rect(560, 650, 800, 100))

        #pygame.draw.rect(self.screen, (0, 0, 0), pygame.rect.Rect(560, 800, 800, 100))

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
        self.saveTimeWorld = 1   # Time in minutes how many times the world should record. Set to 0 to disable.

        #
        pygame.init()

        self.block = []

        self.clock = pygame.time.Clock()
        self.delta = 0.00

        self.saveToTime = 0
        self.saveImageDisplay = 0

        self.xPosCam, self.yPosCam = 0, 0

        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()

        self.blockFileRead = []

        self.selectBlock = 2

        # LOADING WORLD
        readTEMP = []

        with open("save.mov", "r") as f:
            for line in f:
                readTEMP.append(int(line.split(",")[0]))
                readTEMP.append(int(line.split(",")[1]))
                readTEMP.append(int(line.split(",")[2].split("\n")[0]))

        for i in range(3, int(len(readTEMP)/3)):
            self.blockFileRead.append(readTEMP[i * 3])
            self.blockFileRead.append(readTEMP[i * 3 + 1])
            self.blockFileRead.append(readTEMP[i * 3 + 2])

        del readTEMP

        # SCREEN
        size = 1920, 1080
        self.screen = pygame.display.set_mode(size)

        # TEXTURES
        self.dirt = pygame.image.load('textures/dirt.png').convert_alpha()
        self.log = pygame.image.load('textures/log.png').convert_alpha()
        self.grass = pygame.image.load('textures/grass.png').convert_alpha()
        self.stone = pygame.image.load('textures/stone.png').convert_alpha()
        self.leaves = pygame.image.load('textures/leaves_oak.png').convert_alpha()
        self.typeBlockTexture = {1: self.stone, 2: self.dirt, 3: self.grass, 4: self.log, 5: self.leaves}

        self.skyColor = 60, 210, 220
        self.errorTextures = 255, 0, 255
        self.chest = 150, 100, 50
        self.body = 150, 100, 50

        self.always()

    def always(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.savingWorld()
                    sys.exit()

            self.delta += self.clock.tick()/1000.0
            while self.delta > 1 / 120.0:
                self.ticking()
                self.delta -= 1 / 120.0

            self.screen.fill(self.skyColor)
            self.drawing()
            pygame.display.flip()

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

            for i in range(int(len(self.blockFileRead) / 3)):
                swiatFileToWrite.append(f"{self.blockFileRead[i * 3]},{self.blockFileRead[i * 3 + 1]},{self.blockFileRead[i * 3 + 2]}\n")

            with open("save.mov", "w") as f:
                f.writelines(swiatFileToWrite)

            self.saveImageDisplay = 0

    def drawing(self):
        try:
            for i in range((int((-1 * self.xPosCam - 200) * 2.0624888899999999999999)),  (int((-1 * self.xPosCam + 2120) * 2.0624888899999999999999))):
                if -100 < int(self.blockFileRead[i * 3]) + self.xPosCam < 2020 and -100 < int(self.blockFileRead[i * 3 + 1]) + self.yPosCam < 1180:
                    self.blockRemoving(self.blockFileRead[3 * i + 2], i)
                    self.blockSetter(self.blockFileRead[3 * i + 2], i)

                    try:
                        self.screen.blit(self.typeBlockTexture[self.blockFileRead[3 * i + 2]], (
                        int(self.blockFileRead[3 * i]) + self.xPosCam,
                        int(self.blockFileRead[(3 * i) + 1]) + self.yPosCam))
                    except Exception:
                        pass

        except Exception:
            pass
        self.drawGui()
        self.drawBody()


    def drawBody(self):
        body = pygame.Rect(936, 516, 48, 48)
        pygame.draw.rect(self.screen, self.body, body)

    def drawGui(self):
        if self.saveImageDisplay == 1:
            savingGui = (pygame.Rect(98, 98, 48, 48))
            pygame.draw.rect(self.screen, self.chest, savingGui)

    def blockRemoving(self, color, blockIdNumber):
        block = (pygame.Rect(int(self.blockFileRead[3 * blockIdNumber]) + self.xPosCam, int(self.blockFileRead[(3 * blockIdNumber) + 1]) + self.yPosCam, 48, 48))
        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()
        collide = block.collidepoint(self.xPosMouse, self.yPosMouse)
        if pygame.mouse.get_pressed(3)[0]:
            if color != 0 and collide:
                self.blockFileRead[blockIdNumber * 3 + 2] = 0

    def blockSetter(self, color, blockIdNumber):
        block = (pygame.Rect(int(self.blockFileRead[3 * blockIdNumber]) + self.xPosCam, int(self.blockFileRead[(3 * blockIdNumber) + 1]) + self.yPosCam, 48, 48))
        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()
        collide = block.collidepoint(self.xPosMouse, self.yPosMouse)
        if pygame.mouse.get_pressed(3)[2]:
            if color == 0 and collide:
                self.blockFileRead[blockIdNumber * 3 + 2] = self.selectBlock

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.xPosCam += 3
            if keys[pygame.K_LSHIFT]:
                self.xPosCam += 3

        elif keys[pygame.K_d]:
            self.xPosCam += -3
            if keys[pygame.K_LSHIFT]:
                self.xPosCam -= 3

        if keys[pygame.K_w]:
            self.yPosCam += 3
            if keys[pygame.K_LSHIFT]:
                self.yPosCam += 3

        elif keys[pygame.K_s]:
            self.yPosCam += -3
            if keys[pygame.K_LSHIFT]:
                self.yPosCam -= 3

        if keys[pygame.K_1]:
            self.selectBlock = 1

        elif keys[pygame.K_2]:
            self.selectBlock = 2

        elif keys[pygame.K_3]:
            self.selectBlock = 3

        elif keys[pygame.K_4]:
            self.selectBlock = 4

        elif keys[pygame.K_5]:
            self.selectBlock = 5

        elif keys[pygame.K_6]:
            pass

        elif keys[pygame.K_7]:
            pass

        elif keys[pygame.K_8]:
            pass

        elif keys[pygame.K_9]:
            pass

if __name__ == "__main__":
    Main()
