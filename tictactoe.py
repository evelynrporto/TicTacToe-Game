import pygame, sys
import numpy as np

pygame.init()

#constantes
WIDTH = 600 
HEIGHT = 600
LARGURA_LINHA = 15
#cores
BACKGROUND = (28,170,156)
COR_LINHA = (23,145,135)
#matriz
MAT_LINHAS = 3
MAT_COLUNAS = 3
#medidas circulo
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (255, 255, 255, 255)
#medidas quadrado
CROSS_COLOR = (84, 84, 84)
CROSS_WIDTH = 25
SPACE = 55 


#configurações da tela inicial
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
tela.fill(BACKGROUND)

matriz = np.zeros( (MAT_LINHAS, MAT_COLUNAS) )

def fazer_linhas():
    #linhas horizontais
    pygame.draw.line( tela, COR_LINHA, (0, 200), (600,200), LARGURA_LINHA )
    pygame.draw.line( tela, COR_LINHA, (0, 400), (600,400), LARGURA_LINHA )
    #linhas verticais
    pygame.draw.line( tela, COR_LINHA, (200,0), (200,600), LARGURA_LINHA )
    pygame.draw.line( tela, COR_LINHA, (400,0), (400,600), LARGURA_LINHA )

def desenhar_formas():
    for row in range(MAT_LINHAS):
        for col in range(MAT_COLUNAS):
            if matriz[row][col] == 1:
                pygame.draw.circle(tela, CIRCLE_COLOR, (int( col * 200 + 100), int (row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif matriz[row][col] == 2:
                pygame.draw.line(tela, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH )
                pygame.draw.line(tela, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH )
                 
def mark_square(row, col, player): 
    matriz[row][col] = player

def quadrados_disponiveis(row, col):
    return matriz[row][col] == 0


fazer_linhas()

player = 1

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_linha = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if quadrados_disponiveis (clicked_linha, clicked_col):
                if player == 1:
                    mark_square(clicked_linha, clicked_col, 1)
                    player = 2

                elif player == 2:
                    mark_square(clicked_linha, clicked_col, 2)
                    player = 1

                desenhar_formas()
        

    pygame.display.update()
