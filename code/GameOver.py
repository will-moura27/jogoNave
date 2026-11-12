import sys
import pygame
from pygame.locals import K_RETURN, K_ESCAPE, K_DOWN, K_UP, K_KP_ENTER
from code.Const import COLOR_WHITE, COLOR_RED, COLOR_BLACK, WIN_WIDTH, WIN_HEIGHT


class GameOver:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.surf.fill(COLOR_BLACK)
        self.options = ['TRY AGAIN', 'MAIN MENU']
        self.selected_option = 0

    def run(self):
        pygame.mixer_music.stop()  # Para a música do level se quiser
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.blit(self.surf, (0, 0))

            # Desenha o título Game Over
            self.draw_text(48, "GAME OVER", COLOR_RED, (WIN_WIDTH / 2, WIN_HEIGHT / 3 - 20))

            # Desenha as opções do menu de Game Over
            for i, option in enumerate(self.options):
                color = COLOR_RED if i == self.selected_option else COLOR_WHITE
                self.draw_text(20, option, color, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + (i * 30)))

            pygame.display.flip()

            # Captura de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [K_UP, K_DOWN]:
                        self.selected_option = 1 - self.selected_option  # Alterna entre 0 e 1
                    elif event.key in [K_RETURN, K_KP_ENTER]:
                        return self.options[self.selected_option]

    def draw_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="lucida sans typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)