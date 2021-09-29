import pygame

from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

##################### Audio #############
pygame.mixer.music.set_volume(0.05)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_bubble_pop.wav')


############## Tamanho e posição dos obiguetos #########
largura = 640
altura = 480

x_cobra = int(largura/2)
y_cobra = int(altura/2)

x_maca = randint(40,600)
y_maca = randint(50,430)


################# Controles ###############

velocidade = 20
x_controle = velocidade
y_controle = 0

################ Fonte #####################
pontos = 0
fonte = pygame.font.SysFont('gabriola', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo do victor')


################### Objeto cobra ###########
relogio = pygame.time.Clock()

lista_cobra = []

comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:

        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y  

        pygame.draw.circle(tela, (0,255,0), (XeY[0], XeY[1]), 9)

################ Cores ##########################
while True:
    relogio.tick(100)
    tela.fill((0,0,0))
    msg = f'Pontos: {pontos}'
    texto_view = fonte.render(msg, True, (255,255,255))

################# Configuração das teclas de controle #########
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           exit()
    
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

            x_cobra = x_cobra + x_controle
            y_cobra = y_cobra + y_controle

        '''
       if pygame.key.get_pressed()[K_a]:
            x_cobra = x_cobra-20
       if pygame.key.get_pressed()[K_d]:
           x_cobra = x_cobra+20
       if pygame.key.get_pressed()[K_w]:
           y_cobra = y_cobra-20
       if pygame.key.get_pressed()[K_s]:
           y_cobra = y_cobra+20 '''

######################### Objetos ###################################
        cobra = pygame.draw.circle(tela, (0,255,0), (x_cobra,y_cobra),9)
        maca = pygame.draw.circle(tela, (255,0,0), (x_maca,y_maca),9)

############################ colisões #############################
        if cobra.colliderect(maca):
           x_maca = randint(40,600)
           y_maca = randint(50,430)
           pontos = pontos + 1
           barulho_colisao.play()
           comprimento_inicial = comprimento_inicial + 1

        lista_cabeca = []
        lista_cabeca.append(x_cobra)
        lista_cabeca.append(y_cobra)
       
        lista_cobra.append(lista_cabeca)


################ colisão da cobra nela mesma #####################
        

        if len(lista_cobra) > comprimento_inicial:
           del lista_cobra[0]
           

        aumenta_cobra(lista_cobra)

        tela.blit(texto_view, (450,40))

        '''
         pygame.draw.circle(tela, (0,0,255), (450,260), 40)
         pygame.draw.line(tela, (255,255,0), (360,0), (360,480), 5)'''

        pygame.display.update()
