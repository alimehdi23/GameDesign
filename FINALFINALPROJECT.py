import pygame
import random
from itertools import product
from pygame.locals import *
from pygame.color import Color

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
            # initializing values
            SCREEN_WIDTH = 800
            SCREEN_HEIGHT = 400
            SQUARE_SIZE = 50
            SQUARE_GAP = 10
            BOARD_WIDTH = 8
            BOARD_HEIGHT = 4
            X_MARGIN = (SCREEN_WIDTH - (BOARD_WIDTH * (SQUARE_SIZE + SQUARE_GAP))) // 2
            Y_MARGIN = (SCREEN_HEIGHT - (BOARD_HEIGHT * (SQUARE_SIZE + SQUARE_GAP))) // 2

            # the board size must be even due to pairs
            assert (BOARD_HEIGHT * BOARD_WIDTH) % 2 == 0, 'The board size must be even'

            # the shapes
            DIAMOND = 'diamond'
            SQUARE = 'square'
            TRIANGLE = 'triangle'
            CIRCLE = 'circle'

            BGCOLOR = Color('white')


            # reseting the shape
            def game_won(revealed):
                return all(all(x) for x in revealed)

            # function at the sart of the game
            def start_game_animation(board):
                """Starts game by randomly showing 5 squares"""

                coordinates = list(product(range(BOARD_HEIGHT), range(BOARD_WIDTH)))
                random.shuffle(coordinates)

                revealed = [[False] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]

                screen.fill(BGCOLOR)
                draw_board(board, revealed)
                pg.display.update()
                pg.time.wait(500)

            for sz in range(0, BOARD_HEIGHT * BOARD_WIDTH, 5):
                l = coordinates[sz: sz + 5]
                for x in l:
                    revealed[x[0]][x[1]] = True
                    draw_square(board, revealed, *x)
                pg.time.wait(500)
                for x in l:
                    revealed[x[0]][x[1]] = False
                    draw_square(board, revealed, *x)

            # setting up board
            def get_random_board(shape, colors):
                """ Generates the board by random shuffling"""

                icons = list(product(shape, colors))
                num_icons = BOARD_HEIGHT * BOARD_WIDTH // 2
                icons = icons[:num_icons] * 2

                random.shuffle(icons)
                board = [icons[i:i + BOARD_WIDTH]
                         for i in range(0, BOARD_HEIGHT * BOARD_WIDTH, BOARD_WIDTH)]
                return board


            def get_coord(x, y):
                """ Gets the coordinates of particular square.
                The squares are number height wise and then width wise.
                So the x and y are interchanged."""

                top = X_MARGIN + y * (SQUARE_SIZE + SQUARE_GAP)
                left = Y_MARGIN + x * (SQUARE_SIZE + SQUARE_GAP)
                return top, left


            def draw_icon(icon, x, y):
                """Draws the icon of (x, y) square"""

                px, py = get_coord(x, y)
                if icon[0] == DIAMOND:
                    pg.draw.polygon(screen, icon[1],
                                        ((px + SQUARE_SIZE // 2, py + 5), (px + SQUARE_SIZE - 5, py + SQUARE_SIZE // 2),
                                         (px + SQUARE_SIZE // 2, py + SQUARE_SIZE - 5), (px + 5, py + SQUARE_SIZE // 2)))
                elif icon[0] == SQUARE:
                    pg.draw.rect(screen, icon[1],
                                     (px + 5, py + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
                elif icon[0] == TRIANGLE:
                    pg.draw.polygon(screen, icon[1],
                                        ((px + SQUARE_SIZE // 2, py + 5), (px + 5, py + SQUARE_SIZE - 5),
                                         (px + SQUARE_SIZE - 5, py + SQUARE_SIZE - 5)))
                elif icon[0] == CIRCLE:
                    pg.draw.circle(screen, icon[1],
                                       (px + SQUARE_SIZE // 2, py + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)


            def get_pos(cx, cy):
                """Gets the square (x, y) position  from the cartesian coordinates.
                   The squares are number height wise and then width wise.
                   So the cx and cy are interchanged."""

                if cx < X_MARGIN or cy < Y_MARGIN:
                    return None, None

                x = (cy - Y_MARGIN) // (SQUARE_SIZE + SQUARE_GAP)
                y = (cx - X_MARGIN) // (SQUARE_SIZE + SQUARE_GAP)

                if x >= BOARD_HEIGHT or y >= BOARD_WIDTH or(cx - X_MARGIN) % (SQUARE_SIZE + SQUARE_GAP) > SQUARE_SIZE or (cy - Y_MARGIN) % (SQUARE_SIZE + SQUARE_GAP) > SQUARE_SIZE:
                    return None, None
                else:
                    return x, y

            def draw_square(board, revealed, x, y):
                """Draws a particular square"""

                coords = get_coord(x, y)
                square_rect = (*coords, SQUARE_SIZE, SQUARE_SIZE)
                pg.draw.rect(screen, BGCOLOR, square_rect)
                if revealed[x][y]:
                    draw_icon(board[x][y], x, y)
                else:
                    pg.draw.rect(screen, Color('grey'), square_rect)
                pg.display.update(square_rect)

            def draw_board(board, revealed):
                """Draws the entire board"""

                for x in range(BOARD_HEIGHT):
                    for y in range(BOARD_WIDTH):
                        draw_square(board, revealed, x, y)

            def draw_select_box(x, y):
                """Draws the highlight box around the square"""
                px, py = get_coord(x, y)
                pg.draw.rect(screen, Color('red'), (px - 5, py - 5, SQUARE_SIZE + 10, SQUARE_SIZE + 10), 5)


            # the main function
            def main():
                global screen, clock

                pg.init()

                screen = pg.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
                pg.display.set_caption('Memory Game')

                clock = pg.time.Clock()

                shape = (DIAMOND, SQUARE, TRIANGLE, CIRCLE)
                colors = (Color('brown'), Color('purple'), Color('orange'), Color('blue'))

                # There should be enough symbols
                assert len(shape) * len(colors) >= BOARD_HEIGHT * BOARD_WIDTH // 2,'There are not sufficient icons'

                board = get_random_board(shape, colors)
                revealed = [[False] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]  # keeps track of visibility of square

                mouse_x = None
                mouse_y = None
                mouse_clicked = False
                first_selection = None

                running = True
                start_game_animation(board)

                while running:
                    screen.fill(BGCOLOR)
                    draw_board(board, revealed)

                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            running = False
                        elif event.type == MOUSEMOTION:
                            mouse_x, mouse_y = pg.mouse.get_pos()
                        elif event.type == MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pg.mouse.get_pos()
                            mouse_clicked = True

                    x, y = get_pos(mouse_x, mouse_y)

                    if x is not None and y is not None:
                        if not revealed[x][y]:
                            if mouse_clicked:
                                revealed[x][y] = True
                                draw_square(board, revealed, x, y)

                                if first_selection is None:
                                    first_selection = (x, y)
                                else:
                                    pg.time.wait(1000)
                                    if board[x][y] != board[first_selection[0]][first_selection[1]]:
                                        revealed[x][y] = False
                                        revealed[first_selection[0]][first_selection[1]] = False
                                    first_selection = None

                                if game_won(revealed):

                                    board = get_random_board(shape, colors)
                                    revealed = [[False] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]
                                    start_game_animation(board)

                            else:
                                draw_select_box(x, y)

                    mouse_clicked = False
                    pg.display.update()

                else:
                   pg.quit()
                   quit()


            if __name__ == '__main__':
                main()
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

g = Game('self')

while g.running:
    g.curr_menu.menu_screen(self)
    g.game_command()
