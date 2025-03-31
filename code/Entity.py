#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SPEED, ENTITY_SCORE


class Entity(ABC):
    def __init__(self,name, position : tuple):
        self.name = name
        self.surf = pygame.image.load('jogo/assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.damage= ENTITY_DAMAGE[self.name]
        self.last_dmg = 'None'
        self.is_exploding = False
        self.explosion_index = 0
        self.score = ENTITY_SCORE[self.name]


    @abstractmethod
    def move(self, ):
        pass