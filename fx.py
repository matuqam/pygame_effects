from imports import *

class Fx:
    def __init__(self, rect=None, ticks=None, type=None):
        self.rect = rect
        self.ticks = ticks
        self.type = type
    
    def circle(self, surface, pos, radius=24, width=4):
        pygame.draw.circle(surface, BLUE, pos, radius, width)