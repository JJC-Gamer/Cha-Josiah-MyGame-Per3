#This file is created by: Josiah Cha

import pygame as pg
#WEIGHT AND HEIGHT from external source
from settings import*
from sprites import*
from random import randint
from tilemap import*
from os import path

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

    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.map = Map(path.join(self.game_folder, 'level1.txt'))
        
    def new(self):
        self.load_data()
        print(self.map.data)
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_powerups = pg.sprite.Group()
        # self.player = Player(self, 1, 1)
        # instantiated a mob
        # self.mob = Mob(self, 100,100)
        # makes new mobs and walls using a for loop
        # for i in range(randint(10,20)):
        #     m = Mob(self, i*randint(0, 200), i*randint(0, 200))
        #     Wall(self, i*TILESIZE, i*TILESIZE)
        
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
        self.all_sprites.update() 
        #Run the update function on all the sprites
        pass
    pg.quit()
        #output

    def draw_text(self, text, font_name, size, color, x, y,):
        fonet_name = pg.font.match_font('ariel')
        font = pg.font.Font(fonet_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        #Fills the screen with color
        #WHITE and BLACK in Settings.py
        self.screen.fill(BLACK)
        self.draw_text(self.screen, self.dt, 24, WHITE, WIDTH/2, 10)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

 #If is a formaility and checks the file name (If the name of the file is main.py)       
if __name__ == "__main__": #Runs the game
    g = Game() #Creates all game elements with the new method (Not a function)
    g.new()
    g.run()