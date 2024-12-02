#This file was created by: Josiah Cha

import pygame as pg
from pygame import *
from pygame.locals import *
from pygame.rect import *
from pygame.sprite import Sprite
#Sprite is a super class (Daddy class)
from settings import *
#* = EVERYTHING
import random
from main import Game
import math

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
        Ball.effect
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
        self.hit_counter = 0        
        Ball.effect = 0
    
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
        if self.rect.top < -10:
            self.rect.y = self.y
            self.vy *= 0
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.rect = self.image.get_rect()
            self.image.fill(WHITE)
            self.speed = 10
        if self.rect.bottom > HEIGHT + 10:
            self.rect.y = self.y
            self.vy *= 0
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.rect = self.image.get_rect()
            self.image.fill(WHITE)
            self.speed = 10

    def collide_with_walls(self, dir):
        # if dir == 'x':
        #     hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
        #     if hits:
        #         if self.vx > 0:
        #             self.x = hits[0].rect.left - TILESIZE
        #             self.x = hits[0].rect.left - self.rect.width
        #         if self.vx < 0:
        #             self.x = hits[0].rect.right
        #         self.vx = 0
        #         self.rect.x = self.x
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

    def all_hits(self): #Rename method: all_hits?
        hits = pg.sprite.spritecollide(self, self.game.all_powerups, True)
        if hits: 
            if str(hits[0].__class__.__name__) == "Powerup": 
                    self.hit_counter += 1
                    if self.hit_counter > 1:
                        self.effect = False
                        self.hit_counter = 0
                    self.effect = effect = random.randint(1,6)
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
                            TILESIZE = 32 * 2
                            self.image = pg.transform.scale_by(self.image, (2, 2)) 
                            self.rect = self.image.get_rect()
                            old_center = hits[0].rect.center
                            hits[0].image = pg.transform.scale(hits[0].image, (64, 64))
                            hits[0].rect = hits[0].image.get_rect()
                            hits[0].rect.center = old_center
                            self.rect.center = hits[0].rect.center
                            # self.collide_with_walls(self, dir)
                            # if dir == 'y':
                            #         hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
                            #         if hits:
                            #             if self.vy > 0:
                            #                 self.y = hits[0].rect.top - TILESIZE 
                            #                 # self.y = hits[0].rect.top - self.rect.height
                            #             if self.vy < 0:
                            #                 self.y = hits[0].rect.bottom
                            #                 self.vy *= -1
                            #                 self.rect.y = self.y
                    if effect == 4:
                            print('get smaller...')
                            self.image.fill(BBLUE)
                            TILESIZE = 32 / 2
                            self.image = pg.transform.scale_by(self.image, (1/2, 1/2)) 
                            self.rect = self.image.get_rect()
                            old_center = hits[0].rect.center    
                            hits[0].image = pg.transform.scale(hits[0].image, (16, 16))
                            hits[0].rect = hits[0].image.get_rect()
                            hits[0].rect.center = old_center
                            self.rect.center = hits[0].rect.center
                    if effect == 5:
                            print('get taller...')
                            self.image.fill(BLUE)
                            TILESIZE = 32 * 2
                            self.image = pg.transform.scale_by(self.image, (1, 2)) 
                            self.rect = self.image.get_rect()
                            old_center = hits[0].rect.center
                            hits[0].image = pg.transform.scale(hits[0].image, (32, 64))
                            hits[0].rect = hits[0].image.get_rect()
                            hits[0].rect.center = old_center
                            self.rect.center = hits[0].rect.center
                    if effect == 6:
                            print('relfect...')
                            self.speed *= -1

                                                     
                            
                            
                        
            
        hits = pg.sprite.spritecollide(self, self.game.all_players, False)
        if hits:
            if str(hits[0].__class__.__name__) == "Player":
         # when it hits the player, it will move other side
                # print("off the screen...")
                self.speed *= -1
                self.rect.x += 32
                self.vy *= 1
                if self.vy == 0:
                    self.vy += self.speed
                pg.mixer.Sound.play(self.game.ball_ping_snd)
            if str(hits[0].__class__.__name__) == "Player2":
            # when it hits the player2, it will move other side
                #print("off the screen...")
                self.speed *= -1
                self.rect.x -= 32
                self.vy += self.speed
                self.vy *= -1
                if self.vy == 0:
                    self.vy += self.speed
                pg.mixer.Sound.play(self.game.ball_ping_snd)


    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.vy

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        self.all_hits()

        self.collide_with_walls('x')
        self.collide_with_walls('y')

        self.reset()

        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0

class Button(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_buttons
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((64, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    def update(self):
        pass

class Pusher(Sprite):
    def __init__(self, game, x, y):    
        self.game = game
        self.groups = game.all_sprites, game.all_pushers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.speed = 10
        self.x = x * TILESIZE
        self.vx, self.vy = 0, 0
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x += self.vx
            self.vx -= self.speed
        if keys[pg.K_d]:
            self.rect.x += self.vx
            self.vx += self.speed
    
    def enter(self, group, kill):
        hits = pg.sprite.spritecollide(self, self.game.all_buttons, True)
        if hits: 
            if str(hits[0].__class__.__name__) == "Button":
                # self.game.new()
                print(self.game.level)
                self.game.level += 1
                textLevel = "level" + str(self.game.level) + ".txt"
                self.game.load_data(textLevel)
                self.game.new()
                print(textLevel)

    def update(self): 
        self.get_keys()

        self.x += self.vx * self.game.dt

        self.enter(self.game.all_buttons, True) 



