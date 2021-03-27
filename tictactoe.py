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
#medidas x
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

def is_matriz_full():
    for row in range(MAT_LINHAS):
        for col in range(MAT_COLUNAS):
            if matriz[row][col] == 0:
                return False
    return True

def check_win(player):
    #verificar linha vertical win
    for col in range(MAT_COLUNAS):
        if matriz[0][col] == player and matriz[1][col] == player and matriz[2][col] == player:
            desenhar_vertical_win(col, player)
            return True

    #verificar linha horizontal win
    for row in range(MAT_LINHAS):
        if matriz[row][0] == player and matriz[row][1] == player and matriz[row][2] == player:
            desenhar_horizontal_win(row, player)
            return True

    #verificar asc diagonal linha win
    if matriz[2][0] == player and matriz[1][1] == player and matriz[0][2] == player:
        desenhar_asc_diagonal(player)
        return True
    
    #verificar desc diagonal linha win
    if matriz[0][0] == player and matriz[1][1] == player and matriz[2][2] == player:
        desenhar_desc_diagonal(player)
        return True

    return False

def desenho_vertical_win(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line( tela, color, (posX, 15), (posX, HEIGHT - 15), 15 )

def desenhar_horizontal_win(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line (tela, color, (15, posY), (WIDTH - 15, posY), 15)

def desenhar_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( tela, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def desenhar_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(tela, color, (15,15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
    pass

fazer_linhas()

player = 1
game_over = False

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_linha = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if quadrados_disponiveis (clicked_linha, clicked_col):
                if player == 1:
                    mark_square(clicked_linha, clicked_col, 1)
                    if check_win (player):
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_square(clicked_linha, clicked_col, 2)
                    if check_win (player):
                        game_over = True                   
                    player = 1

                desenhar_formas()
        

    pygame.display.update()
