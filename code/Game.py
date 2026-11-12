#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame as pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.GameOver import GameOver


class Game:
    def __init__(self, ):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                play_again = True

                # Loop para permitir o "Tentar Novamente"
                while play_again:
                    player_score = [0, 0]
                    level = Level(self.window, 'level1', menu_return, player_score)
                    level_return = level.run(player_score)

                    if level_return:
                        level = Level(self.window, 'level2', menu_return, player_score)
                        level_return = level.run(player_score)

                    # Se o jogador morreu (level_return é False)
                    if not level_return:
                        game_over = GameOver(self.window)
                        go_return = game_over.run()

                        if go_return == 'TRY AGAIN':
                            play_again = True  # Repete o loop do level
                        else:
                            play_again = False  # Sai para o menu principal
            else:
                pygame.quit()
                sys.exit()