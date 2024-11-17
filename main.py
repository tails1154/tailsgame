import pygame
import json
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
print("Loading config.json...")
f = open("config.json", "rt")
config=f.read()
print(config)
config=json.loads(config)
print(config)
print("TailsGame Version v0.0.1")
if config['floppy_location']:
    print("found config option floppy_location")
    floppy=config['floppy_location']
else:
    print("Config Error!")
    print("floppy_location not set!")
    sys.exit(1)
if config['mount_location']:
    print("Found config option mount_location")
    mount=config['mount_location']
else:
    print("Config Error!")
    print("mount_location not set!")
    sys.exit(1)
menu=True
gameReading=False
font = pygame.font.Font(None, 36)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if menu:
                    menu=False
                    gameReading=True
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")


    if menu:
        text_surface = font.render("Insert Game Floppy and press Enter", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        screen.blit(text_surface, text_rect)
    if gameReading:
        text_surface = font.render("Reading Game...", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
