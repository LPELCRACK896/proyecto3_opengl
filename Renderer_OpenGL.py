import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model
""" 
PARA GIRAR LA CAMARA SE UTILIZA LAS TECLAS 
    W
  A S D

Para acer zoom in se utiliza la tecla 

 O

Para hacer zoom out se utiliza la tecla:

p

 """
width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

face = Model("model.obj", 'model.bmp')

face.position.z = -5

rend.scene.append( face )

rend.setupCameraToRotate(face, 5)

isRunning = True
print(rend.camPosition)
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
    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime
    #print(deltaTime)

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
