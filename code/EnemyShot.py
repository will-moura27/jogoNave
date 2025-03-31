from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):
        def __init__(self, name: str, position: tuple):
            super().__init__(name, position)

        def move(self):
            # Atualiza a posição do tiro do inimigo para se mover para a esquerda (por exemplo)
            self.rect.centerx -= ENTITY_SPEED[self.name]