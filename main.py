import ursina
from ursina import *
import pickle
import biom
import PIL.Image
from ursina.shaders import lit_with_shadows_shader

eqMenage = {}

biomGen = biom.BiomGen()


def worldGen(szer):
    biome = blocks[szer][1]
    swiat = blocks[szer][2]
    structur = blocks[szer][3]

    if blocks[szer][0] == 0:
        for wys in range(100, -100, -1):
            blocks[szer, wys] = biomGen.biomGen(szer, wys, swiat, biome)
        blocks[szer][0] = 1

def structursGen(szer):
    biome = blocks[szer][1]

    def oreGenerating(settingsOre):
        if blocks[szer][3] == settingsOre[2]:
            if settingsOre[7] == 1:
                Deep = random.randint(0, 2)
                Size = random.randint(1, int(settingsOre[3]))
                Down = random.randint(int(settingsOre[4]), int(settingsOre[5])) * -1
                for i in range(100, -100, -1):
                    if blocks[szer, i][0] == int(settingsOre[6]):
                        Down += i + 1
                        break
                with open(
                        f"assest/structures/{biomes[blocks[szer][1] - 1]}/{settingsOre[2]}/{Size}.txt",
                        "r") as f:
                    settingsOre[7] = 0
                    blocks[szer][3] = 1
                    for line in f:
                        tempLineSplit = (line.split(","))
                        tempLineSplit[3] = tempLineSplit[3].split("\n")[0]
                        blocks[szer + int(tempLineSplit[0]), int(tempLineSplit[1]) + Down][Deep] = int(tempLineSplit[3])
            else:
                settingsOre[7] = 1
                blocks[szer][3] = 1

    for i in range(len(structures[biomes[biome - 1]])):
        oreGenerating(structures[biomes[biome - 1]][i])

# SAVE LOAD
with open(f'assest/saves/save/worldSave.data', 'rb') as filehandle:
    blocks = pickle.load(filehandle)

with open(f'assest/saves/save/playerSave.data', 'rb') as filehandle:
    playerInfo = pickle.load(filehandle)

# TEXTURES
    # BLOCKS
with open(f"assest/textures/texturesBlockLoad.txt", "r") as f:
    textureBlock = {}
    for i, line in enumerate(f):
        readTEMPtextures = line.split(";")
        readTEMPtextures[-1] = readTEMPtextures[-1].split("\n")[0]
        texture = PIL.Image.open(str(readTEMPtextures[0]))
        texture = texture.convert("RGBA")
        texture = Texture(texture)
        textureBlock[i] = [texture, readTEMPtextures[1], int(readTEMPtextures[2]), readTEMPtextures[3]]

    # SKY
img = PIL.Image.open("assest/textures/sky_color.png")
img = img.convert("RGB")
skyColorMap = []
for i in range(2400):
    skyColorMap.append([img.getpixel((i, 0))[0], img.getpixel((i, 0))[1], img.getpixel((i, 0))][2])

# STRUCTURES
biomes = os.listdir(f"assest/structures")
structures = {}
for i in range(len(biomes)):
    with open(f"assest/structures/{biomes[i - 1]}/{biomes[i - 1]}.txt", "r") as f:
        structuresTemp = []
        for line in f:
            tempLineSplit = (line.split(","))
            tempLineSplit[6] = tempLineSplit[6].split("\n")[0]
            structuresTemp.append(tempLineSplit + [0])

    structures[biomes[i - 1]] = structuresTemp

