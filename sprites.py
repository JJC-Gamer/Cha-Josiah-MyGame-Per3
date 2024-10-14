#This file was created by: Josiah Cha

import pygame as pg
from pygame.sprite import Sprite
#Sprite is a super class (Daddy class)
from settings import *
#* = EVERYTHING
import random

class Player(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_players1
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)
        # self.rect.x = x
        # self.rect.y = y
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.points = 0
        self.vx, self.vy = 0, 0
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vy -= self.speed
        if keys[pg.K_a]:
            self.vx -= self.speed
        if keys[pg.K_s]:
            self.vy += self.speed
        if keys[pg.K_d]:
            self.vx += self.speed
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - TILESIZE
                    # self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - TILESIZE
                    # self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
    def collide_with_stuff(self, group, kill): 
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Powerup":
                print("i hit a powerup...")
                self.speed += 5

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
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        # reverse order to fix collision issues
        
        self.rect.x = self.x
        self.collide_with_walls('x')

        self.collide_with_stuff(self.game.all_powerups, True)
        
        self.rect.y = self.y
        self.collide_with_walls('y')


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

        


class Player2(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_players2
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        # self.rect.x = x
        # self.rect.y = y
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.points = 0
        self.vx, self.vy = 0, 0
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_i]:
            self.vy -= self.speed
        if keys[pg.K_j]:
            self.vx -= self.speed
        if keys[pg.K_k]:
            self.vy += self.speed
        if keys[pg.K_l]:
            self.vx += self.speed
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - TILESIZE
                    # self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - TILESIZE
                    # self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
    def collide_with_stuff(self, group, kill): 
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Powerup":
                print("i hit a powerup...")
                self.speed += 5

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        # reverse order to fix collision issues
        
        self.rect.x = self.x
        self.collide_with_walls('x')

        self.collide_with_stuff(self.game.all_powerups, True)
        
        self.rect.y = self.y
        self.collide_with_walls('y')



#This is Wall
class Wall(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_walls
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    def update(self):
        pass

class Powerup(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_powerups
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Ball(Sprite): 
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE 
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0
    def collide_with_player(self, group): 
        hits = pg.sprite.spritecollide(self, group)
        if hits:
            if str(hits[0].__class__.__name__) == "Player":
                self.vx += self.speed
    def update(self):
        self.rect.x += self.speed
        hits = pg.sprite.spritecollide(self, self.game.all_players1, False)
        # when it hits the side of the screen, it will move down
        if hits:
            # print("off the screen...")
            self.speed *= -1
            self.rect.x += 32
        hits = pg.sprite.spritecollide(self, self.game.all_players2, False)
        # when it hits the side of the screen, it will move down
        if hits:
            # print("off the screen...")
            self.speed *= -1
            self.rect.x -= 32

