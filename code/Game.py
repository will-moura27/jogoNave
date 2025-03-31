#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from idlelib import window

import pygame as pygame
from pygame import Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self,):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        while True:
            score = Score(self.window)
            menu = Menu(self.window)

            menu_return=menu.run()

            if menu_return in [MENU_OPTIONS[0],MENU_OPTIONS[1],MENU_OPTIONS[2]]:
                player_score =[0,0]
                level = Level(self.window,'level1',menu_return,player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window,'level2',menu_return,player_score)
                    level_return = level.run(player_score)

            else:
                pygame.quit()
                sys.exit()