class Equipment(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, scale = (0.1,0.1))
        global eqMenage

        tempEquipment = 0

        for szer in range(10):
            eqMenage[("ID", szer)] = 0
            eqMenage[("Hot Bar", szer)] = Entity(position = ((szer - 5) * 1.1 + 0.5, -4.5),
                                                 model = 'cube', parent = self, scale = (1, 1),
                                                 texture = "assest/textures/hotBar.png")
            eqMenage[("Item", szer)] = Button(position = ((szer - 5) * 1.1 + 0.5, -4.5),
                                              model = 'assest/models/quad',
                                              texture = textureBlock[eqMenage[("ID", szer)]],
                                              color=color.white, parent=self, scale = (0.8, 0.8),
                                              on_click = self.equipmentSelect, always_on_top = True,
                                              highlight_color = color.white66, name = str(tempEquipment))
            eqMenage[("Count", szer)] = Text(position = (0.1, -0.2),
                                             scale = (10, 10),
                                             text = "",
                                             parent = eqMenage[("Item", szer)],
                                             always_on_top = True,
                                             name = str(tempEquipment))
            tempEquipment += 1


        eqMenage["Select"] = 1
        eqMenage["Big"] = Entity(parent = self,
                                 scale = (1, 1),
                                 visible = False,
                                 enabled = False)
        eqMenage["Big", "equipment"] = Entity(model = 'assest/models/quad',
                                              texture = 'assest/textures/equipment.png',
                                              color=color.white, parent=eqMenage["Big"],
                                              scale = (15,8))
        eqMenage[("Big", "Select")] = Entity(model = 'assest/models/quad',
                                             texture = 'assest/textures/air.png',
                                             color=color.white,
                                             parent=eqMenage["Big"],
                                             world_scale = (1,1))
        eqMenage[("Big", "Select", "Count")] = Text(position = (0.1, -0.2),
                                                    scale = (10, 10),text = "",
                                                    parent = eqMenage[("Big", "Select")],
                                                    always_on_top = True)
        eqMenage[("Big", "Select", "mode")] = 0
        eqMenage[("Big", "Select", "temp")] = []

        for szer in range(10, 26):
            eqMenage[("ID", szer)] = 0
            eqMenage[("Item", szer)] = Button(position = (-0.38 + (int((szer - 10) % 4) / 8), 0.3 - (int((szer - 10) / 4) / 5)),
                                              model = 'assest/models/quad',
                                              texture = textureBlock[eqMenage[("ID", szer)]],
                                              color=color.white, parent=eqMenage["Big", "equipment"],
                                              scale = (0.09, 0.16),
                                              always_on_top = True,
                                              on_click = self.equipmentSelect,
                                              name = str(tempEquipment))
            eqMenage[("Count", szer)] = Text(position = (0.1, -0.2),
                                             scale = (10, 10),
                                             text = "",
                                             parent = eqMenage[("Item", szer)],
                                             always_on_top = True,
                                             name = str(tempEquipment))
            tempEquipment += 1

        for i in range(0, 26):
            try:
                eqMenage[("ID", i)] = playerInfo[4][i][0]
                eqMenage[("Item", i)].texture = playerInfo[4][i][1]
                eqMenage[("Count", i)].text = playerInfo[4][i][2]
            except Exception:
                pass

    def equipmentSelect(self):
        if eqMenage[("Big", "Select", "mode")] == 0:
            if eqMenage[("Count", int(mouse.hovered_entity.name))].text != "":
                name = int(mouse.hovered_entity.name)
                eqMenage[("Big", "Select")].texture = mouse.hovered_entity.texture
                eqMenage[("Big", "Select", "Count")].text = eqMenage[("Count", name)].text
                eqMenage[("Big", "Select", "temp")] = [eqMenage[("Count", name)].text,
                                                       eqMenage[("ID", name)],
                                                       eqMenage[("Item", name)].texture,
                                                       int(mouse.hovered_entity.name)]
                eqMenage[("Count", name)].text = ""
                eqMenage[("ID", name)] = 0
                eqMenage[("Item", name)].texture = "assest/textures/vinet.png"
                eqMenage[("Big", "Select", "mode")] = 1

        if eqMenage[("Big", "Select", "mode")] == 1:
            name = int(mouse.hovered_entity.name)
            if int(mouse.hovered_entity.name) != eqMenage[("Big", "Select", "temp")][3] and eqMenage[("Count", name)].text == "":
                eqMenage[("Big", "Select")].texture = "assest/textures/air.png"
                eqMenage[("Big", "Select", "Count")].text = ""
                eqMenage[("Count", name)].text = eqMenage[("Big", "Select", "temp")][0]
                eqMenage[("ID", name)] = eqMenage[("Big", "Select", "temp")][1]
                eqMenage[("Item", name)].texture = eqMenage[("Big", "Select", "temp")][2]
                eqMenage[("Big", "Select", "mode")] = 0

            elif int(mouse.hovered_entity.name) != eqMenage[("Big", "Select", "temp")][3] and int(eqMenage[("Count", name)].text) + int(eqMenage[("Big", "Select", "temp")][0]) < 33 and eqMenage[("Big", "Select", "temp")][1] == eqMenage[("ID", name)]:
                eqMenage[("Big", "Select")].texture = "assest/textures/air.png"
                eqMenage[("Big", "Select", "Count")].text = ""
                eqMenage[("Count", name)].text = str(int(eqMenage[("Big", "Select", "temp")][0]) + int(eqMenage[("Count", name)].text))
                eqMenage[("ID", name)] = eqMenage[("Big", "Select", "temp")][1]
                eqMenage[("Item", name)].texture = eqMenage[("Big", "Select", "temp")][2]
                eqMenage[("Big", "Select", "mode")] = 0

            elif int(mouse.hovered_entity.name) != eqMenage[("Big", "Select", "temp")][3] and int(eqMenage[("Count", name)].text) + int(eqMenage[("Big", "Select", "temp")][0]) > 32 and eqMenage[("Big", "Select", "temp")][1] == eqMenage[("ID", name)]:
                eqMenage[("Big", "Select", "Count")].text = str(int(eqMenage[("Count", name)].text) + int(eqMenage[("Big", "Select", "temp")][0]) - 32)
                eqMenage[("Count", name)].text = "32"
                eqMenage[("Big", "Select", "mode")] = 2

        elif eqMenage[("Big", "Select", "mode")] == 2:
            name = int(mouse.hovered_entity.name)
            if eqMenage[("Count", name)].text == "":
                eqMenage[("Count", name)].text = eqMenage[("Big", "Select", "Count")].text
                eqMenage[("ID", name)] = eqMenage[("Big", "Select", "temp")][1]
                eqMenage[("Item", name)].texture = eqMenage[("Big", "Select", "temp")][2]
                eqMenage[("Big", "Select", "Count")].text = ""
                eqMenage[("Big", "Select")].texture = "assest/textures/air.png"
                eqMenage[("Big", "Select", "mode")] = 0


    def update(self):
        global eqMenage
        eqMenage[("Big", "Select")].position = mouse.position * 10

        for szer in range(0, 26):
            if eqMenage[("ID", szer)] == 0:
                eqMenage[("Item", szer)].texture = "assest/textures/vinet.png"
                eqMenage[("Count", szer)].text = ""
            else:
                eqMenage[("Item", szer)].texture = textureBlock[eqMenage[("ID", szer)]][0]

            if eqMenage[("Count", szer)].text == "0":
                eqMenage[("Count", szer)].text = ""
                eqMenage[("ID", szer)] = 0
                eqMenage[("Item", szer)].texture = "assest/textures/vinet.png"

    def input(self, key):
        global eqMenage
        if key == "tab":
            if eqMenage["Big"].visible == False:
                eqMenage["Big"].visible = True
                eqMenage["Big"].enabled = True
            else:
                eqMenage["Big"].visible = False
                eqMenage["Big"].enabled = False
        if key == "scroll down" or key == "scroll up":
            if key == "scroll down":
                eqMenage["Select"] -= 1
                if eqMenage["Select"] == 0:
                    eqMenage["Select"] = 10
            elif key == "scroll up":
                eqMenage["Select"] += 1
                if eqMenage["Select"] == 11:
                    eqMenage["Select"] = 1

            for szer in range(10):
                eqMenage[("Hot Bar", szer)].color = color.rgb(255, 255, 255)

            eqMenage[("Hot Bar", eqMenage["Select"] - 1)].color = color.rgb(150, 150, 150)

