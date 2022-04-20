import pygame
from random import randint
import menu

pygame.init()
pygame.time.Clock()
pygame.font.init()

def jeu_max():
    from jeu_1 import win, loose, amongus, height, width
    from jeu_thomas import jeu_tomaye
    from transition import trans_screen_keyboard
    from menu import base_menu

########################################################################################################################

    # Durant tous le programe "tank" définis le gros bateau, "Soldat" et "Soldat2" définissent un des petits bateau

########################################################################################################################
    
    pygame.mouse.set_visible(0) # Le curseur de la souris devient invisible

########################################################################################################################

    # Couleurs de l'affichage du score et du timer
    noir = (0, 0, 0) # fond
    blanc = (200, 200, 200) # ecriture

########################################################################################################################

    Point = 0 # points pour savoir si nous gagnons / perdons le jeu

    # Definition du fond de jeu
    screen = pygame.display.set_mode((height, width))
    background = pygame.image.load("img_max\Fond_Max.jpg") # Charge l'image
    background = pygame.transform.scale(background, (height, width)) # Taille de l'image
    fond = background.convert()
    screen.blit(fond, (0, 0)) # actualise le fond
    pygame.display.flip()

    # Definition du Viseur
    Viseur = pygame.image.load("img_max\Viseur.PNG") # Charge l'image

    Viseur = pygame.transform.scale(Viseur, (50, 50)).convert_alpha() # Taille de l'image

    x_Viseur = height // 2 # coordonnee x de l'image
    y_Viseur = width // 2 # coordonnee y de l'image

    # Definition de l' Ult
    Ulte = pygame.image.load("img_max\Bouton u.png") # Charge l'image

    Ulte = pygame.transform.scale(Ulte, (200, 150)).convert_alpha() # Taille de l'image

    x_Ulte = height - 250 # coordonnee x de l'image
    y_Ulte = width - 200 # coordonnee y de l'image

    class explo(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.sprites = []
            self.is_animating = False
            vide = pygame.image.load('img_max/transpar.png')
            explo1 = pygame.image.load('img_max/explosion-frame-1.png')
            explo1 = pygame.transform.scale(explo1, (x_explo - 5, y_explo - 5)) # Taille de l'image de la frame 1
            explo2 = pygame.image.load('img_max/explosion-frame-2.png')
            explo2 = pygame.transform.scale(explo2, (x_explo, y_explo)) # Taille de l'image de la frame 2
            explo3 = pygame.image.load('img_max/explosion-frame-3.png')
            explo3 = pygame.transform.scale(explo3, (x_explo, y_explo)) # Taille de l'image de la frame 3
            explo4 = pygame.image.load('img_max/explosion-frame-4.png')
            explo4 = pygame.transform.scale(explo4, (x_explo, y_explo)) # Taille de l'image de la frame 4
            explo5 = pygame.image.load('img_max/explosion-frame-5.png')
            explo5 = pygame.transform.scale(explo5, (x_explo, y_explo)) # Taille de l'image de la frame 5
            explo6 = pygame.image.load('img_max/explosion-frame-6.png')
            explo6 = pygame.transform.scale(explo6, (x_explo, y_explo)) # Taille de l'image de la frame 6
            explo7 = pygame.image.load('img_max/explosion-frame-7.png')
            explo7 = pygame.transform.scale(explo7, (x_explo, y_explo)) # Taille de l'image de la frame 7
            explo8 = pygame.image.load('img_max/explosion-frame-8.png')
            explo8 = pygame.transform.scale(explo8, (x_explo, y_explo)) # Taille de l'image de la frame 8
            self.sprites.append(vide) # Cre la liste des images de l'animation
            self.sprites.append(explo1) # ajoute l'image 1 a la liste
            self.sprites.append(explo2) # ajoute l'image 2 a la liste
            self.sprites.append(explo3) # ajoute l'image 3 a la liste
            self.sprites.append(explo4) # ajoute l'image 4 a la liste
            self.sprites.append(explo5) # ajoute l'image 5 a la liste
            self.sprites.append(explo6) # ajoute l'image 6 a la liste
            self.sprites.append(explo7) # ajoute l'image 7 a la liste
            self.sprites.append(explo8) # ajoute l'image 8 a la liste
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
    Soldat = pygame.image.load("img_max\Soldat.PNG") # Charge l'image

    height_Soldat = height // 25  # taille en x de l'image
    width_Soldat = width // 40  # taille en y de l'image

    Soldat = pygame.transform.scale(Soldat, (height_Soldat, width_Soldat)).convert_alpha() # Taille de l'image

    y_Soldat = width // 3  # coordonnee x de l'image
    x_Soldat = -100  # coordonnee y de l'image

    # Definition du soldat2
    pygame.image.load("img_max\Soldat.PNG") # Charge l'image

    height_Soldat2 = height // 25  # taille en x de l'image
    width_Soldat2 = width // 40  # taille en y de l'image

    Soldat2 = pygame.transform.scale(Soldat, (height_Soldat2, width_Soldat2)).convert_alpha() # Taille de l'image

    y_Soldat2 = width * 2 // 3  # coordonnee x de l'image
    x_Soldat2 = -100  # coordonnee y de l'image

    # Definition du Tank
    Tank = pygame.image.load("img_max\Tank.PNG") # Charge l'image

    height_Tank = height // 15 # taille en x de l'image
    width_Tank = width // 15 # taille en y de l'image

    Tank = pygame.transform.scale(Tank, (height_Tank, width_Tank)).convert_alpha() # Taille de l'image

    y_Tank = width // 2  # coordonnee x de l'image
    x_Tank = -100  # coordonnee y de l'image

    son_explo = pygame.mixer.Sound('son/son_explo.wav') # son de l'explosion
    son_explo.set_volume(0.02) # définis le volume auquel on entend le son

########################################################################################################################

    x_explo = 100 # coordonne x de l'explosion
    y_explo = 100 # coordonne y de l'explosion
    
    
    anim_explo = pygame.sprite.Group()
    explosion = explo(x_Soldat, y_Soldat)
    anim_explo.add(explosion)

########################################################################################################################

    start_ticks = pygame.time.get_ticks()
    JeuLance = True # Le jeu est lance
    Ult = True # L'ult est disponoble
    x_MouseAncien = pygame.mouse.get_pos(0) # Variable pour plus tard
    y_MouseAncien = pygame.mouse.get_pos(1) # Variable pour plus tard

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
                if event.key == pygame.K_w: # Ester egg
                    amongus()
                if event.key == pygame.K_ESCAPE: # retour au menu
                    musique_jeu.stop()
                    menu.base_menu()
                if event.key == pygame.K_u: # Déclenchement de l'ult
                    if Ult:
                        x_explo = 800 # Définis la taille de l'explosion                                   Shéma type systématique à toutes les explosions
                        y_explo = 800 # Dfinis la taille de l'explosion
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(height // 8, width // 8) # coordonnées de l'explosion
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35) # temps entre les frames
                        x_explo = 100 # rednis la taille de l'explosion
                        y_explo = 100 # rednis la taille de l'explosion

                        Ult = False # l'ult est désormais indisponible

                        y_Soldat = width // 3 # remet les unités au début
                        x_Soldat = -20
                        y_Soldat2 = width * 2 // 3
                        x_Soldat2 = -200
                        y_Tank = width // 2
                        x_Tank = -200
                        Point += 3

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT: # definis la droite pour un jeu au clavier
                    x_Viseur += height // 100

                if event.key == pygame.K_q or event.key == pygame.K_LEFT: # definis la gauche pour un jeu au clavier
                    x_Viseur -= height // 100

                if event.key == pygame.K_z or event.key == pygame.K_UP: # definis le haut pour un jeu au clavier
                    y_Viseur -= width // 70

                if event.key == pygame.K_s or event.key == pygame.K_DOWN: # definis le bas pour un jeu au clavier
                    y_Viseur += width // 70

########################################################################################################################
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        base_menu()

                # Definis l'espace
                if event.key == pygame.K_SPACE:
                    if x_Viseur + 25 >= x_Soldat and x_Viseur + 25 <= x_Soldat + height_Soldat and y_Viseur + 25 >= y_Soldat and y_Viseur + 25 <= y_Soldat + width_Soldat: # test si les coordonnees du viseur sont sur celle du soldat
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(x_Soldat, y_Soldat)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        x_Soldat = - 20
                        y_Soldat = randint(100, width - 200)
                        Point += 2
                    elif x_Viseur + 25 >= x_Tank and x_Viseur + 25 <= x_Tank + height_Tank and y_Tank <= y_Viseur + 25 <= y_Tank + width_Tank:# test si les coordonnees du viseur sont sur celle du tank
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(x_Tank, y_Tank)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        x_Tank = - 20
                        y_Tank = randint(100, width - 200)
                        Point += 2
                    elif x_Viseur + 25 >= x_Soldat2 and x_Viseur + 25 <= x_Soldat2 + height_Soldat2 and y_Viseur + 25 >= y_Soldat2 and y_Viseur + 25 <= y_Soldat2 + width_Soldat2: # test si les coordonnees du viseur sont sur celle du soldat2
                        anim_explo = pygame.sprite.Group()  # animation d'explosion
                        explosion = explo(x_Soldat2, y_Soldat2)
                        anim_explo.add(explosion)
                        explosion.animate()
                        anim_explo.draw(screen)
                        anim_explo.update(0.35)
                        x_Soldat2 = - 20
                        y_Soldat2 = randint(100, width - 200)
                        Point += 2
                    elif x_Viseur + 25 >= x_Ulte and x_Viseur + 25 <= x_Ulte + 200 and y_Ulte + 25 >= y_Ulte and y_Ulte + 25 <= y_Ulte + 150:# test si les coordonnees du viseur sont sur celle de l'ult
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
                    if x_Viseur + 25 >= x_Soldat and x_Viseur + 25 <= x_Soldat + height_Soldat and y_Viseur + 25 >= y_Soldat and y_Viseur + 25 <= y_Soldat + width_Soldat: # test si les coordonnees du viseur sont sur celle du soldat
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
                    elif x_Viseur + 25 >= x_Tank and x_Viseur + 25 <= x_Tank + height_Tank and y_Viseur + 25 >= y_Tank and y_Viseur + 25 <= y_Tank + width_Tank: # test si les coordonnees du viseur sont sur celle du soldat2
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
                    elif x_Viseur + 25 >= x_Soldat2 and x_Viseur + 25 <= x_Soldat2 + height_Soldat2 and y_Viseur + 25 >= y_Soldat2 and y_Viseur + 25 <= y_Soldat2 + width_Soldat2: # test si les coordonnees du viseur sont sur celle du Tank
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
        if x_Soldat >= height // 2.4: # test de si le soldat depasse la berge
            x_explo = 500
            y_explo = 500
            anim_explo = pygame.sprite.Group()  # animation d'explosion sur la base
            explosion = explo((height * 3 // 5), width // 4)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            x_explo = 100
            y_explo = 100
            
            nim_explo = pygame.sprite.Group()  # animation d'explosion sur le bateau
            explosion = explo(x_Soldat, y_Soldat)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            Point -= 3

            x_Soldat = - 20
            y_Soldat = randint(200, width - 200)

        if x_Soldat2 >= height // 2.4: # test de si le soldat2 depasse la berge
            x_explo = 500
            y_explo = 500
            anim_explo = pygame.sprite.Group()  # animation d'explosion sur la base
            explosion = explo((height * 3 // 5), width // 4)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            x_explo = 100
            y_explo = 100
            
            nim_explo = pygame.sprite.Group()  # animation d'explosion sur le bateau
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
        if x_Tank >= height // 2.4: # test de si le tank depasse la berge
            x_explo = 500
            y_explo = 500
            anim_explo = pygame.sprite.Group()  # animation d'explosion sur la base
            explosion = explo((height * 3 // 5), width // 4)
            anim_explo.add(explosion)
            explosion.animate()
            anim_explo.draw(screen)
            anim_explo.update(0.35)
            x_explo = 100
            y_explo = 100
            
            nim_explo = pygame.sprite.Group()  # animation d'explosion sur le bateau
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
        
        screen.blit(Viseur, (x_Viseur, y_Viseur)) # Apparition du Viseur
        
        anim_explo.draw(screen)
        anim_explo.update(0.35)
        
        pygame.display.update()
        pygame.display.flip()

        screen.blit(fond, (0, 0)) # Reaffiche l'écran

        # affichage des Points
        font = pygame.font.Font('freesansbold.ttf', 64)
        text = font.render(str(Point), True, noir, blanc)
        screen.blit(text, (height // 1.1, width // 60))

########################################################################################################################

        # Fin du jeu
        if seconds < 0: # Test si le temps de jeu est écoulé
            if menu.gamemode == 1: # Test si le mode de jeu est en test
                if Point >= 30: # test si les points sont suffisant pour que la partie soit gagnée
                    win() # victoire
                else:
                    loose() # defaite
            else: # si le mode de jeu est en survie
                if Point < 30: # test si les points sont suffisant pour que la partie soit gagnée
                    loose() # defaite
                else:
                    trans_screen_keyboard() # lancement de l'écrant de transition
                    jeu_tomaye() # lancement du jeu suivant (3)

 ########################################################################################################################
