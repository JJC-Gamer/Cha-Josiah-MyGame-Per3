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
        self.groups = game.all_sprites, game.all_players1, game.all_players
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)
        # self.rect.x = x
        # self.rect.y = y
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 15
        self.points = 0
        self.vx, self.vy = 0, 0
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y -= self.speed
        if keys[pg.K_a]:
            self.x -= self.speed
        if keys[pg.K_s]:
            self.y += self.speed
        if keys[pg.K_d]:
            self.x += self.speed
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_borders, False)
            if hits:
                if self.x > 0:
                    self.x = hits[0].rect.left - TILESIZE
                    # self.x = hits[0].rect.left - self.rect.width
                if self.x < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.y > 0:
                    self.y = hits[0].rect.top - TILESIZE
                    # self.y = hits[0].rect.top - self.rect.height
                if self.y < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
    def get_points(self):
        if self.game.all_balls.sprites()[0].rect.right > WIDTH:
            self.points += 1

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
        
        self.rect.y = self.y
        self.collide_with_walls('y')

        self.get_points()






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
        self.groups = game.all_sprites, game.all_players2, game.all_players
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.rect.x = x 
        self.rect.y = y
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 15
        self.points = 0
        self.vx, self.vy = 0, 0
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_i]:
            self.y -= self.speed
        if keys[pg.K_j]:
            self.x -= self.speed
        if keys[pg.K_k]:
            self.y += self.speed
        if keys[pg.K_l]:
            self.x += self.speed
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_borders, False)
            if hits:
                if self.x > 0:
                    self.x = hits[0].rect.left - TILESIZE
                    # self.x = hits[0].rect.left - self.rect.width
                if self.x < 0:
                    self.x = hits[0].rect.right
                self.vx = 0  
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.y > 0:
                    self.y = hits[0].rect.top - TILESIZE
                    # self.y = hits[0].rect.top - self.rect.height
                if self.y < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
    def get_points(self):
        if  self.game.all_balls.sprites()[0].rect.left < 0:
            self.points += 1
    def get_keys2(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_k]:
            self.y -= self.speed
        if keys[pg.K_l]:
            self.x -= self.speed
        if keys[pg.K_i]:
            self.y += self.speed
        if keys[pg.K_j]:
            self.x += self.speed
    def update(self):
        self.get_keys()


        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        # reverse order to fix collision issues
        
        self.rect.x = self.x
        self.collide_with_walls('x')
        
        self.rect.y = self.y
        self.collide_with_walls('y')

        self.get_points()
        




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

class Border(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_borders
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
        self.width = self.rect.width
    def update(self):
        # self.rect.width = self.width
        # self.rect = self.image.get_rect()
        pass

class Ball(Sprite): 
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_balls
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
    
    def reset(self):
        if self.rect.right > WIDTH + 10:
            self.rect.x = self.x
            self.vy *= 0
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.rect = self.image.get_rect()
            self.image.fill(WHITE)
            self.speed = 10
        if self.rect.left < -10:
            self.rect.x = self.x
            self.speed *= -1
            self.vy *= 0
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.rect = self.image.get_rect()
            self.image.fill(WHITE)
            self.speed = 10

    def collide_with_walls(self, dir):
        #if dir == 'x':
            #hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            #if hits:
                #if self.vx > 0:
                    #self.x = hits[0].rect.left - TILESIZE
                    # self.x = hits[0].rect.left - self.rect.width
                #if self.vx < 0:
                    #self.x = hits[0].rect.right
                #self.vx = 0
                #self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - TILESIZE 
                    # self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy *= -1
                self.rect.y = self.y

    def hits(self): #Rename method: all_hits?
        hits = pg.sprite.spritecollide(self, self.game.all_powerups, True)
        if hits: 
            if str(hits[0].__class__.__name__) == "Powerup": 
                    effect = random.randint(1,3)
                    if effect == 1:
                        print('get faster...')
                        self.image.fill(PURPLE)
                        self.speed *= 1.5
                        if self.rect.right > WIDTH + 10:
                            self.rect.x = self.x
                            self.vy *= 0
                        if self.rect.left < -10:
                            self.rect.x = self.x
                            self.speed *= -1
                            self.vy *= 0
                    if effect == 2:
                        print('get slower...')
                        self.image.fill(ORANGE)
                        self.speed /= 1.5
                        if self.rect.right > WIDTH + 10:
                            self.rect.x = self.x
                            self.vy *= 0
                        if self.rect.left < -10:
                            self.rect.x = self.x
                            self.speed *= -1
                            self.vy *= 0
                    if effect == 3: 
                            print('get bigger...')
                            self.image.fill(PINK)
                            TILESIZE2 = TILESIZE * 2
                            self.image = pg.transform.scale(self.image, (TILESIZE2, TILESIZE2)) 
                            old_center = hits[0].rect.center
                            hits[0].image = pg.transform.scale(hits[0].image, (64, 64))
                            hits[0].rect = hits[0].image.get_rect()
                            hits[0].rect.center = old_center
        hits = pg.sprite.spritecollide(self, self.game.all_players, False)
        if hits:
            if str(hits[0].__class__.__name__) == "Player":
         # when it hits the player, it will move other side
                # print("off the screen...")
                self.speed *= -1
                self.rect.x += 32
                self.vy *= -1
            if str(hits[0].__class__.__name__) == "Player2":
            # when it hits the player2, it will move other side
                #print("off the screen...")
                self.speed *= -1
                self.rect.x -= 32
                self.vy += self.speed
                self.vy *= -1


    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.vy

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        self.hits()

        self.collide_with_walls('x')
        self.collide_with_walls('y')

        self.reset()

        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0




