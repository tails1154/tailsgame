import os
import pygame
import json
import sys
import subprocess
# pygame setup
pygame.init()
pygame.mixer.init()
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
ready=False
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
            if event.key == pygame.K_SPACE:
                if ready:
                    gameReading=False
                    ready=False
                    print("Starting!")
                    game.start(mount)
                    print("Game Ended...")
                    running = True
                    ready=False
                    screen.fill("blue")
                    pygame.quit()
                    sys.exit(0)

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
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        subprocess.call(['udisksctl', 'unmount', '-f', '-b', floppy])
        result = subprocess.run(
            ['udisksctl', 'mount', '-b', floppy],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        mount = result.stdout.split("Mounted " + floppy + " at ")[1]
        print(mount)
        #return mount
        #print(mount)
        #mount = mountiguess()
        print(mount)
        print("removing stupid new line")
        mount = mount.replace("\n", "")
        print(mount)
        print("adding to path")
        sys.path.insert(0, mount)
        print(sys.path)
        print("Importing game")
        import game
        ready=True
        gameReading=False
        menu=False
        screen.fill("blue")
    if ready:
        screen.fill("blue")
        text_surface = font.render("Press space to start!", True, (255,255,255))
        text_rect = text_surface.get_rect(center=(400, 300))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
def playsong(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
def pausesong():
    pygame.mixer.music.pause()
def unpausesong():
    pygame.mixer.music.unpause()
def rewindsong():
    pygame.mixer.music.rewind()
