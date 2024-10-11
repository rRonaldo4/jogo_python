# https://www.pygame.org/ - documentação py game
# Example file showing a basic pygame "game loop"

# comandos - para criar repositório

# echo "# jogo_python" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/rRonaldo4/jogo_python.git
# git push -u origin main

import pygame

# pygame setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('jogo da velha - by ronaldo')
clock = pygame.time.Clock()

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100, True, True)
running = True

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'red')

cor_fundo = 1 # azul

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('clicou na tela')
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 3):
                cor_fundo = 1

    if cor_fundo == 1:
        screen.fill('black')
        screen.blit(personagem_x, (250, 250))
    elif cor_fundo == 2:
        screen.fill('black')
        screen.blit(personagem_y, (250, 250))
    else:
        screen.fill('purple')

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()