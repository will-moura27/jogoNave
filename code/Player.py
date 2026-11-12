import pygame
from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, \
    PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.score = 0
        self.lives = 3              # Inicia com 3 vidas
        self.invincible_timer = 0   # Tempo de imunidade ao renascer
        self.shot_delay = 0         # Controle de cadência do tiro

    def move(self):
        # Decrementa o tempo de invencibilidade a cada frame se estiver ativo
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

        # Decrementa o cooldown do tiro se estiver maior que zero
        if self.shot_delay > 0:
            self.shot_delay -= 1

        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        # O tiro só é disparado se o cooldown (delay) estiver totalmente zerado
        if self.shot_delay == 0:
            self.shot_delay = 18  # Define o intervalo entre os tiros (ajuste se quiser mais rápido/lento)
            return PlayerShot(name=f'{self.name}shot', position=(self.rect.centerx, self.rect.centery))
        return None