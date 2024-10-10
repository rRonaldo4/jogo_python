# https://www.pygame.org/ - documentação py game
# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

cor_fundo = 1 # azul
cor_fundo = 2 # vermelho

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('clicou na tela')
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 4):
                cor_fundo = 1

    if cor_fundo == 1:
        screen.fill('blue')
    elif cor_fundo == 2:
        screen.fill('red')
    elif cor_fundo == 3:
        screen.fill('black')
    else:
        screen.fill('green')

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()