class Voxel(Button):
    def __init__(self, position = (0,0,0), textureBlock = textureBlock[0][0], model = 'cube', colid = "solid", **kwargs):
        super().__init__(parent = scene,
                         position = position,
                         model = f"assest/models/{model}",
                         texture = textureBlock,
                         color = light,
                         name = colid)
    def update(self):
        self.color = light
        if -9 > self.x - player.x or 11 < self.x - player.x or -5 > self.y - player.y or 7 < self.y - player.y:
            blocks[self.x, self.y][3] = 0
            destroy(self)

    def input(self, key):
        global eqMenage
        self.color = light
        if key == "left mouse down" and mouse.hovered_entity == self and textureBlock[blocks[self.x, self.y][int(self.z)]][2] < 100:
            temp = False
            for szer in range(0, 26):
                if eqMenage[("ID", szer)] == blocks[self.x, self.y][int(self.z)]:
                    eqMenage[("ID", szer)] = blocks[self.x, self.y][int(self.z)]
                    if eqMenage[("Count", szer)].text == "":
                        eqMenage[("Count", szer)].text = "1"
                        temp = True
                        break
                    elif int(eqMenage[("Count", szer)].text) < 32:
                        eqMenage[("Count", szer)].text = str(int(eqMenage[("Count", szer)].text) + 1)
                        temp = True
                        break

            if temp == False:
                for szer in range(0, 26):
                    if eqMenage[("ID", szer)] == 0 or eqMenage[("ID", szer)] == blocks[self.x, self.y][int(self.z)]:
                        eqMenage[("ID", szer)] = blocks[self.x, self.y][int(self.z)]
                        if eqMenage[("Count", szer)].text == "":
                            eqMenage[("Count", szer)].text = "1"
                            break
                        elif int(eqMenage[("Count", szer)].text) < 32:
                            eqMenage[("Count", szer)].text = str(int(eqMenage[("Count", szer)].text) + 1)
                            break

            blocks[self.x, self.y][int(self.z)] = 0

            destroy(self)
        elif key == "right mouse down" and mouse.hovered_entity == self:
            try:
                for i in range(3):
                    a = blocks[int(self.x + mouse.world_normal.x), int(self.y + mouse.world_normal.y)][i]

            except Exception:
                blocks[int(self.x + mouse.world_normal.x), int(self.y + mouse.world_normal.y)] = [0, 0, 0, 1]

            if eqMenage[("Count", eqMenage["Select"] - 1)].text != "":
                if blocks[int(self.x + mouse.world_normal.x), int(self.y + mouse.world_normal.y)][int(self.z + mouse.world_normal.z)] == 0:
                    eqMenage[("Count", eqMenage["Select"] - 1)].text = str(int(eqMenage[("Count", eqMenage["Select"] - 1)].text) - 1)
                    blocks[int(self.x + mouse.world_normal.x), int(self.y + mouse.world_normal.y)][int(self.z + mouse.world_normal.z)] = eqMenage[("ID", eqMenage["Select"] - 1)]

                    Voxel(position=(int(self.x + mouse.world_normal.x), int(self.y + mouse.world_normal.y), int(self.z + mouse.world_normal.z)),
                          textureBlock=textureBlock[blocks[int(self.x + mouse.world_normal.x), int(self.y + mouse.world_normal.y)][int(self.z + mouse.world_normal.z)]][0],
                          model=textureBlock[blocks[int(self.x + mouse.world_normal.x), int(self.y + mouse.world_normal.y)][int(self.z + mouse.world_normal.z)]][1],
                          colid=textureBlock[blocks[int(self.x + mouse.world_normal.x), int(self.y + mouse.world_normal.y)][int(self.z + mouse.world_normal.z)]][3])

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.color = color.red
        self.scale = Vec3(1, 1.8, 1)
        self.parent = scene
        self.position = (0,0,1)
        self.visible = True

    def input(self, key):
        pass

    def update(self):
        pass

