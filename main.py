#This file is created by: Josiah Cha

import pygame as pg
#WEIGHT AND HEIGHT from external source
from settings import*
from sprites import*
from random import randint

#Defined class
class Game:
    def __init__(self):
    #Initializes the game and displays the window
        pg.init()
        pg.mixer.init() #Sound
        #Size of the screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Cha's Game")
        #This is a clock, sets the FPS
        self.clock = pg.time.Clock()
        #Start the Game
        self.running = True
    def new(self):
    #Initializes all the sprites and places them in the display, cretes all.sprites group so that it can batch update and render
    #Defines proprties that can be seen in the game system
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self,1,1)
        self.mob = Mob(self,500,500)
        self.wall = Wall(self,250,250)
        # instantiaed a mob
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.mob)
        for i in range(10):
            Mob(self, i*randint(0,WIDTH), i *randint(0,HEIGHT)) 
        for i in range(32): 
        #creates a horizontal wall with one wall per tilesize
            #print(i*TILESIZE)
            self.w = Wall(self,i*TILESIZE,150)
            self.all_sprites.add(self.w)

    def run(self):
    #Starts the game, is the main game loop, and runs the game as a boolean (True or False, game is continuing or not)
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    def events(self):
        #Closes the game with the X button
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
        self.all_sprites.update() #Run the update function on all the sprites
    pg.quit()
        #output
    def draw(self):
        #Fills the screen with color
        #WHITE and BLACK in Settings.py
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

 #If is a formaility and checks the file name (If the name of the file is main.py)       
if __name__ =="__main__": #Runs the game
    g = Game() #Creates all game elements with the new method (Not a function)
    g.new()
    g.run()