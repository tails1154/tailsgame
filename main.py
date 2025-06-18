print("Starting TailsGame...")
print("BGMusic in menu from msn tv 2")
import os
import pygame
import json
import sys
import subprocess
import requests
import time
# pygame setup

pygame.init()
pygame.mixer.init()
def gameInfo(gameId):
    eshop = False
    game = next(key for key, value in games.items() if value["id"] == gameId)  # Look for the correct gameId
    screen.fill("orange")
    eshop = False
    eshopinfo = True
    drawText(game, 100, 50, screen)  # Draw the game title
    drawText(f"Description: {games[game]['description']}", 500, 90, screen)  # Draw the description
    drawText(f"Author: {games[game]['author']}", 500, 130, screen)  # Draw the author
    drawText("Press enter to download and run", 500, 170, screen)
    pygame.display.flip()

    # Wait for a key event before returning to the menu
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # When Enter is pressed, go back
                    waiting_for_input = False
                    screen.fill("orange")
                    drawText("Downloading Game", 500, 500, screen)
                    pygame.display.flip()
                    r = requests.get(server + "/download?game=" + gameId + ".py")
                    # exec(r.text)
                    with open('game.py', 'w') as file:
                        file.write(r.text)
                    print("Importing game")
                    import game
                    print("Starting!")
                    pygame.mixer.music.stop();pygame.mixer.music.unload()
                    game.start(os.getcwd())
                    print("Game Ended...")
                    running = True
                    ready=False
                    screen.fill("blue")
                    pygame.quit()
                    sys.exit(0)

def waitForSound():
    while pygame.mixer.music.get_busy():
        1+1
def playSound(location):
    pygame.mixer.music.unload()
    pygame.mixer.music.load(location, namehint="mp3")
    pygame.mixer.music.play()
def drawText(text, x, y, screen):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
clock = pygame.time.Clock()
running=False
def drawPage(page, games):
    counter = 0
    y_pos = 50
    out = 0
    out += page * 5
    screen.fill("orange")

    # Start from the "out" index, skipping the first "out" games
    for i, (game_name, game_info) in enumerate(games.items()):
        if i < out:  # Skip the first "out" games
            continue

        if counter >= 5:
            break

        # Drawing each game's info
        game_id = game_info["id"]
        game_description = game_info["description"]
        drawText(f"{game_id}. {game_name}", 100, y_pos, screen)
        y_pos += 40  # Move to the next line
        counter += 1
    drawText(f"Page {page}", 100, y_pos, screen)

def start():
    global running
    global server
    global serveractive
    serveractive=False
    running = True
    pygame.init()