class PlayerPart(Entity):
    def __init__(self, position = (0, 0, 0), scale = (1, 1, 1), texture = "brick", **kwargs):
        super().__init__()
        texture = load_texture(texture)
        self.model='assest/models/cube'
        self.color = color.random_color()
        self.scale = scale
        self.parent = player
        self.position = position
        self.visible = True
        self.texture = texture

    def update(self):
        self.color = light

class Hitboxes(Entity):
    def __init__(self, pos = (0,0,0), scale = (1,1,1),**kwargs):
        super().__init__()
        self.scale = scale
        self.model = 'cube'
        self.color = color.blue
        self.parent = player
        self.position = pos
        self.collider = 'box'
        self.visible = False

# SETTINGS
gamePath = sys.path[0]
app = Ursina()
application.development_mode = False
application.version = "1.0"
#window.fullscreen_size = window.screen_resolution
#window.fullscreen = True
window.borderless = True
show_ursina_splash = False
window.title = "CreyBlock Game"

player = Player()
sky = Sky()
eqMenage = {}
eq = Equipment()
light = 0
player.x = playerInfo[0]
player.y = playerInfo[1]
player.z = playerInfo[2]
camera.parent = player
camera.scale = Vec3(1, 0.55, 1)
camera.rotation_x = 7
camera.y = 3

