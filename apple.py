import random
import pygame

class Apple:
    def __init__(self):
        self.pos = [0,0]
        self.taille_bloc = 20

    def place(self):
        self.pos[0] = random.randint(1,23)*self.taille_bloc
        self.pos[1] = random.randint(1,23)*self.taille_bloc

    def drawn(self,screen):
        pygame.draw.rect(screen, (255, 0, 0), [self.pos[0],self.pos[1], self.taille_bloc, self.taille_bloc])