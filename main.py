import pygame

from apple import Apple
from snake import Snake

pygame.init()

LARGEUR = 500
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
font = pygame.font.SysFont('Arial', 50) # Font name and size

horloge = pygame.time.Clock()
vitesse=5

def game():
    game_over = False

    score = 0

    snake = Snake()

    apple = Apple()
    apple.place()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != "right":
                    snake.direction = "left"
                elif event.key == pygame.K_RIGHT and snake.direction != "left":
                    snake.direction = "right"
                elif event.key == pygame.K_UP and snake.direction != "down":
                    snake.direction = "up"
                elif event.key == pygame.K_DOWN and snake.direction != "up":
                    snake.direction = "down"

        fenetre.fill((0,0,0))
        pygame.draw.rect(fenetre, (200,200,200), [[0,500],[500,600]])
        apple.drawn(fenetre)
        snake.move()
        if snake.check_wall_collision():
            print("game over")
            game_over = True

        if snake.check_collision():
            print("game over")
            game_over = True

        if snake.body[0] == apple.pos:
            apple.place()
            snake.body.append(snake.body[0])
            score += 1

        snake.draw(fenetre)

        score_text = font.render("Score : " + str(score), True, (0, 0, 0))
        fenetre.blit(score_text, (175, 525))

        pygame.display.update()
        horloge.tick(vitesse)

if __name__ == "__main__":
    game()