import ursina
from ursina import *

app = Ursina()

class Menu(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, position=(0,0))
        backgrond = Entity(parent = self, color = color.azure, model = "quad", scale = (2, 1))
        self.guiButtons = ["singleplayer", "multiplayer", "options", "packets", "exit"]
        for i in range(5):
            self.guiButtons[i] = Button(parent = self, color = color.white, model = "cube", scale = (0.33, 0.165), position = (-0.7 + (i * 0.35), 2), texture = f"assest/textures/gui/{self.guiButtons[i]}.png", name = "tryb")
            self.guiButtons[i].animate_position((-0.7 + (i * 0.35), -0.415), 2, delay = i)

    def update(self):
        for i in range(5):
            if float(self.guiButtons[i].y) == -0.4000000059604645:
                self.guiButtons[i].y = -0.415
        if mouse.hovered_entity != None and mouse.hovered_entity.name == "tryb":
            mouse.hovered_entity.y = -0.4

menu = Menu()

app.run()