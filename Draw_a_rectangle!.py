import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Draw a Rectangle!')
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()

pygame.quit()