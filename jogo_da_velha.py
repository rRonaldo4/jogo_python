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

screen = pygame.display.set_mode((600, 600))
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
        if event.type == pygame.MOUSEBUTTONDOWN: # evento de click do mouse
            print('clicou na tela')
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 3):
                cor_fundo = 1
    # Desenha o tabuleiro
    pygame.draw.line(screen, 'white',(200, 0),(200, 600), 5)
    pygame.draw.line(screen, 'white',(400, 0),(400, 600), 5)
    pygame.draw.line(screen, 'white',(0, 200),(600, 200), 5)
    pygame.draw.line(screen, 'white',(0, 400),(600, 400), 5)

    screen.blit(personagem_x, (65, 20))
    screen.blit(personagem_y, (260, 30))
    screen.blit(personagem_x, (460, 30))

    # if cor_fundo == 1:
    #     screen.blit(personagem_x, (60, 30))
    # elif cor_fundo == 2:
    #     screen.blit(personagem_y, (195, 195))
        
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()