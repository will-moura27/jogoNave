from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        if ent1.is_exploding or ent2.is_exploding:
            return

        # Se alguma das entidades for um Player com invencibilidade ativa, ignora a colisão/dano
        if isinstance(ent1, Player) and ent1.invincible_timer > 0:
            return
        if isinstance(ent2, Player) and ent2.invincible_timer > 0:
            return

        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom):

                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        elif isinstance(ent, PlayerShot):
            # Se o tiro do player ultrapassar a largura da tela, marca para sumir direto
            if ent.rect.left > WIN_WIDTH:
                ent.health = 0
        elif isinstance(ent, EnemyShot):
            # Se o tiro do inimigo passar da borda esquerda, marca para sumir direto
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                # Se for um tiro (PlayerShot ou EnemyShot), remove direto da lista SEM explosão
                if isinstance(ent, (PlayerShot, EnemyShot)):
                    entity_list.remove(ent)
                    continue

                # Se for o Player e ainda tiver vidas, a lógica de vida/reviver é tratada no Level.py
                if isinstance(ent, Player) and ent.lives > 0:
                    continue

                # Inicia a animação de explosão apenas para naves (Player e Enemy)
                if not ent.is_exploding:
                    ent.is_exploding = True
                elif ent.explosion_index > len(ent.explosion_surf_list) * 4:
                    entity_list.remove(ent)