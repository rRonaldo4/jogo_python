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

apresenta_personagem = 0 # azul
x = 0
y = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # evento de click do mouse
            print('clicou na tela')
            click_pos = pygame.mouse.get_pos() # posição do mouse quando houve o evento de click
            print('eixo x:', click_pos[0])
            print('eixo y:', click_pos[1])
            x = click_pos[0]
            y = click_pos[1]
            apresenta_personagem = apresenta_personagem + 1
            if(apresenta_personagem >= 10):
                screen.fill('black')
                apresenta_personagem = 0
    # Desenha o tabuleiro
    #                                origem    destino
    #                                (x, y)   (x, y)
    pygame.draw.line(screen, 'white',(200, 0),(200, 600), 5)
    pygame.draw.line(screen, 'white',(400, 0),(400, 600), 5)
    pygame.draw.line(screen, 'white',(0, 200),(600, 200), 5)
    pygame.draw.line(screen, 'white',(0, 400),(600, 400), 5)

    if x > 0 and x < 200 and y < 200:
        screen.blit(personagem_x, (60, 30)) # 1

    elif x >= 200 and x < 400 and y < 200:
        screen.blit(personagem_y, (260, 30)) # 2

    elif x >= 400 and y < 200:
        screen.blit(personagem_y, (460, 30)) # 3

    elif x < 200 and y >= 200 and y < 400:
        screen.blit(personagem_x, (60, 230)) # 4

    elif x > 200 and x < 40 and y > 200 and y <= 400:
        screen.blit(personagem_y, (260, 230)) # 5

    elif x >= 400 and y > 200 and y <= 400:
        screen.blit(personagem_y, (460, 230)) # 6

    elif x < 200 and y >= 400:
        screen.blit(personagem_x, (60, 430)) # 7

    elif x >= 200 and y < 400 and y >=400:
        screen.blit(personagem_y, (260, 430)) # 8
        
    elif x >= 400 and y >= 400:
        screen.blit(personagem_y, (460, 430)) # 9
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()