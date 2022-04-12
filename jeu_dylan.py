import pygame as pyg
from random import randint
from sys import exit
import menu

clock = pyg.time.Clock()


def jeu():
    from jeu_1 import height, width, screen, win, loose, amongus, shake, explo
    from transition import trans_screen
    from Siorac import jeu_max
    from menu import base_menu
    global x_explo
    global y_explo
    global background
    global losescreen
    global xsoldat1
    global xsoldat
    global gamemode

    # importation et affichage du background
    background = pyg.image.load("img_dylan/fond1.jpg")
    background = pyg.transform.scale(background, (height, width))
    fond = background.convert()
    screen.blit(fond, (0, 0))
    pyg.display.flip()

    # importation et convertion des images en png
    para = pyg.image.load("img_dylan/para.png")
    para = pyg.transform.scale(para, (130, 170)).convert_alpha()
    tank = pyg.image.load("img_dylan/Tank.png")
    tank = pyg.transform.scale(tank, (200, 260)).convert_alpha()
    soldat = pyg.image.load("img_dylan/Soldat.png")
    soldat = pyg.transform.scale(soldat, (80, 120)).convert_alpha()
    soldat1 = pyg.image.load("img_dylan/Soldat.png")
    soldat1 = pyg.transform.scale(soldat1, (80, 120)).convert_alpha()
    degrade = pyg.image.load("img_dylan/degrade.png").convert_alpha()
    degrade = pyg.transform.scale(degrade, (200, 400))
    bombe = pyg.image.load("img_dylan/bombe.png").convert_alpha()
    bombe = pyg.transform.scale(bombe, (50, 50))
    paradore = pyg.image.load("img_dylan/paradore.png").convert_alpha()
    paradore = pyg.transform.scale(paradore, (130, 170))

    # importation des sfx
    son_explo = pyg.mixer.Sound('son/son_explo.wav')
    son_explo.set_volume(0.02)
    musique_jeu = pyg.mixer.Sound('son/synthware.mp3')
    musique_jeu.set_volume(0.02)
    ben_sfx = pyg.mixer.Sound('son/ben.mp3')
    ben_sfx.set_volume(1)

    # definitions des variables

    y_para = -100
    x_para = 0
    tankexplode = False
    tankcanexplode = False
    anim_explo = pyg.sprite.Group()
    explosion = explo(x_para, width - 300)
    anim_explo.add(explosion)
    point = 0
    x_tank = height / -9.6
    xsoldat = height / 3.49090909
    xsoldat1 = height / 1.28
    isleft = False
    isleft1 = False
    darkgreen = (12, 74, 0)
    black = (0, 0, 0)
    paramort = 0
    vitesse = 15
    acceleration = 1.1
    start_ticks = pyg.time.get_ticks()
    end = False
    bomb_can_explode = False
    paradore_can_spawn = False
    y_bomb = -100
    y_paradore = -100
    seconds_en_plus = 0
    # definition du lieu d'apparation du parachutiste
    chance = randint(1, 5)

    if chance == 1:
        x_para = height / 3.85
    if chance == 2:
        x_para = height / 2.75
    if chance == 3:
        x_para = height / 2.15
    if chance == 4:
        x_para = height / 1.75
    if chance == 5:
        x_para = height / 1.45

    chance = randint(1, 5)

    if chance == 1:
        x_bomb = height / 3.85
    if chance == 2:
        x_bomb = height / 2.75
    if chance == 3:
        x_bomb = height / 2.15
    if chance == 4:
        x_bomb = height / 1.75
    if chance == 5:
        x_bomb = height / 1.45

    chance = randint(1, 5)

    if chance == 1:
        x_paradore = height / 3.85
    if chance == 2:
        x_paradore = height / 2.75
    if chance == 3:
        x_paradore = height / 2.15
    if chance == 4:
        x_paradore = height / 1.75
    if chance == 5:
        x_paradore = height / 1.45

    pyg.image.load('img_dylan/black.jpg')

    place = [height / 3.85 - 50, height / 2.75 - 50, height / 2.15 - 50, height / 1.75 - 50, height / 1.45 - 50]
    base = 2
    place_selected = place[base]
    musique_jeu.play()
    game = 0
    # debut du jeu
    while True:
        seconds = round(30 - ((pyg.time.get_ticks() - start_ticks) / 1000)) + seconds_en_plus
        if not end:
            font = pyg.font.Font('freesansbold.ttf', 64)
            countdown = font.render(str(seconds), True, darkgreen, black)
            screen.blit(countdown, (200, width / 60))
        if game == 0:
            acceleration *= 1.0005
            son_explo.set_volume(0.02)
            # reaparition du parachutiste
            if y_para >= width:
                y_para = -100
                paramort += 1
                acceleration = 1.1
                point -= 1
                shake(30)
                chance = randint(1, 5)

                if chance == 1:
                    x_para = height / 3.85
                if chance == 2:
                    x_para = height / 2.75
                if chance == 3:
                    x_para = height / 2.15
                if chance == 4:
                    x_para = height / 1.75
                if chance == 5:
                    x_para = height / 1.45

            y_para += vitesse * acceleration

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    exit()

                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        musique_jeu.stop()
                        menu.base_menu()
                    if event.key == pyg.K_x:
                        seconds_en_plus -= 20
                    if event.key == pyg.K_b:
                        ben_sfx.play()
                    if event.key == pyg.K_m:
                        point += 10
                    if event.key == pyg.K_n:
                        point -= 10
                    if event.key == pyg.K_w:
                        musique_jeu.stop()
                        amongus()
                    if event.key == pyg.K_LEFT:
                        if base != 0:
                            base -= 1
                            place_selected = place[base]
                        else:
                            base = 4
                            place_selected = place[base]
                    elif event.key == pyg.K_RIGHT:
                        if base != 4:
                            base += 1
                            place_selected = place[base]
                        else:
                            base = 0
                            place_selected = place[base]
                    if width - 400 <= y_para <= width - 50:
                        if x_para == place_selected + 50:
                            if event.key == pyg.K_SPACE:
                                point += 1
                                anim_explo = pyg.sprite.Group()
                                explosion = explo(x_para, y_para)
                                anim_explo.add(explosion)
                                screen_shake = 40
                                y_para = -300
                                chance = randint(1, 5)
                                if chance == 1:
                                    x_para = height / 3.85
                                if chance == 2:
                                    x_para = height / 2.75
                                if chance == 3:
                                    x_para = height / 2.15
                                if chance == 4:
                                    x_para = height / 1.75
                                if chance == 5:
                                    x_para = height / 1.45
                                explosion.animate()
                                anim_explo.draw(screen)
                                anim_explo.update(0.35)
                                shake(screen_shake)
                                son_explo.play()
                                paramort += 1
                                vitesse += 1
                                point += 1

                if width - 400 >= y_para or x_para != place_selected + 50:
                    if not paradore_can_spawn:
                        if event.type == pyg.KEYDOWN:
                            if event.key == pyg.K_SPACE:
                                point -= 1
                                chance = randint(1, 5)
                                if chance == 1:
                                    x_para = height / 3.85
                                if chance == 2:
                                    x_para = height / 2.75
                                if chance == 3:
                                    x_para = height / 2.15
                                if chance == 4:
                                    x_para = height / 1.75
                                if chance == 5:
                                    x_para = height / 1.45
                                y_para = -100
                                shakex = randint(-10, 10)
                                shakey = randint(-10, 10)
                                screen.blit(background, (shakex, shakey))
                                paramort += 1
                                vitesse -= 1

                if bomb_can_explode:
                    if width - 400 <= y_bomb <= width - 50:
                        if x_bomb == place_selected + 50:
                            if event.key == pyg.K_SPACE:
                                anim_explo = pyg.sprite.Group()
                                explosion = explo(x_bomb, y_bomb - 25)
                                anim_explo.add(explosion)
                                explosion.animate()
                                anim_explo.draw(screen)
                                anim_explo.update(0.35)
                                shake(30)
                                son_explo.play()
                                seconds_en_plus -= 2
                                bomb_can_explode = False
                                y_bomb = -100
                                chance = randint(1, 5)
                                if chance == 1:
                                    x_bomb = height / 3.85
                                if chance == 2:
                                    x_bomb = height / 2.75
                                if chance == 3:
                                    x_bomb = height / 2.15
                                if chance == 4:
                                    x_bomb = height / 1.75
                                if chance == 5:
                                    x_bomb = height / 1.45
                    elif y_bomb > width:
                        y_bomb = -100
                        bomb_can_explode = False
                        chance = randint(1, 5)
                        if chance == 1:
                            x_bomb = height / 3.85
                        if chance == 2:
                            x_bomb = height / 2.75
                        if chance == 3:
                            x_bomb = height / 2.15
                        if chance == 4:
                            x_bomb = height / 1.75
                        if chance == 5:
                            x_bomb = height / 1.45
                        acceleration = 1.1

                if paradore_can_spawn:
                    if width - 400 <= y_paradore <= width - 50:
                        if x_paradore == place_selected + 50:
                            if event.key == pyg.K_SPACE:
                                anim_explo = pyg.sprite.Group()
                                explosion = explo(x_paradore, y_paradore - 25)
                                anim_explo.add(explosion)
                                explosion.animate()
                                anim_explo.draw(screen)
                                anim_explo.update(0.35)
                                shake(30)
                                son_explo.play()
                                seconds_en_plus += 1
                                y_paradore = -100
                                chance = randint(1, 5)
                                if chance == 1:
                                    x_paradore = height / 3.85
                                if chance == 2:
                                    x_paradore = height / 2.75
                                if chance == 3:
                                    x_paradore = height / 2.15
                                if chance == 4:
                                    x_paradore = height / 1.75
                                if chance == 5:
                                    x_paradore = height / 1.45
                                point += 1
                                acceleration *= 1.005
                                paradore_can_spawn = False

                    elif y_paradore > width:
                        y_paradore = -100
                        chance = randint(1, 5)
                        if chance == 1:
                            x_paradore = height / 3.85
                        if chance == 2:
                            x_paradore = height / 2.75
                        if chance == 3:
                            x_paradore = height / 2.15
                        if chance == 4:
                            x_paradore = height / 1.75
                        if chance == 5:
                            x_paradore = height / 1.45
                        acceleration = 1.1
                        paradore_can_spawn = False

            screen.blit(soldat, (xsoldat, width / 1.992611))
            screen.blit(soldat1, (xsoldat1, width / 2.037735849))
            if isleft:
                xsoldat -= 0.4
                if xsoldat < height / 3.67:
                    isleft = False
                    soldat = pyg.transform.flip(soldat, True, False)
            if not isleft:
                xsoldat += 0.2
                if xsoldat > height / 3.06:
                    isleft = True
                    soldat = pyg.transform.flip(soldat, True, False)

            if isleft1:
                xsoldat1 -= 0.2
                if xsoldat1 < height / 1.338912133891213:
                    isleft1 = False
                    soldat1 = pyg.transform.flip(soldat1, True, False)
            if not isleft1:
                xsoldat1 += 0.3
                if xsoldat1 > height / 1.248374512353706:
                    isleft1 = True
                    soldat1 = pyg.transform.flip(soldat1, True, False)

            if x_tank == -50:
                tankcanexplode = True
                x_tank = -50.1
            elif x_tank < -50:
                x_tank += height / 3840
            chance1 = randint(1, 500)
            if chance1 == 20:
                if tankcanexplode:
                    tankcanexplode = False
                    tankexplode = True
                    anim_explo = pyg.sprite.Group()
                    explosion = explo(height / 192, width / 2.117647059)
                    anim_explo.add(explosion)
                    explosion.animate()
                    anim_explo.draw(screen)
                    anim_explo.update(0.35)
                    son_explo.set_volume(0.01)
                    son_explo.play()

            if vitesse == 0:
                vitesse = 1

            if tankexplode:
                screen.blit(tank, (-1000, -1000))
            else:
                screen.blit(tank, (x_tank, width / 2.373626374))

            anim_explo.draw(screen)
            anim_explo.update(0.30)
            pyg.display.flip()
            pyg.display.update()
            screen.blit(background, (0, 0))
            screen.blit(para, (x_para, y_para))
            font = pyg.font.Font('freesansbold.ttf', 64)
            text = font.render(str(point), True, darkgreen, black)
            screen.blit(text, (height / 1.1, width / 60))
            screen.blit(degrade, (place_selected, width - 400))

            if seconds <= 0:
                end = True
            if end:
                if menu.gamemode == 1:
                    if point >= 30:
                        musique_jeu.stop()
                        win()
                    else:
                        musique_jeu.stop()
                        loose()
                else:
                    if point >= 30:
                        musique_jeu.stop()
                        trans_screen()
                        jeu_max()
                    if point == -69:
                        musique_jeu.stop()
                        amongus()
                    else:
                        musique_jeu.stop()
                        loose()

            luck_bombe = randint(1, 300)
            if luck_bombe == 1:
                bomb_can_explode = True

            if bomb_can_explode:
                screen.blit(bombe, (x_bomb + 25, y_bomb))
                y_bomb += vitesse * acceleration

            luck_paradore = randint(1, 600)
            if luck_paradore == 1:
                paradore_can_spawn = True

            if paradore_can_spawn:
                y_paradore += vitesse * acceleration
                screen.blit(paradore, (x_paradore, y_paradore))

            clock.tick(60)
