import sys

import pygame
from pygame import Surface
from pygame.font import Font

from code.Const import COLOR_ORANGE, WIN_WIDTH, MENU_OPTIONS, COLOR_YELLOW, COLOR_WHITE, COLOR_VIOLET


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('jogo/assets/menubg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./jogo/assets/menu.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.2)
        menu_option= 0
        while True:
            #DESENHAR NA TELA
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "THE", COLOR_VIOLET, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "VOID", COLOR_VIOLET, ((WIN_WIDTH / 2), 120))

            for i  in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(20,MENU_OPTIONS[i],COLOR_VIOLET,((WIN_WIDTH / 2), 200+30*i))

                else:
                    self.menu_text(20, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))
            pygame.display.flip()
            #VERIFICAR EVENTOS
            for event in pygame.event.get(): #esse for serve pra fechar o jogo corretamente
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN: #essa condiçào serve pra rolarmos o menu pra baixo e voltar pra
                    # primeira opçào
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) -1:
                            menu_option +=1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:#essa é pra fazer o contrario
                        if menu_option >0 :
                            menu_option -=1
                        else:
                            menu_option = len(MENU_OPTIONS) -1

                    if event.key == pygame.K_RETURN: #se a tecla enter for pressionada, retorne a opção desejada
                        return MENU_OPTIONS[menu_option]#VAI RETORNAR COM BASE NO TEXTO COM BASE NA OPCAO QUE FOI DESEJADA


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida sans typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)