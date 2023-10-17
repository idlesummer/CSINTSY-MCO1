import pygame


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")


player = pygame.Rect((0, 0, 50, 50))

run = True
while run:
    
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
        
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
        
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
            
pygame.quit()