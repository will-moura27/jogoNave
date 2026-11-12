import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, MENU_OPTIONS, EVENT_ENEMY, EVENT_TIMEOUT, COLOR_VIOLET, COLOR_YELLOW, WIN_HEIGHT, \
    COLOR_CYAN, COLOR_GREEN, PLAYER_KEY_SHOOT
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, menu_option: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[Entity] = []
        # Usa a instância de EntityFactory para obter a entidade
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'bg'))
        player = EntityFactory.get_entity('player1')
        player.score = player_score[0]  # score do player 1
        self.entity_list.append(player)
        if menu_option in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            player = EntityFactory.get_entity('player2')
            player.score = player_score[1]  # score player 2
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, 4000)
        self.timeout = 60000
        pygame.time.set_timer(EVENT_TIMEOUT, 100)  # 100ms

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'jogo/assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.2)
        clock = pygame.time.Clock()

        while True:
            clock.tick(80)

            # Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1', 'enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:  # acontece a cada 100ms
                    self.timeout -= 100
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'player2':
                                player_score[1] = ent.score
                        return True

            # Gerenciamento de vidas do Player (se a saúde zerar mas ainda tiver vidas)
            found_player = False
            for ent in self.entity_list[:]:
                if isinstance(ent, Player):
                    found_player = True
                    if ent.health <= 0 and not ent.is_exploding:
                        if ent.lives > 0:
                            ent.lives -= 1              # Perde 1 vida
                            ent.health = 100            # Restaura a saúde
                            ent.invincible_timer = 120  # 1.5 a 2 segundos de imunidade
                            ent.rect.center = (100, WIN_HEIGHT / 2)  # Reseta posição
                        else:
                            return False  # Acabaram as vidas -> Game Over

            if not found_player:
                return False

            # Limpar entidades com saúde zero ou gerenciar animações de explosão
            EntityMediator.verify_health(self.entity_list)

            # Verificar colisões
            EntityMediator.verify_collision(self.entity_list)

            # Desenhar todas as entidades na tela
            for ent in self.entity_list:
                if ent is not None:
                    # Tratar a animação de explosão vs movimento normal
                    if ent.is_exploding:
                        num_frame = ent.explosion_index // 4
                        if num_frame < len(ent.explosion_surf_list):
                            center = ent.rect.center
                            ent.surf = ent.explosion_surf_list[num_frame]
                            ent.rect = ent.surf.get_rect(center=center)
                        ent.explosion_index += 1
                    else:
                        # Se for inimigo, persegue o player; senão, movimento normal
                        if isinstance(ent, Enemy):
                            player_pos = None
                            for e in self.entity_list:
                                if isinstance(e, Player):
                                    player_pos = e.rect.center
                                    break
                            ent.move(player_pos)
                        else:
                            ent.move()

                        # Disparo seguro para Inimigos e Players (respeitando o delay)
                        if isinstance(ent, Enemy):
                            shoot = ent.shoot()
                            if shoot is not None:
                                self.entity_list.append(shoot)
                        elif isinstance(ent, Player):
                            pressed_key = pygame.key.get_pressed()
                            if pressed_key[PLAYER_KEY_SHOOT[ent.name]]:
                                shoot = ent.shoot()
                                if shoot is not None:
                                    self.entity_list.append(shoot)

                    # Desenha a entidade na tela (com efeito de piscar se estiver invencível)
                    if isinstance(ent, Player) and ent.invincible_timer > 0:
                        if (ent.invincible_timer // 10) % 2 == 0:  # Pisca a cada 10 frames
                            self.window.blit(source=ent.surf, dest=ent.rect)
                    else:
                        self.window.blit(source=ent.surf, dest=ent.rect)

                    # Placar e informações na tela
                    if ent.name == 'player1':
                        self.level_text(14, f'P1 HP: {ent.health} | Lives: {ent.lives} | Score: {ent.score}', COLOR_CYAN, (180, 10))
                    if ent.name == 'player2':
                        self.level_text(14, f'P2 HP: {ent.health} | Lives: {ent.lives} | Score: {ent.score}', COLOR_VIOLET, (180, 30))

            # Texto a ser exibido na tela (Timeout)
            self.level_text(14, f'{self.name} - timeout: {self.timeout / 1000}s', COLOR_WHITE, (100, 300))

            # Atualizar tela
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida sans typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)