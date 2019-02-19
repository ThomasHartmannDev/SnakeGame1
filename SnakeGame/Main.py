import pygame
from random import randrange

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
cinza = (90,90,90)
try:
    print(pygame.init())
except:
    print("error")

    
largura = 640
altura = 520
tamanho = 10
placar = 40
relogio = pygame.time.Clock()

fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Pygame Thomas")
font = pygame.font.SysFont(None,25)            

def text(msg, cor, tam, posx, posy):
    font = pygame.font.SysFont(None,tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1,(posx,posy))

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo,branco,(XY[0],XY[1],tamanho,tamanho))

def maca(maca_x, maca_y):
    pygame.draw.rect(fundo,vermelho,(maca_x,maca_y,tamanho,tamanho))

def jogo():
    pos_x = randrange(0,largura - tamanho,10)
    pos_y = randrange(0,altura - tamanho - placar,10)
    maca_x = randrange(0,largura - tamanho ,10)
    maca_y = randrange(0,altura - tamanho - placar,10)
    vel_x = 0
    vel_y = 0     
    sair = True
    fimdejogo = False
    menu = True
    CobraXY = []
    CobraComp = 1
    Score = 0
    while sair:
       
        while fimdejogo:
            fundo.fill(preto)
            text("GAME OVER",vermelho,50,205,130)
            text("Para jogar novamente aperte R", branco, 25, 190,180)
            text("Para sair aperte espaço", branco, 25, 225,210)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pos_x = randrange(0,largura - tamanho,10)
                        pos_y = randrange(0,altura - tamanho,10)
                        maca_x = randrange(0,largura - tamanho,10)
                        maca_y = randrange(0,altura - tamanho,10)
                        vel_x = 0
                        vel_y = 0     
                        sair = True
                        fimdejogo = False
                        CobraXY = []
                        CobraComp = 1
                        Score = 0 
                    if event.key == pygame.K_SPACE:
                        sair = False
                        fimdejogo = False
                        print("apertou para sair")
        for event in pygame.event.get():
        #print(event)
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and vel_x != tamanho:
                    vel_y = 0
                    vel_x = -tamanho
                if event.key == pygame.K_RIGHT and vel_x != -tamanho:
                    vel_y = 0
                    vel_x = tamanho
                if event.key == pygame.K_UP and vel_y != tamanho:
                    vel_x = 0
                    vel_y = -tamanho
                if event.key == pygame.K_DOWN and vel_y != -tamanho:
                    vel_x = 0
                    vel_y = tamanho

                if event.key == pygame.K_a and vel_x != tamanho:
                    vel_y = 0
                    vel_x = -tamanho
                if event.key == pygame.K_d and vel_x != -tamanho:
                    vel_y = 0
                    vel_x = tamanho
                if event.key == pygame.K_w and vel_y != tamanho:
                    vel_x = 0
                    vel_y = -tamanho
                if event.key == pygame.K_s and vel_y != -tamanho:
                    vel_x = 0
                    vel_y = tamanho

        if sair:
            fundo.fill(preto)
            pos_x += vel_x
            pos_y += vel_y

            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0,largura - tamanho,10)
                maca_y = randrange(0,altura - tamanho - placar,10)
                CobraComp += 1
                Score +=10


            if pos_x < 0 or pos_x + tamanho> largura: 
                fimdejogo = True
            if pos_y < 0 or pos_y + tamanho > altura - placar: 
                fimdejogo = True

            CobraInicio = []
            CobraInicio.append(pos_x)
            CobraInicio.append(pos_y)
            CobraXY.append(CobraInicio)
            if len(CobraXY) > CobraComp:
                del CobraXY[0]
            
            if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                fimdejogo = True

            cobra(CobraXY)
            maca(maca_x,maca_y)

            pygame.draw.rect(fundo,cinza,(0,altura-placar,largura,placar))
            text("Score : {}".format(Score),branco,40,10,altura-30)
            pygame.display.update()
            relogio.tick(20)
jogo()     
pygame.quit()