def save():
    for i in range(playerInfo[3] - 1):
        if blocks[i][0] == 1:
            for a in range(100, -100, -1):
                blocks[i, a][3] = 0
    with open(f'assest/saves/save/worldSave.data', 'wb') as filehandle:
        pickle.dump(blocks, filehandle)

    playerInfo[0] = player.x
    playerInfo[1] = player.y
    playerInfo[2] = player.z


    for i in range(0, 26):
        try:
            playerInfo[4][i][0] = eqMenage[("ID", i)]
            playerInfo[4][i][1] = eqMenage[("Item", i)].texture
            playerInfo[4][i][2] = eqMenage[("Count", i)].text
        except Exception:
            playerInfo[4].append([])
            playerInfo[4][i].append(eqMenage[("ID", i)])
            playerInfo[4][i].append(eqMenage[("Item", i)].texture)
            playerInfo[4][i].append(eqMenage[("Count", i)].text)


    with open(f'assest/saves/save/playerSave.data', 'wb') as filehandle:
        pickle.dump(playerInfo, filehandle)
tick = 0
skyColor = 1200

# FIRST WORLDGEN
for szer in range(-16, 18):
    if blocks[int(player.x) + szer][3] == 0:
        worldGen(int(player.x) + szer)

for szer in range(-12, 14):
    if blocks[int(player.x) + szer][3] == 0:
        blocks[int(player.x) + szer][3] = biomGen.structurs(blocks[int(player.x) + szer][1])
        structursGen(int(player.x) + szer)


#Player
playerParts = {}
playerParts["Body"] = PlayerPart((0, 0.1, 0), (0.45, 0.4, 0.2), texture = "assest/textures/body.png")
playerParts["Head"] = PlayerPart((0, 0.4, 0), (0.3, 0.2, 0.2), texture = "assest/textures/head.png")
playerParts["LeftArm"] = PlayerPart((-0.37, 0.1, 0), (0.2, 0.38, 0.2), texture = "assest/textures/leftArm.png")
playerParts["RightArm"] = PlayerPart((0.37, 0.1, 0), (0.2, 0.38, 0.2), texture = "assest/textures/rightArm.png")
playerParts["LeftLeg"] = PlayerPart((-0.15, -0.31, 0), (0.2, 0.38, 0.2), texture = "assest/textures/leftLeg.png")
playerParts["RightLeg"] = PlayerPart((0.15, -0.31, 0), (0.2, 0.38, 0.2), texture = "assest/textures/rightLeg.png")

#Player Hitboxes
PlayerHitboxes = {}
PlayerHitboxes["Up 1"] = Hitboxes(pos=(0,0.48,0), scale=(0.7, 0.01, 0.1))
PlayerHitboxes["Up 2"] = Hitboxes(pos=(0,0.51,0), scale=(0.7, 0.01, 0.1))
PlayerHitboxes["Down 1"] = Hitboxes(pos=(0,-0.48,0), scale=(0.7, 0.01, 0.1))
PlayerHitboxes["Down 2"] = Hitboxes(pos=(0,-0.51,0), scale=(0.7, 0.01, 0.1))
PlayerHitboxes["Left 1"] = Hitboxes(pos=(-0.51,0,0), scale=(0.01, 0.7, 0.1))
PlayerHitboxes["Right 1"] = Hitboxes(pos=(0.51,0,0), scale=(0.01, 0.7, 0.1))
PlayerHitboxes["Front 1"] = Hitboxes(pos=(0,0,-0.17), scale=(0.7, 0.7, 0.0))
PlayerHitboxes["Front 2"] = Hitboxes(pos=(0,0,-0.2), scale=(0.7, 0.7, 0.01))
PlayerHitboxes["Back 1"] = Hitboxes(pos=(0,0,0.17), scale=(0.7, 0.7, 0.0))
PlayerHitboxes["Back 2"] = Hitboxes(pos=(0,0,0.2), scale=(0.7, 0.7, 0.01))

#Acceleration
accLeft = Vec2(0, 0)
accRight = Vec2(0, 0)
accJump = Vec2(0, 0)
accFall = Vec2(-1, -1)

acc = Vec2(0, 0)

def blockSolid(hitbox):
    if PlayerHitboxes[hitbox].intersects().entities != []:
        solidBlocks = 0
        for ent in PlayerHitboxes[hitbox].intersects().entities:
            if ent.name == "solid":
                solidBlocks += 1
        if solidBlocks >= 1:
            return True
        else:
            return False
    else:
        return False

