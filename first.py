import pygame

# init pygame 
pygame.init()

# Display Screen
WIDTH , HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Caption = 
pygame.display.set_caption("hi")

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("you pressed q! ")
            else:
                x=0
                while x<10:
                    pygame.draw.rect(screen, (255,0,0), (100, 10+10*x, 100 , 100))
                    pygame.display.flip() # pygame.quit()
                    x=x+1
