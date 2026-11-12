import sys
import random
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_WHITE, COLOR_YELLOW, COLOR_CYAN, COLOR_BLACK, MENU_OPTIONS, WIN_WIDTH, WIN_HEIGHT


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.selected_option = 0

        # Cria uma lista de estrelas para o fundo animado (posição x, y e velocidade)
        self.stars = []
        for _ in range(60):  # 60 estrelas na tela
            self.stars.append({
                'x': random.randint(0, WIN_WIDTH),
                'y': random.randint(0, WIN_HEIGHT),
                'speed': random.uniform(0.5, 2.0),  # Velocidades diferentes dão efeito de profundidade
                'size': random.choice([1, 2, 3])  # Tamanhos variados para parecerem mais distantes ou próximas
            })

    def run(self):
        try:
            pygame.mixer_music.load('./jogo/assets/menu.mp3')
            pygame.mixer_music.play(-1)
            pygame.mixer_music.set_volume(0.2)
        except:
            pass

        clock = pygame.time.Clock()
        frame_count = 0

        while True:
            clock.tick(60)
            frame_count += 1

            # Limpa a tela com preto
            self.surf.fill(COLOR_BLACK)

            # Atualiza e desenha as estrelas no fundo
            for star in self.stars:
                star['x'] -= star['speed']  # Move a estrela para a esquerda
                # Se sair da tela pela esquerda, reposiciona na direita com nova altura
                if star['x'] < 0:
                    star['x'] = WIN_WIDTH
                    star['y'] = random.randint(0, WIN_HEIGHT)

                # Desenha a estrela (pontinho branco)
                pygame.draw.circle(self.surf, COLOR_WHITE, (int(star['x']), int(star['y'])), star['size'])

            # Joga o fundo animado na janela principal
            self.window.blit(self.surf, (0, 0))

            # Efeito de piscar no título
            title_color = COLOR_YELLOW if (frame_count // 30) % 2 == 0 else COLOR_CYAN

            # Desenha o Título do Jogo
            self.draw_text(32, "SPACE SHOOTER", title_color, (WIN_WIDTH / 2, WIN_HEIGHT / 4 - 20))
            self.draw_text(12, "- ARCADE EDITION -", COLOR_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 4 + 10))

            # Desenha as opções do Menu com setas indicadoras
            for i, option_text in enumerate(MENU_OPTIONS):
                if i == self.selected_option:
                    color = COLOR_YELLOW
                    display_text = f'> {option_text} <'
                else:
                    color = COLOR_WHITE
                    display_text = option_text

                self.draw_text(16, display_text, color, (WIN_WIDTH / 2, (WIN_HEIGHT / 2) + (i * 35)))

            pygame.display.flip()

            # Captura de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(MENU_OPTIONS)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(MENU_OPTIONS)
                    elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                        return MENU_OPTIONS[self.selected_option]

    def draw_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida sans typewriter", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)