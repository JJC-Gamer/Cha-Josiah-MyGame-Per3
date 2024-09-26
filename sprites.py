#This file was created by: Josiah Cha

import pygame as pg
from pygame.sprite import Sprite
#Sprite is a super class (Daddy class)
from settings import *
#* = EVERYTHING

class Player(Sprite):
    def __init__(self,game,x,y):
        self.group = game.all_sprites
        Sprite.__init__(self, self.group)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed
        if keys[pg.K_d]:
            self.rect.x += self.speed
    def rev_get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y += self.speed
        if keys[pg.K_a]:
            self.rect.x += self.speed
        if keys[pg.K_s]:
            self.rect.y -= self.speed
        if keys[pg.K_d]:
            self.rect.x -= self.speed
    def update(self):
        self.get_keys()
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speed *= 1
            self.rev_get_keys()
        if self.rect.left > WIDTH or self.rect.right < 0:
            self.speed *= 1
            self.rev_get_keys()
            self.rev_get_keys()
        if self.rect.y == 0:
            self.speed *= 1
            self.rev_get_keys()
        if self.rect.y == HEIGHT:
            self.speed *= 1
            self.rev_get_keys()
        if self.rect.colliderect(self.game.wall):
            self.speed *= 1
            self.rev_get_keys()


class Mob(Sprite):
    def __init__(self,game,x,y):
        self.group = game.all_sprites
        Sprite.__init__(self,self.group)
        self.image = pg.Surface((32, 32))
        self.game = game
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
    def update(self):
        # moving towards the side of the screen
        self.rect.x += self.speed
        # when it hits the side of the screen, it will move down
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speed *= -1
            self.rect.y += 32
        elif self.rect.colliderect(self.game.player):
            self.speed *= -1
            self.rect.y -= 32
        if self.rect.colliderect(self.game.wall):
            self.speed *= -1


#This is Wall
class Wall(Sprite):
    def __init__(self,game,x,y):
        self.group = game.all_sprites
        Sprite.__init__(self,self.group)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
    def update(self):
        pass
