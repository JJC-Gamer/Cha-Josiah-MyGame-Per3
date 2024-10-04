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
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vy -= self.speed
            self.rect.y -= self.speed
        if keys[pg.K_a]:
            self.vx -= self.speed
            self.rect.x -= self.speed
        if keys[pg.K_s]:
            self.vy += self.speed
            self.rect.y += self.speed
        if keys[pg.K_d]:
            self.vx += self.speed
            self.rect.x += self.speed
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.rect.right = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.rect.left = hits[0].rect.right
                self.vx = 0
                self.rect.x += self.vx
                if self.vy > 0:
                    self.rect.top = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.rect.bottom = hits[0].rect.bottom
                self.vy = 0
                self.rect.y += self.vy
    '''
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
    '''

    def update(self):
        self.get_keys()
        '''
                self.vx += self.vx * self.game.dt
        self.vy += self.vy * self.game.dt
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speed *= 1
            self.rev_get_keys()
        if self.rect.left > WIDTH or self.rect.right < 0:
            self.speed *= 1
            self.rev_get_keys()
        if self.rect.y < 0:
            self.speed *= 1
            self.rev_get_keys()
        if self.rect.y > HEIGHT:
            self.speed *= 1
            self.rev_get_keys()
        if self.rect.colliderect(self.game.wall):
            self.speed *= 1
            self.rev_get_keys()
        '''

        


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
        if self.rect.y > HEIGHT:
            if self.rect.right > WIDTH or self.rect.left < 0:
                self.speed *= -1
                self.rect.y -= 32
        if self.rect.y < 0:
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
        self.group = game.all_sprites, game.walls
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

class Powerup(Sprite):
    def __init__(self,game,x,y):
        self.group = game.all_sprites
        Sprite.__init__(self,self.group)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.rect.x = x
        self.rect.y = y
        self.speed = 10