from typing import List, Dict, Tuple

import pygame
from pygame.locals import *

import engine
from engine import *
import fx


SCREEN_SIZE = (800, 600)
DISPLAY_SIZE = (600, 450)

pygame.init()
display = pygame.display.set_mode(SCREEN_SIZE)
camera = Camera(display)
engine.camera = camera

reminders = Reminders()
engine.reminders = reminders

# Protagonist is controlled
protagonist = Entity(Rect(0,0, 16, 16), color=(250,250,250), speed=2)
statics = []
for i in range(20):
    entity = Entity(Rect(i*20 + 20, i*20, 16, 16), parallax=1, color=(250,150,150), speed=1)
    entity.add_destination(Vector2d(randint(camera.rect.x, camera.rect.width),
                                    randint(camera.rect.y, camera.rect.height)))
    entity.add_destination(Vector2d(randint(camera.rect.x, camera.rect.width),
                                    randint(camera.rect.y, camera.rect.height)))
    statics.append(entity)

# elements = statics + [protagonist]
elements = Entities(protagonist, statics)

def main_loop():
    while True:
        for event in pygame.event.get():
            EventManager.manage_event(event, protagonist)
        
        display.fill(color=(150,150,150))

        reminders.tick()

        camera.move()
        # camera.shake()

        elements.tick()

        protagonist.move()

        for element in elements.entities:
            reminders.add_reminder(Reminder(fx.Fx(), 
                    fx.Fx().circle,
                    {'surface': camera.surface, 'pos': (element.rect.centerx, element.rect.centery)},
                    30, 0))
            element.move()

        for element in sorted(elements.entities+[protagonist], key=lambda e: e.parallax, reverse=False):
            pygame.draw.rect(camera.surface, color=element.color, rect=camera_draw(camera, element.rect, element.parallax))

        pygame.display.update()


main_loop()
