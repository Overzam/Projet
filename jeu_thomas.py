# Importation des librairies
import pygame as pyg

# initialisation de pygame
pyg.init()
pyg.mixer.init()
pyg.font.init()
music = pyg.mixer.Sound('son/synthware.mp3')
music.set_volume(0.02)

# initialisation de l'horloge
clock = pyg.time.Clock()


def jeu_tomaye():
    from jeu_1 import screen, width, height, win, loose
    from jeu_elliott import jeu_ell
    from transition import trans_screen
    import menu

    # initialisation de pygame
    pyg.init()
    pyg.mixer.init()
    pyg.font.init()

    # importation et affichage de l'icone du jeu
    icon = pyg.image.load('img_thomas/icone.jpg')
    pyg.display.set_icon(icon)

    # importation des sprites
    tank = pyg.image.load("img_thomas/tank.png")
    tank = pyg.transform.scale(tank, (100, 80)).convert_alpha()
    avion = pyg.image.load("img_thomas/avion.png")
    avion = pyg.transform.scale(avion, (120, 80)).convert_alpha()
    fleche = pyg.image.load("img_thomas/fleche.png")
    fleche = pyg.transform.scale(fleche, (height // 4, width // 4)).convert_alpha()
    flechepressed = pyg.image.load("img_thomas/flechepressed.png")
    flechepressed = pyg.transform.scale(flechepressed, (height // 4, width // 4)).convert_alpha()
    barre = pyg.image.load("img_thomas/barre.png")
    feu = pyg.image.load("img_thomas/feu.png")
    feu = pyg.transform.scale(feu, (height, width))
    # importation et affichage du background
    background = pyg.image.load("img_thomas/Fond_Thomas_2.jpg")
    background = pyg.transform.scale(background, (height, width))
    fond = background.convert()
    screen.blit(fond, (0, 0))
    pyg.display.flip()
    start_ticks = pyg.time.get_ticks()
    # les variables en sah
    xtank = height / 9
    ytank = width / 1.5
    xavion = height / 9
    yavion = width / 4
    darkgreen = (12, 74, 0)
    black = (0, 0, 0)
    Leftkey = False
    Rightkey = False
    xfleche = height / 2.5
    yfleche = width / 50
    nbtouches = 0

    avionsEnRoute = True
    # lancement du jeu mon bébou
    music.play()
    while avionsEnRoute:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT and Leftkey == False:
                    xavion += height / 15
                    nbtouches += 1
                    Leftkey = True
                    Rightkey = False
                    screen.blit(avion, (xavion, yavion))
                if event.key == pyg.K_RIGHT and Rightkey == False:
                    xtank += height / 15
                    nbtouches += 1
                    Rightkey = True
                    Leftkey = False
                    screen.blit(tank, (xtank, ytank))

        xtank -= width / 400
        xavion -= width / 400
        seconds = round(10 - ((pyg.time.get_ticks() - start_ticks) / 1000))
        screen.blit(tank, (xtank, ytank))
        screen.blit(avion, (xavion, yavion))
        if seconds <= 0:
            if xavion and xtank <= height / 1.40 and xavion and xtank >= height / 2:
                if menu.gamemode == 1:
                    music.stop()
                    win()
                else:
                    music.stop()
                    trans_screen()
                    jeu_ell()
            else:
                music.stop()
                loose()
        font = pyg.font.Font('freesansbold.ttf', 64)
        countdown = font.render(str(seconds), True, darkgreen, black)
        screen.blit(countdown, (200, height / 60))
        if nbtouches >= 100:
            screen.blit(feu, (0, 0))
        if seconds >= 8:
            screen.blit(fleche, (xfleche, yfleche))
        if 8 > seconds >= 5:
            screen.blit(flechepressed, (xfleche, yfleche))
        screen.blit(barre, (0, 0))
        pyg.display.update()
        pyg.display.flip()
        screen.blit(fond, (0, 0))
