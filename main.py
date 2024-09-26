#This file is created by: Josiah Cha

import pygame as pg
#WEIGHT AND HEIGHT from external source
from settings import*
from sprites import*
from random import randint

#Defined class
class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        #Size of the screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Cha's Game")
        #This is a clock
        self.clock = pg.time.Clock()
        #Start the Game
        self.running = True
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self,50,50)
        self.mob = Mob(self,500,500)
        self.wall = Wall(self,250,250)
        # instantiaed a mob
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.mob)
        self.all_sprites.add(self.wall)
        for i in range(6):
            Mob(self, i*randint(0,WIDTH), i *randint(0,HEIGHT)) 
        for i in range(32): 
            #print(i*TILESIZE)
            w = Wall(self,i*TILESIZE,150)
            self.all_sprites.add(w)

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        
        #input
    def input(self):
        for event in pg.event.get():
                #The X button to quit the game
                if event.type == pg.QUIT:
                    self.running = False
        #process
    def update(self):
        self.all_sprites.update()
    pg.quit()
        #output
    def draw(self):
        #WHITE and BLACK in Settings.py
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

        
if __name__ =="__main__":
    g = Game()
    g.new()
    g.run()