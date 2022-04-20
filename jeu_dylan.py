# importation des bibliotheque a utiliser
import pygame as pyg
from random import randint
from sys import exit
import menu

# initialisation de lhorloge
clock = pyg.time.Clock()


def jeu():
    # importation des autres bibliotheque a utiliser
    from jeu_1 import height, width, screen, win, loose, amongus, shake, explo
    from transition import trans_screen_mouse
    from jeu_maximilien import jeu_max
    from menu import base_menu
    global x_explo
    global y_explo
    global background
    global losescreen
    global xsoldat1
    global xsoldat
    global gamemode

    # importation et affichage du background
    background = pyg.image.load("img_dylan/fond2.png")
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
    musique_jeu.play()
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
    base = 2
    seconds = 30

    # definition du lieu d'apparation du parachutiste, de la bombe, et du parachutiste doré
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

    # création d'une liste avec tous les endroits ou peuvent apparaitre les parachutiste, bombe, et parachutiste doré
    place = [height / 3.85 - 50, height / 2.75 - 50, height / 2.15 - 50, height / 1.75 - 50, height / 1.45 - 50]
    place_selected = place[base]
    # reinitialisation au cas ou un autre jeu modifiant cette valeur a ete lancé
    pyg.key.set_repeat()

    # debut du jeu
    while True:
        if not end:
            font = pyg.font.Font('freesansbold.ttf', 64)
            countdown = font.render(str(seconds), True, darkgreen, black)

        # definition et affichage du compte a rebourd avant la fin du jeu
        seconds = round(30 - ((pyg.time.get_ticks() - start_ticks) / 1000)) + seconds_en_plus
        screen.blit(countdown, (200, width / 60))
        # definition d'une acceleration pour que la gravité s'applique au parachutiste et incrementation du y du parchutiste
        acceleration *= 1.0005
        y_para += vitesse * acceleration

        # ajustement du son de l'explosion
        son_explo.set_volume(0.02)

        # reaparition du parachutiste
        if y_para >= width:
            # redefinition du y
            y_para = -100

            # redefinition du l'acceleration
            acceleration = 1.1

            # retrait d'un point car dans ce cas, le joueur n'a pas fait explosé le parachutiste avant qu'il atteigne le bas
            point -= 1

            # tremblement de l'ecran
            shake(30)

            # definition du lieu d'appartion du parchutiste
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

        for event in pyg.event.get():
            # si le joueur quitte le jeu, la fenetre se ferme
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()

            if event.type == pyg.KEYDOWN:
                # retour au menu si bouton escape pressé
                if event.key == pyg.K_ESCAPE:
                    musique_jeu.stop()
                    base_menu()
                # ben si b pressé
                if event.key == pyg.K_b:
                    ben_sfx.play()
                # amogus si w pressé
                if event.key == pyg.K_w:
                    musique_jeu.stop()
                    amongus()
                # deplacement vers la gauche si fleche gauche pressé ou "q"
                if event.key == pyg.K_LEFT or event.key == pyg.K_q:
                    # deplacement du curseur blanc en fonction avec le liste contenant les lieux possible d'apparition du parachutiste
                    if base != 0:
                        base -= 1
                        place_selected = place[base]

                    else:
                        base = 4
                        place_selected = place[base]
                # deplacement vers la droite si fleche gauche pressé ou "d"
                elif event.key == pyg.K_RIGHT or event.key == pyg.K_d:
                    # deplacement du curseur blanc en fonction avec le liste contenant les lieux possible d'apparition du parachutiste
                    if base != 4:
                        base += 1
                        place_selected = place[base]

                    else:
                        base = 0
                        place_selected = place[base]

                # si le parachutiste se touve dans les bonnes conditions et que le joueur appui sur espace, il explose et se retrouve tout en haut
                if width - 400 <= y_para <= width - 50:
                    if x_para == place_selected + 50:
                        if event.key == pyg.K_SPACE:
                            # incrementation d'un point
                            point += 2

                            # animation de l'explosion
                            anim_explo = pyg.sprite.Group()
                            explosion = explo(x_para, y_para)
                            anim_explo.add(explosion)

                            # tramblement de l'ecran
                            screen_shake = 40
                            shake(screen_shake)
                            # reinitialisation du y du parachutiste
                            y_para = -300

                            # reinitialisation du x du parachutiste
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

                            # animation de l'explosion
                            explosion.animate()
                            anim_explo.draw(screen)
                            anim_explo.update(0.35)

                            # sfx joué
                            son_explo.play()

                            # si le joueur en tue plein d'affillé le jeu devient plus dur
                            vitesse += 1

            # si le joueur appuie sur espace alors que le x et y ne sont pas bon et que le parachutiste doré ne peut pas apparaitre
            if width - 400 >= y_para or x_para != place_selected + 50:
                if not paradore_can_spawn:
                    if event.type == pyg.KEYDOWN:
                        if event.key == pyg.K_SPACE:
                            # decrementation d'un point
                            point -= 1

                            # reinitialisation du x
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

                            # reinitialisation du y
                            y_para = -100

                            # si le joueur en tue pas beaucoup le jeu devient plus simple
                            vitesse -= 1


            #pareil avec la bombe et le parachutiste doré sauf que la bombe fait perdre 2 secondes et le parachutiste doré en fait gagner 2
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
                    paradore_can_spawn = False


        #affichage de soldat en tank en fond pour rendre le jeu plus beau
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


        #une chance sur 500 que le tank explose
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


        ## si le jeu devient trop simple, la vitesse peut etre negative donc au cas ou
        if vitesse == 0:
            vitesse = 1

        #desaparition du tank si il a explosé
        if tankexplode:
            screen.blit(tank, (-1000, -1000))
        else:
            screen.blit(tank, (x_tank, width / 2.373626374))


        #animation de l'explosion
        anim_explo.draw(screen)
        anim_explo.update(0.30)
        pyg.display.flip()
        pyg.display.update()

        #reaffichage du fond
        screen.blit(background, (0, 0))
        #actualisation du y du parachutiste
        screen.blit(para, (x_para, y_para))


        #affichage du score comme le timer
        font = pyg.font.Font('freesansbold.ttf', 64)
        text = font.render(str(point), True, darkgreen, black)
        screen.blit(text, (height / 1.1, width / 60))
        screen.blit(degrade, (place_selected, width - 400))


        #fin du jeu
        if seconds <= 0:
            end = True
        if end:
            #si mode de jeu ou on joue juste les minis jeu, ecran de victoire, sinon on passe au jeu suivant, si victoire, si defaite, ecran de defaite dans tous les cas
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
                    trans_screen_mouse()
                    jeu_max()

                else:
                    musique_jeu.stop()
                    loose()


        #apparition de la bombe avec une chance sur 300
        luck_bombe = randint(1, 300)
        if luck_bombe == 1:
            bomb_can_explode = True

        if bomb_can_explode:
            #affichage de la bombe
            screen.blit(bombe, (x_bomb + 25, y_bomb))
            y_bomb += vitesse * acceleration


        # apparition du parachutiste doré avec une chance sur 600
        luck_paradore = randint(1, 600)
        if luck_paradore == 1:
            paradore_can_spawn = True

        if paradore_can_spawn:
            # affichage du parachutiste doré
            y_paradore += vitesse * acceleration
            screen.blit(paradore, (x_paradore, y_paradore))

        clock.tick(60)