def blockLiquid(hitbox):
    if PlayerHitboxes[hitbox].intersects().entities != []:
        liquidBlocks = 0
        for ent in PlayerHitboxes[hitbox].intersects().entities:
            if ent.name == "liquid":
                liquidBlocks += 1
        if liquidBlocks == len(PlayerHitboxes[hitbox].intersects().entities):
            return True
        else:
            return False
    else:
        return False


def update():
    #print(player.position)
    global skyColor
    global light
    accRight.x *= 0.7
    accLeft.x *= 0.7
    acc.x = accRight.x + accLeft.x
    accJump.y *= 0.9
    acc.y = accFall.y + 1 + accJump.y

    if accJump.y < 0.1:
        accJump.y = 0
        if not blockSolid("Down 2"):
            accFall.y *= 1.003
        elif blockLiquid("Down 2"):
            accFall.y *= 1
        else:
            accFall.y = -1

    player.position += acc


    accRight.x += held_keys['d'] * time.dt * 2
    accLeft.x -= held_keys['a'] * time.dt * 2

    if blockSolid("Left 1"):
        accLeft.x = 0
    if blockSolid("Right 1"):
        accRight.x = 0
    if blockSolid("Down 2"):
        acc.y = 0
        accFall.y = -1
    if blockSolid("Down 1"):
        player.y += 1 * time.dt * 5
    if blockSolid("Up 1"):
        accJump.y = 0
    if blockSolid("Up 2"):
        player.y -= 0.1


    if not blockSolid("Front 2") and -0.2 < player.z:
        player.z -= (held_keys['s'] * time.dt * 2)
    elif blockSolid("Front 1"):
        player.z += 0.1

    if not blockSolid("Back 2") and 2.2 > player.z:
        player.z += (held_keys['w'] * time.dt * 2)
    elif blockSolid("Back 1"):
        player.z -= 0.1

    # ROTATING HEAD
    playerParts["Head"].rotation_y = math.atan2(playerParts["Head"].position.x - mouse.x, playerParts["Head"].position.y - mouse.y) * math.pi * 18

    worldGen(int(player.x) - 16)
    worldGen(int(player.x) + 18)

    if blocks[int(player.x) - 12][3] == 0:
        blocks[int(player.x) - 12][3] = biomGen.structurs(blocks[int(player.x) - 12][1])
        structursGen(int(player.x) - 12)

    if blocks[int(player.x) + 14][3] == 0:
        blocks[int(player.x) + 14][3] = biomGen.structurs(blocks[int(player.x) + 14][1])
        structursGen(int(player.x) + 14)

    for szer in range(-8, 10):
        for wys in range(-4, 6):
            try:
                if blocks[int(player.x) + szer, int(player.y) + wys][3] == 0:
                    for i in range(3):
                        if blocks[int(player.x) + szer, int(player.y) + wys][i] != 0:
                            Voxel(position = (int(player.x) + szer, int(player.y) + wys, 0 + i),
                                  textureBlock = textureBlock[blocks[int(player.x) + szer, int(player.y) + wys][i]][0],
                                  model = textureBlock[blocks[int(player.x) + szer, int(player.y) + wys][i]][1],
                                  colid = textureBlock[blocks[int(player.x) + szer, int(player.y) + wys][i]][3])

                    blocks[int(player.x) + szer, int(player.y) + wys][3] = 1
            except Exception:
                pass

    mediumColor = int(((skyColorMap[int(skyColor)][0] + int(skyColorMap[int(skyColor)][1]) + int(skyColorMap[int(skyColor)][2])) / 3))
    mediumColor1 = int((skyColorMap[int(skyColor)][0] + mediumColor + mediumColor + mediumColor) / 4)
    mediumColor2 = int((skyColorMap[int(skyColor)][1] + mediumColor + mediumColor + mediumColor) / 4)
    mediumColor3 = int((skyColorMap[int(skyColor)][2] + mediumColor + mediumColor + mediumColor) / 4)
    light = color.rgb(mediumColor1 + 20, mediumColor2 + 20, mediumColor3 + 20)
    if skyColor >= 2390:
        skyColor = 0
    else:
        skyColor += 0.1
    sky.color = color.rgb(skyColorMap[int(skyColor)][0], skyColorMap[int(skyColor)][1], skyColorMap[int(skyColor)][2])

def input(key):
    if key == 'escape':
        save()
        application.quit()

    if key == 'space' and blockSolid("Down 2"):
        accJump.y += 0.285

app.run()
