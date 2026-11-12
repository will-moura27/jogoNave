from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, player_pos: tuple = None):
        # Move para a esquerda normalmente
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Se recebeu a posição do player, persegue a altura (Y) dele de forma suave
        if player_pos:
            player_y = player_pos[1]
            # Se o player estiver abaixo do inimigo, o inimigo desce
            if self.rect.centery < player_y:
                self.rect.centery += 1  # Velocidade de perseguição vertical (ajuste se quiser mais rápido)
            # Se o player estiver acima, o inimigo sobe
            elif self.rect.centery > player_y:
                self.rect.centery -= 1

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}shot', position=(self.rect.centerx, self.rect.centery))