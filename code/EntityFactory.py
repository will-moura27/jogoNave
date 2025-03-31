import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity( entity_name: str,  position= (0, 0)):
        match entity_name:
            case 'level1bg':
                list_bg=[]
                for i in range (7):#o 7 representa o numero de sprites que compoem o background
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'level2bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level2bg{i}', (0, 0)))
                    list_bg.append(Background(f'level2bg{i}', (WIN_WIDTH, 0)))
                return list_bg


            case 'player1':
                return Player('player1',(10, WIN_HEIGHT/2 - 30))
            case 'player2':
                return Player('player2', (10, WIN_HEIGHT / 2 + 30))

            case 'enemy1':
                return Enemy('enemy1', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))
            case 'enemy2':
                return Enemy('enemy2', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))