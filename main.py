#This file is created by: Josiah Cha

import pygame as pg
from settings import *
from sprites import *
from tilemap import *
from os import path
from random import randint
'''
Elevator pitch: I want to create a pong game that has diffrent power ups to give the player a new expierience each time they play.

GOALS: Get the ball to the other side of the screen
RULES: move up and down, can't cross the border between Player 1 and Player 2
FEEDBACK: Hits the ball to other side
FREEDOM: x and y movement with WASD and/or IJKL

What sentence does your game make?
Hit the ball with player bounce ball to other side
Hit side of wall bounces ball to other side
Hits power up, gives effect to either the ball, the player, or the walls

Alpha goal:To create a border to seperate Player 1 and Player 2

'''
'''
Sources:
Chirs Cozart - Collisions for effects
Ethan Chan - Title Screen
'''

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
        self.level = 1
        self.load_data('level1.txt')

    # def load_data_intro(self):
    #     self.game_folder = path.dirname(__file__)
    #     self.map = Map(path.join(self.game_folder, 'level0.txt'))
    def load_data(self, level):
        self.game_folder = path.dirname(__file__)
        self.map = Map(path.join(self.game_folder, level))
        self.img_folder = path.join(self.game_folder, 'images')
        self.snd_folder = path.join(self.game_folder, 'sound')
        self.ball_ping_snd = pg.mixer.Sound(path.join(self.game_folder, 'ball_ping.wav'))
        self.game_music = pg.mixer.Sound(path.join(self.game_folder, 'game_music.wav'))
        self.game_music2 = pg.mixer.Sound(path.join(self.game_folder, 'game_music2.wav'))
        if self.level == 2:
            pg.mixer.Sound.play(self.game_music)
            pg.mixer.Sound.stop(self.game_music2)
        else:
            pg.mixer.Sound.play(self.game_music2)

            
        print ('load data')
         
    def new(self):
        print(self.map.data)
        self.all_buttons = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_pushers = pg.sprite.Group()
        self.all_balls = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_powerups = pg.sprite.Group()
        self.all_players = pg.sprite.Group()
        self.all_players1 = pg.sprite.Group()
        self.all_players2 = pg.sprite.Group()
        self.all_borders = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            print (row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == 'Q':
                    self.pushers = Pusher(self, col, row)
                if tile == 'T':
                    self.buttons = Button(self, col, row)
                if tile == 'W':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'M':
                    self.player2 = Player2(self, col, row)
                if tile == 'U':
                    Powerup(self, col, row)
                    # random.randint(0, 2) and Powerup(self, col, row)
                if tile == 'X':
                    Border(self, col, row)
                if tile == 'B':
                    Ball(self, col, row)

    
            
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

    def run(self):
    #Starts the game, is the main game loop, and runs the game as a boolean (True or False, game is continuing or not)
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.input()
            self.draw_intro()
    def draw_text(self, surface, text, size, color, x, y):
        
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surface.blit(text_surface, text_rect)
    def draw_intro(self):
        if self.level == 1:
            self.screen.fill(BLACK)
            self.draw_text(self.screen, 'Welcome to Pong:', 24, GREEN, WIDTH/2, HEIGHT/24)
            self.draw_text(self.screen, 'WITH POWER UPS!!!!!!!', 24, RED, WIDTH/2, HEIGHT/10)
            self.all_sprites.draw(self.screen)
            pg.display.flip()
        if self.level == 2:
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            self.draw_text(self.screen, str(self.dt*1000), 24, WHITE, WIDTH/30, HEIGHT/30)
            self.draw_text(self.screen, "Player 1 points: " + str(self.player.points), 24, WHITE, WIDTH/4, HEIGHT/24)
            self.draw_text(self.screen, "Player 2 points: " + str(self.player2.points), 24, WHITE, WIDTH/1.33, HEIGHT/24)
            pg.display.flip()


 #If is a formaility and checks the file name (If the name of the file is main.py)       
if __name__ == "__main__": #Runs the game
    g = Game() #Creates all game elements with the new method (Not a function)
    g.new()
    g.run()
    