try:
    print("BGMusic in menu from msn tv 2")
    print("Loading config.json...")
    f = open("config.json", "rt")
    config=f.read()
    print(config)
    config=json.loads(config)
    print(config)
    print("TailsGame Version v2.0.0")
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
    if config['fullscreen']:
        print("[INFO] fullscreen option found: " + config['fullscreen'])
        if config['fullscreen'] == "True":
            flags=pygame.FULLSCREEN
            screen = pygame.display.set_mode((1280, 720), flags)
        else:
            screen = pygame.display.set_mode((1280, 720))
    try:
        if config['server']:
            server=config['server']
            serveractive=True
            print("[INFO] Loaded server: " + server)
    except:
        print("[WARNING] Exception occoured when trying to read server field in config.json . online functions will be disabled.")
        serveractive=False
    # else:
    #     screen = pygame.display.set_mode((1280, 720))
    menu=True
    gameReading=False
    ready=False
    rmplay=False
    eshop=False
    eshoploading=False
    eshopcatalogloading=False
    catalog=False
    eshopinfo=False
    page = 0
    font = pygame.font.Font(None, 36)
    gameid = 0
    if __name__ == '__main__':
        start()
    def restart():
        start()
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
                        pygame.mixer.music.load("audio/wait.mp3", namehint="mp3")
                        pygame.mixer.music.play(loops=-1)
                if event.key == pygame.K_s:
                    if menu:
                        playSound("audio/eshop.mp3")
                        menu=False
                        eshoploading=True
                if event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:  # Check for number key press
                    game_id = str(event.key - pygame.K_0)  # Get the number key pressed
                    # Find the game name by the ID
                    for game_name, game_info in games.items():
                        if game_info["id"] == game_id:
                            print(f"Selected game: {game_name}")
                            gameid = game_info["id"]
                            gameInfo(game_info["id"])
                            break
                if event.key == pygame.K_RIGHT:
                    if eshop:
                        page = page + 1
                if event.key == pygame.K_LEFT:
                    if eshop:
                        page = page - 1


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("blue")


        if menu:
            text_surface = font.render("Insert Game Floppy and press Enter", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(400, 300))
            screen.blit(text_surface, text_rect)
            drawText("Press s for game shop", 400, 500, screen)
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
            ready=True
            gameReading=False
            menu=False
            screen.fill("blue")
        if ready:
            screen.fill("blue")
            if True:
                    if ready:
                        gameReading=False
                        ready=False
                        screen.fill("blue")
                        text_surface = font.render("Starting...", True, (255, 255, 255))
                        text_rect = text_surface.get_rect(center=(400, 300))
                        screen.blit(text_surface, text_rect)
                        pygame.display.flip()
                        # pygame.mixer.music.load("audio/start.mp3", namehint="mp3")
                        # pygame.mixer.music.play()
                        # while pygame.mixer.music.get_busy():
                        #     1+1
                        # pygame.mixer.music.stop()
                        # pygame.mixer.music.unload()
                        pygame.mixer.music.load("audio/wait.mp3", namehint="mp3")
                        pygame.mixer.music.play(loops=-1)
                        print("Importing game")
                        import game
                        print("Starting...")
                        pygame.mixer.music.stop();pygame.mixer.music.unload()
                        game.start(mount)
                        print("Game Ended...")
                        running = True
                        ready=False
                        screen.fill("blue")
                        pygame.quit()
                        sys.exit(0)

            # text_surface = font.render("Press space to start!", True, (255,255,255))
            if not rmplay:
                rmplay=True
                pygame.mixer.music.load("audio/gameread.mp3", namehint="mp3")
                pygame.mixer.music.play()
            text_rect = text_surface.get_rect(center=(400, 300))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
        if eshoploading:
            try:
                screen.fill("orange")
                drawText("TailsGame shop", 300, 500, screen)
                pygame.display.flip()
                r = requests.get(server + "/hello")
                if r.status_code == 200:
                    eshoploading=False
                    eshopcatalogloading=True
                else:
                    pygame.mixer.stop()
                    pygame.mixer.unload()
                    playSound("audio/error.mp3")
                    waitForSound()
                    drawText("Error Loading Shop", 300, 300, screen)
            except Exception as e:
                print("Exception:")
                print(e)
                playSound("audio/error.mp3")
                # waitForSound()
                screen.fill("orange")
                drawText("Error connecting: Check console for details", 500, 500, screen)
                pygame.display.flip()
                time.sleep(3)
                waitForSound()
                eshoploading=False
                eshop=False
                menu=True
        if eshopcatalogloading:
            try:
                # games = catalog
                screen.fill("orange")
                drawText("TailsGame shop", 300, 500, screen)
                drawText("Loading catalog", screen.get_width() // 2, screen.get_height() // 2, screen)
                pygame.display.flip()
                r = requests.get(server + "/catalog")
                if r.status_code == 200:
                    catalog = json.loads(r.text)
                    eshopcatalogloading=False
                    eshop=True
                else:
                    raise Exception("Not 200 Status code")
            except Exception as e:
                print("Exception:")
                print(e)
                playSound("audio/error.mp3")
                # waitForSound()
                screen.fill("orange")
                drawText("Error connecting: Check console for details", 500, 500, screen)
                pygame.display.flip()
                time.sleep(3)
                waitForSound()
                eshoploading=False
                eshopcatalogloading=False
                eshop=False
                menu=True


        if eshop:
            try:
                games = catalog
                screen.fill("orange")
                # drawText("TailsGame shop", 300, 500, screen)
                y_pos = 50  # Starting Y position for drawing text
                try:
                    drawPage(page, games)
                except Exception as e:
                    print("Exception: Most likely last or first page")
                    print(e)
                # for game_name, game_info in games.items():
                #     # Drawing each game's info
                #     game_id = game_info["id"]
                #     game_description = game_info["description"]
                #     drawText(f"{game_id}. {game_name}", 50, y_pos, screen)
                #     y_pos += 40  # Move to the next line
                # for event in pygame.event.get():
                #     if event.type == pygame.QUIT:
                #         running = False

            except Exception as e:
                print("Exception:")
                print(e)
                playSound("audio/error.mp3")
                # waitForSound()
                screen.fill("orange")
                drawText("Error connecting: Check console for details", 500, 500, screen)
                pygame.display.flip()
                time.sleep(3)
                waitForSound()
                eshoploading=False
                eshop=False
                eshopcatalogloading=False
                menu=True
        if eshopinfo:
            try:
                gameInfo(gameid)
            except Exception as e:
                print("Exception:")
                print(e)
                playSound("audio/error.mp3")
                # waitForSound()
                screen.fill("orange")
                drawText("Error displaying info: Check console for details", 500, 500, screen)
                pygame.display.flip()
                # time.sleep(3)
                waitForSound()
                eshoploading=False
                eshop=True
                eshopcatalogloading=False
                menu=False
                eshopinfo=False

    # pygame.display.flip()  # Update the screen

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
except Exception as e:
    print("Tails1154 Unhandled exception:")
    # print(repo(e))
    print(repr(e))
    # pygame.init()
    pygame.quit()
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1280, 720))
    font = pygame.font.Font(None, 36)
    # time.sleep(1)
    drawText("Tails1154 Unhandled Exception: Check console for details", 500, 500, screen)
    pygame.display.flip()
    playSound("audio/fatal.mp3")
    waitForSound()
    pygame.quit()
    sys.exit()
pygame.quit()
print("Exit")
sys.exit()
