import pygame
from pygame.locals import *
import random
from itertools import product
from pygame.color import Color

# Initialize
pygame.init()

# Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

# Works the text
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Colors for the code
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Font basic font
font = pygame.font.get_default_font()

# Main Menu
def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        print("Start")
                        # initializing values
                        # start of code for game
                        #this is for size
                        SCREEN_WIDTH = 800
                        SCREEN_HEIGHT = 400
                        SQUARE_SIZE = 50
                        SQUARE_GAP = 10
                        BOARD_WIDTH = 8
                        BOARD_HEIGHT = 4
                        X_MARGIN = (SCREEN_WIDTH - (BOARD_WIDTH * (SQUARE_SIZE + SQUARE_GAP))) // 2
                        Y_MARGIN = (SCREEN_HEIGHT - (BOARD_HEIGHT * (SQUARE_SIZE + SQUARE_GAP))) // 2

                        # the board size must be even due to pairs because they have to match
                        assert (BOARD_HEIGHT * BOARD_WIDTH) % 2 == 0, 'The board size must be even'

                        # the shapes used for matching
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

                            coordinates = list(product(range(BOARD_HEIGHT), range(BOARD_WIDTH)))
                            random.shuffle(coordinates)

                            revealed = [[False] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]

                            screen.fill(BGCOLOR)
                            draw_board(board, revealed)
                            pygame.display.update()
                            pygame.time.wait(500)

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
                                pygame.draw.polygon(screen, icon[1],
                                                    ((px + SQUARE_SIZE // 2, py + 5), (px + SQUARE_SIZE - 5, py + SQUARE_SIZE // 2),
                                                     (px + SQUARE_SIZE // 2, py + SQUARE_SIZE - 5), (px + 5, py + SQUARE_SIZE // 2)))
                            elif icon[0] == SQUARE:
                                pygame.draw.rect(screen, icon[1],
                         (px + 5, py + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
                            elif icon[0] == TRIANGLE:
                                pygame.draw.polygon(screen, icon[1],
                                                    ((px + SQUARE_SIZE // 2, py + 5), (px + 5, py + SQUARE_SIZE - 5),
                                                     (px + SQUARE_SIZE - 5, py + SQUARE_SIZE - 5)))
                            elif icon[0] == CIRCLE:
                                pygame.draw.circle(screen, icon[1],
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
                            pygame.draw.rect(screen, BGCOLOR, square_rect)
                            if revealed[x][y]:
                                draw_icon(board[x][y], x, y)
                            else:
                                pygame.draw.rect(screen, Color('grey'), square_rect)
                            pygame.display.update(square_rect)

                        def draw_board(board, revealed):
                            """Draws the entire board"""

                            for x in range(BOARD_HEIGHT):
                                for y in range(BOARD_WIDTH):
                                    draw_square(board, revealed, x, y)

                        def draw_select_box(x, y):
                            """Draws the highlight box around the square"""

                            px, py = get_coord(x, y)
                            pygame.draw.rect(screen, Color('red'), (px - 5, py - 5, SQUARE_SIZE + 10, SQUARE_SIZE + 10), 5)


                        # the main function
                        def main():
                            global screen, clock

                            pygame.init()

                            screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
                            pygame.display.set_caption('Memory Game')

                            clock = pygame.time.Clock()

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

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        running = False
                                    elif event.type == MOUSEMOTION:
                                        mouse_x, mouse_y = pygame.mouse.get_pos()
                                    elif event.type == MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = pygame.mouse.get_pos()
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
                                                pygame.time.wait(1000)
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
                                pygame.display.update()

                            else:
                               pygame.quit()
                               quit()
       

                        if __name__ == '__main__':
                            main()
                            
                    if selected=="quit":
                        pygame.quit()
                        quit()


        # Code that makes up what is said on the main menu
        screen.fill(black)
        title=text_format("Matching Game!", font, 90, red)
        if selected=="start":
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, white)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, white)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        pygame.display.set_caption("Menu")

#Initialize the Game
main_menu()
pygame.quit()
quit()
