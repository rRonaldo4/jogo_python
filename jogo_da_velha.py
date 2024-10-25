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
personagem_o = fonte_quadrinhos.render('O', True, 'red')

jogador_atual = personagem_x # inicializa o jogo com x

rodadas = 0 

coordenada_x = 0
coordenada_y = 0

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
            coordenada_x = click_pos[0]
            coordenada_y = click_pos[1]
            rodadas = rodadas + 1
            if rodadas >= 10:
                screen.fill('black')
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0

            if rodadas != 1:
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                
                else:
                    jogador_atual = personagem_x
            else: 
                jogador_atual = personagem_x
                
            

    # Desenha o tabuleiro
    #                                origem    destino
    #                                (x, y)   (x, y)
    pygame.draw.line(screen, 'white',(200, 0),(200, 600), 5)
    pygame.draw.line(screen, 'white',(400, 0),(400, 600), 5)
    pygame.draw.line(screen, 'white',(0, 200),(600, 200), 5)
    pygame.draw.line(screen, 'white',(0, 400),(600, 400), 5)

    if coordenada_x > 0 and coordenada_x < 200 and coordenada_y < 200:
        screen.blit(jogador_atual,(60,30))  #primeiro

    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y < 200:
        screen.blit(jogador_atual,(260,30)) #segundo

    elif coordenada_x >= 400 and coordenada_y < 200:
        screen.blit(jogador_atual,(460,30)) #terceiro

    elif coordenada_x < 200 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(60,230))  #quarto

    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(260,230)) #quinto

    elif coordenada_x >= 400 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(460,230)) #sexto

    elif coordenada_x < 200 and coordenada_y >= 400:
        screen.blit(jogador_atual,(60,430))  #setimo

    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 400:
        screen.blit(jogador_atual,(260,430)) #oitavo

    elif coordenada_x >= 400 and coordenada_y >= 400:
        screen.blit(jogador_atual,(460,430)) #nono
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()