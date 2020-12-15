import pygame

def Menu():
    def __init__(self, game):
        self.game = game
        #gives access to earlier things
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        #tells menu to keep running
        self.cursor_rect = pygame.Rect(0, 0, 15, 15)
        #15 by 15 square curor
        self.offset = - 100

    def cursor(self):
        self.game.draw_text('^', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_command(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    class MainMenu(Menu):
        def __init__(self, game):
            Menu.__init__(self, game)
            self.state = "Start"
            self.startx, self.starty = self.mid_w, self.mid_h + 30
            self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
            self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
            self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def menu_screen(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.WHITE)
            self.game.draw_text('Main Menu', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 15, self.startx, self.starty)
            self.draw_cursor()
            self.blit_screen()

    def input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True

def Game(self):
    def __init__(self):
        pygame.init()
        self.running, self.playing = True,False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        #font
        self.font_name = pygame.font.get_default_font()
        #color
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.curr_menu(self)

    def game_command(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            #reset screen to clear old
            self.draw_text('Game In Progress Still!', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
            #set everything back to false
    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #break game cycle
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                #check if they're still playing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        #resets the keys

    def text(self, text, size, x,y):
        font= pygame.font.Font(self.font_name, size)
        text_s = font.render(text, True, self.BLACK)
        text_r = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

run_game = Game(self)

while run_game.running:
    run_game.curr_menu.menu_screen(self)
    run_game.game_command()
