import pygame
from random import randint
import menu
from sys import exit

pygame.init()
pygame.time.Clock()
pygame.font.init()
def jeu_max():
    from jeu_1 import win, loose, amongus
    from jeu_thomas import jeu_tomaye
    from transition import trans_screen

    x_Mouse = 0
    0

    pygame.mouse.set_visible(0)

    # #######################################################################################################################

    # Point
    noir = (0, 0, 0)
    blanc = (200, 200, 200)

    ########################################################################################################################

    Point = 0

    # Definis fond du jeu
    # height = GetSystemMetrics(0)
    # width = GetSystemMetrics(1)
    height = 1920
    width = 1080
    screen = pygame.display.set_mode((height, width))

    background = pygame.image.load("img_max\Fond_Max.jpg")
    background = pygame.transform.scale(background, (height, width))
    fond = background.convert()
    screen.blit(fond, (0, 0))
    pygame.display.flip()

    # Definition du Viseur
    Viseur = pygame.image.load("img_max\Viseur.PNG")

    Viseur = pygame.transform.scale(Viseur, (50, 50)).convert_alpha()

    x_Viseur = height // 2
    y_Viseur = width // 2

    0

    # Definition de l' Ult
    Ulte = pygame.image.load("img_max\Bouton u.png")

    Ulte = pygame.transform.scale(Ulte, (200, 150)).convert_alpha()

    x_Ulte = height - 250
    y_Ulte = width - 200

    r_Ulte = 0

    class explo(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.sprites = []
            self.is_animating = False
            vide = pygame.image.load('img_max/transpar.png')
            explo1 = pygame.image.load('img_max/explosion-frame-1.png')
            explo1 = pygame.transform.scale(explo1, (x_explo - 5, y_explo - 5))
            explo2 = pygame.image.load('img_max/explosion-frame-2.png')
            explo2 = pygame.transform.scale(explo2, (x_explo, y_explo))
            explo3 = pygame.image.load('img_max/explosion-frame-3.png')
            explo3 = pygame.transform.scale(explo3, (x_explo, y_explo))
            explo4 = pygame.image.load('img_max/explosion-frame-4.png')
            explo4 = pygame.transform.scale(explo4, (x_explo, y_explo))
            explo5 = pygame.image.load('img_max/explosion-frame-5.png')
            explo5 = pygame.transform.scale(explo5, (x_explo, y_explo))
            explo6 = pygame.image.load('img_max/explosion-frame-6.png')
            explo6 = pygame.transform.scale(explo6, (x_explo, y_explo))
            explo7 = pygame.image.load('img_max/explosion-frame-7.png')
            explo7 = pygame.transform.scale(explo7, (x_explo, y_explo))
            explo8 = pygame.image.load('img_max/explosion-frame-8.png')
            explo8 = pygame.transform.scale(explo8, (x_explo, y_explo))
            self.sprites.append(vide)
            self.sprites.append(explo1)
            self.sprites.append(explo2)
            self.sprites.append(explo3)
            self.sprites.append(explo4)
            self.sprites.append(explo5)
            self.sprites.append(explo6)
            self.sprites.append(explo7)
            self.sprites.append(explo8)
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]

            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]

        def animate(self):
            self.is_animating = True

        def update(self, vitesse):
            if self.is_animating:
                self.current_sprite += vitesse

                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                    self.is_animating = False

                self.image = self.sprites[int(self.current_sprite)]

    # Definition du soldat
    Soldat = pygame.image.load("img_max\Soldat.PNG")

    height_Soldat = height // 25
    width_Soldat = width // 40

    Soldat = pygame.transform.scale(Soldat, (height_Soldat, width_Soldat)).convert_alpha()

    y_Soldat = width // 3
    x_Soldat = -100

    r_Soldat = 0

    # Definition du soldat2
    pygame.image.load("img_max\Soldat.PNG")

    height_Soldat2 = height // 25
    width_Soldat2 = width // 40

    Soldat2 = pygame.transform.scale(Soldat, (height_Soldat2, width_Soldat2)).convert_alpha()

    y_Soldat2 = width * 2 // 3
    x_Soldat2 = -100

    r_Soldat2 = 0

    # Definition du Tank
    Tank = pygame.image.load("img_max\Tank.PNG")

    height_Tank = height // 15
    width_Tank = width // 15

    Tank = pygame.transform.scale(Tank, (height_Tank, width_Tank)).convert_alpha()

    y_Tank = width // 2
    x_Tank = -100

    r_Tank = 0

    son_explo = pygame.mixer.Sound('son/son_explo.wav')
    son_explo.set_volume(0.02)

    ########################################################################################################################

    # Definition de victoire / défaite

    ########################################################################################################################

    x_explo = 100
    y_explo = 100

    anim_explo = pygame.sprite.Group()
    explosion = explo(x_Soldat, y_Soldat)
    anim_explo.add(explosion)

    ########################################################################################################################

    start_ticks = pygame.time.get_ticks()
    JeuLance = True
    Ult = True
    x_MouseAncien = pygame.mouse.get_pos(0)
    y_MouseAncien = pygame.mouse.get_pos(1)

    musique_jeu = pygame.mixer.Sound('son/synthware.mp3')
    musique_jeu.set_volume(0.02)
    musique_jeu.play()

    while JeuLance:
        for event in pygame.event.get():

            # Definis la croix pour fermer l'appli
            if event.type == pygame.QUIT:
                pygame.quit()

            # Deplacement du Viseur par les touches
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    amongus()
                if event.key == pygame.K_ESCAPE:
                    musique_jeu.stop()
                    menu.base_menu()
                if event.key == pygame.K_u:
                    if Ult:
                        x_explo = 800
                        y_explo = 800
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(height // 8, width // 8)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        x_explo = 100
                        y_explo = 100

                        Ult = False

                        y_Soldat = width // 3
                        x_Soldat = -100
                        y_Soldat2 = width * 2 // 3
                        x_Soldat2 = -100
                        y_Tank = width // 2
                        x_Tank = -100
                        Point += 10

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_Viseur += height // 100

                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    x_Viseur -= height // 100

                if event.key == pygame.K_z or event.key == pygame.K_UP:
                    y_Viseur -= width // 70

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    y_Viseur += width // 70

                ########################################################################################################################

                # Disparition des unités si touche espace apuyée dessus

                # Definis l'espace
                if event.key == pygame.K_SPACE:
                    if x_Viseur + 25 >= x_Soldat and x_Viseur + 25 <= x_Soldat + height_Soldat and y_Viseur + 25 >= y_Soldat and y_Viseur + 25 <= y_Soldat + width_Soldat:
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(x_Soldat, y_Soldat)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        x_Soldat = - 20
                        y_Soldat = randint(100, width - 200)
                        Point += 2
                    elif x_Viseur + 25 >= x_Tank and x_Viseur + 25 <= x_Tank + height_Tank and y_Tank <= y_Viseur + 25 <= y_Tank + width_Tank:
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(x_Tank, y_Tank)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        x_Tank = - 20
                        y_Tank = randint(100, width - 200)
                        Point += 2
                    elif x_Viseur + 25 >= x_Soldat2 and x_Viseur + 25 <= x_Soldat2 + height_Soldat2 and y_Viseur + 25 >= y_Soldat2 and y_Viseur + 25 <= y_Soldat2 + width_Soldat2:
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(x_Soldat2, y_Soldat2)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        x_Soldat2 = - 20
                        y_Soldat2 = randint(100, width - 200)
                        Point += 2
                    elif x_Viseur + 25 >= x_Ulte and x_Viseur + 25 <= x_Ulte + 200 and y_Ulte + 25 >= y_Ulte and y_Ulte + 25 <= y_Ulte + 150:
                        if Ult:
                            x_explo = 800
                            y_explo = 800
                            anim_explo = pygame.sprite.Group()  # animation d'explosion
                            explosion = explo(height // 8, width // 8)
                            anim_explo.add(explosion)
                            explosion.animate()
                            anim_explo.draw(screen)
                            anim_explo.update(0.35)
                            x_explo = 100
                            y_explo = 100

                            Ult = False

                            y_Soldat = width // 3
                            x_Soldat = -100
                            y_Soldat2 = width * 2 // 3
                            x_Soldat2 = -100
                            y_Tank = width // 2
                            x_Tank = -100
                            Point += 10

                        else:
                            Point -= 1

            # Definis le clic gauche
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if x_Viseur + 25 >= x_Soldat and x_Viseur + 25 <= x_Soldat + height_Soldat and y_Viseur + 25 >= y_Soldat and y_Viseur + 25 <= y_Soldat + width_Soldat:
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(x_Soldat, y_Soldat)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        son_explo.play()
                        x_Soldat = - 20
                        y_Soldat = randint(100, width - 200)
                        Point += 2
                    elif x_Viseur + 25 >= x_Tank and x_Viseur + 25 <= x_Tank + height_Tank and y_Viseur + 25 >= y_Tank and y_Viseur + 25 <= y_Tank + width_Tank:
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(x_Tank, y_Tank)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        son_explo.play()
                        x_Tank = - 20
                        y_Tank = randint(100, width - 200)
                        Point += 2
                    elif x_Viseur + 25 >= x_Soldat2 and x_Viseur + 25 <= x_Soldat2 + height_Soldat2 and y_Viseur + 25 >= y_Soldat2 and y_Viseur + 25 <= y_Soldat2 + width_Soldat2:
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(x_Soldat2, y_Soldat2)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        son_explo.play()
                        x_Soldat2 = - 20
                        y_Soldat2 = randint(100, width - 200)
                        Point += 2
                    elif x_Viseur + 25 >= x_Ulte and x_Viseur + 25 <= x_Ulte + 200 and y_Ulte + 25 >= y_Ulte and y_Ulte + 25 <= y_Ulte + 150:
                        if Ult:
                            x_explo = 800
                            y_explo = 800
                            anim_explo = pygame.sprite.Group()  # animation d'explosion
                            explosion = explo(height // 8, width // 8)
                            anim_explo.add(explosion)
                            explosion.animate()
                            anim_explo.draw(screen)
                            son_explo.set_volume(0.2)
                            son_explo.play()
                            anim_explo.update(0.35)
                            x_explo = 100
                            y_explo = 100

                            Ult = False

                            y_Soldat = width // 3
                            x_Soldat = -100
                            y_Soldat2 = width * 2 // 3
                            x_Soldat2 = -100
                            y_Tank = width // 2
                            x_Tank = -100
                            Point += 10
                    else:
                        Point -= 1

        # Définis le timer
        seconds = round(30 - ((pygame.time.get_ticks() - start_ticks) / 1000))
        font = pygame.font.Font('freesansbold.ttf', 64)
        countdown = font.render(str(seconds), True, blanc, noir)
        screen.blit(countdown, (200, width / 60))
        son_explo.set_volume(0.02)

        # Definis les variables de la position de la souris
        x_Mouse = pygame.mouse.get_pos(0)
        y_Mouse = pygame.mouse.get_pos(1)

        # Deplacement du viseur par la souris
        if x_Mouse != x_MouseAncien and y_Mouse != y_MouseAncien:
            x_Viseur = x_Mouse[0]
            y_Viseur = y_Mouse[1]

        screen.blit(Viseur, (x_Viseur, y_Viseur))


        x_MouseAncien = x_Mouse
        y_MouseAncien = y_Mouse

        ########################################################################################################################

        # Apparition des Soldats
        screen.blit(Soldat, (x_Soldat, y_Soldat))
        screen.blit(Soldat2, (x_Soldat2, y_Soldat2))

        # Deplacement des Soldats
        x_Soldat += 3
        x_Soldat2 += 3

        # Retour des Soldats au depart
        if x_Soldat >= height // 2.4:
            x_explo = 500
            y_explo = 500
            anim_explo = pygame.sprite.Group()  # animation d'explosion
            explosion = explo((height * 3 // 5), width // 4)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            x_explo = 100
            y_explo = 100
            nim_explo = pygame.sprite.Group()  # animation d'explosion
            explosion = explo(x_Soldat, y_Soldat)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            Point -= 3

            x_Soldat = - 20
            y_Soldat = randint(200, width - 200)

        if x_Soldat2 >= height // 2.4:
            x_explo = 500
            y_explo = 500
            anim_explo = pygame.sprite.Group()  # animation d'explosion
            explosion = explo((height * 3 // 5), width // 4)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            x_explo = 100
            y_explo = 100
            nim_explo = pygame.sprite.Group()  # animation d'explosion
            explosion = explo(x_Soldat2, y_Soldat2)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            Point -= 3

            x_Soldat2 = - 20
            y_Soldat2 = randint(200, width - 200)

        # Apparition du Tank
        screen.blit(Tank, (x_Tank, y_Tank))

        # Deplacement du Tank
        x_Tank += 4.5

        # Retour du Tank au depart
        if x_Tank >= height // 2.4:
            x_explo = 500
            y_explo = 500
            anim_explo = pygame.sprite.Group()  # animation d'explosion
            explosion = explo((height * 3 // 5), width // 4)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            x_explo = 100
            y_explo = 100
            nim_explo = pygame.sprite.Group()  # animation d'explosion
            explosion = explo(x_Tank, y_Tank)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            Point -= 5

            x_Tank = - 20
            y_Tank = randint(100, width - 200)

        # Apparition de l' Ult
        if Ult:
            screen.blit(Ulte, (x_Ulte, y_Ulte))
        # Apparition du Viseur
        screen.blit(Viseur, (x_Viseur, y_Viseur))
        anim_explo.draw(screen)
        anim_explo.update(0.35)
        pygame.display.update()
        pygame.display.flip()
        # Reaffiche l'écran
        screen.blit(fond, (0, 0))

        # affichage du Point
        font = pygame.font.Font('freesansbold.ttf', 64)
        text = font.render(str(Point), True, noir, blanc)
        screen.blit(text, (height // 1.1, width // 60))

        ########################################################################################################################

        # Fin du jeu
        if seconds < 0:
            if menu.gamemode == 1:
                if Point >= 30:
                    win()
                else:
                    loose()
            else:
                if Point < 30:
                    loose()
                else:
                    trans_screen()
                    jeu_tomaye()

    ########################################################################################################################
