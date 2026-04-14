import random
import pygame

from snake import Snake


class Apple:
    def __init__(self):
        self.pos = [0,0]
        self.taille_bloc = 20
        self.safe = []

    def place(self,snake:Snake):
        self.safe = [[x*self.taille_bloc,y*self.taille_bloc] for x in range(0,25) for y in range(0,25)]
        print(self.safe)
        print(snake.body)
        for bloc in snake.body:
            self.safe.remove(bloc)
        self.pos = random.choice(self.safe)

    def drawn(self,screen):
        pygame.draw.circle(screen, (255, 0, 0), [self.pos[0]+self.taille_bloc/2,self.pos[1]+self.taille_bloc/2], self.taille_bloc/2)