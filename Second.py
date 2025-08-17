import pygame as py

# initilization
py.init()

# dislplay 
WIDTH, HEIGHT = 500, 500
screen = py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Second Game :D ")


x = 250
y = 250 
speed = 0.1

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            break
        
    keys = py.key.get_pressed()
    if keys[py.K_LEFT] or keys[py.K_6] or keys[py.K_a]:
        x -= speed
        print("left")
    if keys[py.K_RIGHT] or keys[py.K_4] or keys[py.K_d]:
        x +=speed
        print("right")
    if keys[py.K_UP] or keys[py.K_8] or keys[py.K_w]:
        y -= speed
        print("up")
    if keys[py.K_DOWN] or keys[py.K_2] or keys[py.K_s]:
        y += speed
        print("down")

    screen.fill((0, 0, 0))
    py.draw.rect(screen, (255, 255, 255), (x, y, 100, 100))
    py.display.flip() 