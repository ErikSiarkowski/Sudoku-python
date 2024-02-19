import pygame as pg
import random
import math

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (139, 188, 252)
azul_claro = (150, 196, 255)
azul_escuro = (66, 140, 237)
cor_adjacente = (183, 211, 247)

window = pg.display.set_mode((1000, 750))
pg.font.init()
fonte = pg.font.SysFont("Courier New", 50, bold=True)
fonte2 = pg.font.SysFont(None, 55)
subtitulo = pg.font.SysFont(None, 22)

tabuleiro_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

jogo_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]


# variaveis globais

faltantes = None
escondendo_numeros = True
tabuleiro_preenchido = True
click_last_status = False
click_position_x = -1
click_position_y = -1
numero = 0

def Tabuleiro(window):
    pg.draw.rect(window, preto, (50, 50, 600, 600), 6)
    pg.draw.rect(window, preto, (50, 250, 600, 200), 6)
    pg.draw.rect(window, preto, (250, 50, 200, 600), 6)
    pg.draw.rect(window, preto, (50, 117, 600, 67), 2)
    pg.draw.rect(window, preto, (50, 317, 600, 67), 2)
    pg.draw.rect(window, preto, (50, 517, 600, 67), 2)
    pg.draw.rect(window, preto, (117, 50, 67, 600), 2)
    pg.draw.rect(window, preto, (317, 50, 67, 600), 2)
    pg.draw.rect(window, preto, (517, 50, 67, 600), 2)

def Tabuleiro_Hover(window, mouse_position_x, mouse_position_y):
    quadrado = 66.7
    ajuste = 50
    x = (math.ceil((mouse_position_x - ajuste) / quadrado) - 1)
    y = (math.ceil((mouse_position_y - ajuste) / quadrado) - 1)
    pg.draw.rect(window, branco, (0, 0, 1000, 750))
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, azul_claro, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
            if pg.K_1 <= event.key <= pg.K_9:
                # Retorna o número correspondente à tecla pressionada
                numero = event.key - pg.K_1 + 1
            else:
                numero = None

     # Declarando variavel da posição do mouse
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # Declarando variavel do click do mouse
    click = pg.mouse.get_pressed()

    # Jogo em si
    Tabuleiro_Hover(window, mouse_position_x, mouse_position_y)
    Tabuleiro(window)

    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()