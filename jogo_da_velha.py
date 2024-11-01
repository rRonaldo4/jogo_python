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

# ------------------------------------------------------------------

# git pull origin main

# git config --global user.name
# git config --global user.email
# git add .
# git commit -m 'nome da atualização'
# git push origin main
# git status

import pygame

# pygame setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('jogo da velha - by ronaldo')
clock = pygame.time.Clock()

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100, True, True)
running = True

personagem_x = fonte_quadrinhos.render('X', True, 'pink')
personagem_o = fonte_quadrinhos.render('O', True, 'yellow')

jogador_atual = personagem_x # inicializa o jogo com x

rodadas = 0 
tabuleiro_desenhado = False
coordenada_x = 0
coordenada_y = 0

q1 = ''
q2 = ''
q3 = ''

q4 = ''
q5 = ''
q6 = ''

q7 = ''
q8 = ''
q9 = ''


def desenha_tabuleiro(espessura, cor):
    # Desenha o tabuleiro
    #                                 origem    destino
    #                                (x,   y) (x,     y)
    pygame.draw.line(screen, cor,(200, 0),(200, 600), espessura)
    pygame.draw.line(screen, cor,(400, 0),(400, 600), espessura)
    pygame.draw.line(screen, cor,(0, 200),(600, 200), espessura)
    pygame.draw.line(screen, cor,(0, 400),(600, 400), espessura)

def faz_jogada():
    global q1, q2, q3, q4, q5, q6, q7, q8, q9
    status = True
    if q1 == '' and coordenada_x > 0 and coordenada_x < 200 and coordenada_y < 200:
        screen.blit(jogador_atual,(60,30))  #primeiro
        q1 = jogador_atual

    elif q2 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y < 200:
        screen.blit(jogador_atual,(260,30)) #segundo
        q2 = jogador_atual

    elif q3 == '' and coordenada_x >= 400 and coordenada_y < 200:
        screen.blit(jogador_atual,(460,30)) #terceiro
        q3 = jogador_atual

    elif q4 == '' and coordenada_x < 200 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(60,230))  #quarto
        q4 = jogador_atual

    elif q5 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(260,230)) #quinto
        q5 = jogador_atual

    elif q6 == '' and coordenada_x >= 400 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(460,230)) #sexto
        q6 = jogador_atual

    elif q7 == '' and coordenada_x < 200 and coordenada_y >= 400:
        screen.blit(jogador_atual,(60,430))  #setimo
        q7 = jogador_atual

    elif q8 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 400:
        screen.blit(jogador_atual,(260,430)) #oitavo
        q8 = jogador_atual

    elif q9 == '' and coordenada_x >= 400 and coordenada_y >= 400:
        screen.blit(jogador_atual,(460,430)) #nono
        q9 = jogador_atual
    else:
        status = False
    return status

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

            if rodadas >= 9:
                screen.fill('black')
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                tabuleiro_desenhado = False

            if(faz_jogada()):
                rodadas = rodadas + 1
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                else: 
                    jogador_atual = personagem_x

            faz_jogada()

    if tabuleiro_desenhado == False:               
            desenha_tabuleiro(10, 'green')
            q1 = ''
            q2 = ''
            q3 = ''

            q4 = ''
            q5 = ''
            q6 = ''

            q7 = ''
            q8 = ''
            q9 = ''
            tabuleiro_desenhado = True
    # faz_jogada() apagar
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()