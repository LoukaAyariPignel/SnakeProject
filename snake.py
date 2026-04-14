import pygame

class Snake:
    def __init__(self):
        self.body = [[300, 200]]
        self.size = 1
        self.direction = "down"
        self.taille_bloc = 20

    def move(self):
        tete_x = self.body[0][0]
        tete_y = self.body[0][1]

        if self.direction == "left":
            tete_x -= self.taille_bloc
        elif self.direction == "right":
            tete_x += self.taille_bloc
        elif self.direction == "up":
            tete_y -= self.taille_bloc
        elif self.direction == "down":
            tete_y += self.taille_bloc

        self.body.insert(0, [tete_x, tete_y])

        if len(self.body) > self.size:
            self.body.pop()

    def check_collision(self):
        for bloc in self.body[1:]:
            if self.body[0] == bloc:
                return True
        return False

    def check_wall_collision(self):
        if self.body[0][0] >= self.taille_bloc*25 or self.body[0][1] >= self.taille_bloc*25:
            return True
        if self.body[0][0] <= 0 or self.body[0][1] <= 0:
            return True
        return False

    def draw(self, screen):
        for bloc in self.body:
            pygame.draw.rect(screen, (0, 255, 0), [bloc[0], bloc[1], self.taille_bloc, self.taille_bloc])