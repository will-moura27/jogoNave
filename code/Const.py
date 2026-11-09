import pygame

COLOR_ORANGE=(255, 128, 0)
COLOR_WHITE=(255, 255, 255)
COLOR_YELLOW=(255,255,128)
COLOR_VIOLET=(139,0,139)
COLOR_GREEN=(0,255,0)
COLOR_CYAN=(0,255,255)
COLOR_BLACK=(0,0,0)
#M

MENU_OPTIONS= ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')
#W
WIN_WIDTH=576
WIN_HEIGHT=324

#E

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT= pygame.USEREVENT +2

ENTITY_SHOT_DELAY= {'player1' :20,
                    'player2' :15,
                    'enemy1' :100,
                    'enemy2' :100,

                    } #intervalo de criaçao de tiro quando a tecla de tiro for pressionada


ENTITY_SPEED = {'level1bg0':0,
                'level1bg1':1,
                'level1bg2':2,
                'level1bg3':3,
                'level1bg4':4,
                'level1bg5':5,
                'level1bg6':6,
                'level2bg0':0,
                'level2bg1':1,
                'level2bg2':2,
                'level2bg3':3,
                'level2bg4':4,
                'player1' :4,
                'player2' :4,
                'enemy1' : 2 ,
                'enemy2' : 2,
                'player1shot' :4,
                'player2shot' :4,
                'enemy1shot' : 4,
                'enemy2shot' : 4,}

ENTITY_HEALTH = {'level1bg0':999,
                'level1bg1':999,
                'level1bg2':999,
                'level1bg3':999,
                'level1bg4':999,
                'level1bg5':999,
                'level1bg6':999,
                'level2bg0':999,
                'level2bg1':999,
                'level2bg2':999,
                'level2bg3':999,
                'level2bg4':999,
                'player1' :150,
                'player2' :3100,
                'enemy1' : 150,
                'enemy2' : 150,
                 'player1shot' : 1 ,
                 'player2shot': 1,
                 'enemy1shot': 1,
                 'enemy2shot': 1,
                 }
ENTITY_DAMAGE = {'level1bg0':0,
                'level1bg1':0,
                'level1bg2':0,
                'level1bg3':0,
                'level1bg4':0,
                'level1bg5':0,
                'level1bg6':0,
                'level2bg0':0,
                'level2bg1':0,
                'level2bg2':0,
                'level2bg3':0,
                'level2bg4':0,
                'player1' :100,
                'player2' :100,
                'enemy1' : 100,
                'enemy2' : 100,
                 'player1shot' : 100 ,
                 'player2shot': 25,
                 'enemy1shot': 25,
                 'enemy2shot': 15,
                 }
ENTITY_SCORE = {'level1bg0':0,
                'level1bg1':0,
                'level1bg2':0,
                'level1bg3':0,
                'level1bg4':0,
                'level1bg5':0,
                'level1bg6':0,
                'level2bg0':0,
                'level2bg1':0,
                'level2bg2':0,
                'level2bg3':0,
                'level2bg4':0,
                'player1' :0,
                'player2' :0,
                'enemy1' : 100,
                'enemy2' : 150,
                 'player1shot' : 0 ,
                 'player2shot': 0,
                 'enemy1shot': 0,
                 'enemy2shot': 0,
                 }





PLAYER_KEY_UP = {'player1' : pygame.K_UP,
                 'player2' : pygame.K_w}
PLAYER_KEY_DOWN = {'player1' : pygame.K_DOWN,
                 'player2' : pygame.K_s}
PLAYER_KEY_LEFT = {'player1' : pygame.K_LEFT,
                 'player2' : pygame.K_a}
PLAYER_KEY_RIGHT = {'player1' : pygame.K_RIGHT,
                 'player2' : pygame.K_d}
PLAYER_KEY_SHOOT = {'player1' : pygame.K_SPACE,
                 'player2' : pygame.K_KP_ENTER}