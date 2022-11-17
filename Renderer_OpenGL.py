import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model

from tkinter import *
from tkinter import ttk

""" 
PARA GIRAR LA CAMARA SE UTILIZA LAS TECLAS 
    W
  A S D

Para acer zoom in se utiliza la tecla 

 O

Para hacer zoom out se utiliza la tecla:

p

 """
def changeModel(ren: Renderer, index: int, models: list):
    tupl_model = models[index]
    ren.scene = []
    ren.scene.append(tupl_model[1])
    ren.setupCameraToRotate(tupl_model[1], tupl_model[2], tupl_model[2]/2, tupl_model[2]*2)
    print(tupl_model[0])


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Use WASD to move camera around model").grid(column=0, row=0)
ttk.Label(frm, text="Use IJKL to move pointlight in scene").grid(column=0, row=1)
ttk.Label(frm, text="Press F1 to show model sword").grid(column=0, row=2)
ttk.Label(frm, text="Press F2 to show model gun").grid(column=0, row=3)
ttk.Label(frm, text="Press F3 to show model barrel").grid(column=0, row=4)
ttk.Label(frm, text="Press F4 to show model pumpkin").grid(column=0, row=5)
ttk.Label(frm, text="Press F5 to show model tree").grid(column=0, row=6)
ttk.Label(frm, text="Use O to zoom in into the model, and P to zoom out").grid(column=0, row=7)
ttk.Button(frm, text="Go to scene", command=root.destroy).grid(column=0, row=8)
root.mainloop()

width = 960
height = 540

deltaTime = 0.0

pygame.init()
pygame.mixer.music.load('./music/megalovania.mp3')
pygame.mixer.music.play(3)
screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

face = Model("model.obj", 'model.bmp')
barrel = Model('./models/barrel/barrel.obj','./models/barrel/poison_barrel_text.bmp' )
gun = Model('./models/gun/gun.obj', './models/gun/gun.bmp')
sword = Model('./models/sword/sword.obj', './models/sword/sword.bmp')
pumpkin = Model('./models/pumpkin/pumpkin.obj', './models/pumpkin/pumpkin.bmp')
tree = Model('./models/tree/tree.obj', './models/tree/tree.bmp')





myObjects = [
    ("Sword", sword, 80),
    ("Handgun", gun, 5),
    ("Barrel", barrel, 5),
    ("Pumpkin", pumpkin, 3),
    ('Tree', tree, 20)
]
index_model = 0

changeModel(rend, index_model, myObjects)

isRunning = True
while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_1:
                rend.filledMode()
            elif event.key == pygame.K_2:
                rend.wireframeMode()

    if keys[K_LEFT]:
        rend.camPosition.x -= 10 * deltaTime
    elif keys[K_RIGHT]:
        rend.camPosition.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.camPosition.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.camPosition.y -= 10 * deltaTime
    elif keys[K_j]:
        rend.pointLight.x -= 10 * deltaTime
    elif keys[K_l]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_i]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_k]:
        rend.pointLight.y -= 10 * deltaTime
    elif keys[K_a]:
        rend.rotateLeft()
    elif keys[K_d]:
        rend.rotateRight()
    elif keys[K_w]:
        rend.rotateUp()
    elif keys[K_s]:
        rend.rotateDown()
    elif keys[K_o]:
        rend.zoomIn()
    elif keys[K_p]:
        rend.zoomOut()
    elif keys[K_F1] or keys[K_F2] or keys[K_F3] or keys[K_F4] or keys[K_F5]:
        new_index = 0 if keys[K_F1] else 1 if keys[K_F2] else 2 if keys[K_F3] else 3 if keys[K_F4] else 4
        if not new_index == index_model:
            changeModel(rend, new_index, myObjects)
            index_model = new_index

    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime
    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
