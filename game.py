import sys, pygame

run = True
pygame.init()
size = width, height = 1000, 1000

black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)

loadingscreen = True


def drawboard():
    board = pygame.image.load("board.jpeg")
    board = pygame.transform.scale(board, (size))
    boardrect = board.get_rect()
    screen.blit(board, boardrect)
    

def drawmove():
    xicon = pygame.image.load("x.png")
    xicon = pygame.transform.scale(xicon, (200, 200))
    xrect = xicon.get_rect()
    screen.blit(xicon, xrect)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        

        if event.type == pygame.mouse.get_pressed():
            mouseposition = pygame.mouse.get_pos()
            print (mouseposition)  
    drawboard()
    drawmove()
    pygame.display.update()