import pygame

class Cell:
    def __init__(self):
        self.clicked = False

grid_size = 10
board = [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]

pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:    
            if event.button == 1:
                row = event.pos[1] // 20
                col = event.pos[0] // 20
                board[row][col].clicked = True

    window.fill(0)
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            color = (64, 64, 64) if cell.clicked else (164, 164, 164)
            pygame.draw.rect(window, color, (ix*20+1, iy*20+1, 18, 18))
    pygame.display.flip()

pygame.quit()
exit()