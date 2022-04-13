def jeu_ell():
    import pygame as pyg
    from random import randint
    from jeu_1 import height, width, loose, win
    from menu import base_menu
    import menu

    # Intialisation de pygame
    pyg.init()

    pyg.display.set_caption("In the Aeroplane Over the Sea")
    screen = pyg.display.set_mode((height, width))
    background = pyg.image.load("img_elliott/elliottbg.jpg")
    background = pyg.transform.scale(background, (height, width))
    fond = background.convert()
    screen.blit(fond, (0, 0))
    pyg.display.flip()

    # VARIABLES
    a = [0, 0]  # Tableau d'angle
    p = [0, 0]  # Tableau de positions des anneaux
    xmov = 10
    xmov2 = 5
    ymov = 4
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Definition du joueur
    Player = pyg.image.load("img_elliott/avion.png")
    Player = pyg.transform.scale(Player, (150, 150)).convert_alpha()
    Player_norm = Player
    Player_down = pyg.image.load("img_elliott/avion_down.png")
    Player_down = pyg.transform.scale(Player_down, (80, 80)).convert_alpha()
    Player_up = pyg.image.load("img_elliott/avion_up.png")
    Player_up = pyg.transform.scale(Player_up, (80, 80)).convert_alpha()
    x_Player = width // 2
    y_Player = height // 5
    Player_rect = pyg.Surface.get_rect(Player, width=85, height=30, topleft=(x_Player + 28, y_Player + 60))

    # Définition anneau
    Ring = pyg.image.load("img_elliott/ring.png")
    Ring = pyg.transform.scale(Ring, (80, 100)).convert_alpha()
    x_Ring, y_Ring = 1 / 4 * width + 100, 250
    Ring_rect = pyg.Surface.get_rect(Ring, width=50, height=75, topleft=(x_Ring + 15, y_Ring + 15))

    start_ticks = pyg.time.get_ticks()
    point = 0

    music = pyg.mixer.Sound('son/synthware.mp3')
    music.set_volume(0.02)
    music.play()
    running = True

    while running:

        for event in pyg.event.get():
            # Fermeture de fenêtre
            if event.type == pyg.QUIT:
                running = False
                pyg.quit()

            # Apparition du joueur
            screen.blit(Player, (x_Player, y_Player))
            screen.blit(Ring, (x_Ring, y_Ring))

            # Déplacement joueur
            pyg.key.set_repeat(10)  # Maintenir une touche appuyée revient à appuyer plusieurs fois sur cette touche
            if event.type == pyg.KEYDOWN:

                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        pyg.key.set_repeat(1)
                        music.stop()
                        base_menu()


                # Droite
                if (pyg.key.get_pressed()[pyg.K_RIGHT]) or (pyg.key.get_pressed()[pyg.K_d]):
                    # Incrémentation de la coordonnée voulue
                    x_Player += xmov
                    # Création d'une nouvelle case dans le tableau avec l'angle de l'avion
                    a[1] = 0

                # Gauche
                if (pyg.key.get_pressed()[pyg.K_LEFT]) or (pyg.key.get_pressed()[pyg.K_q]):
                    x_Player -= xmov
                    a[1] = 0

                # Diagonale haut-droite
                if ((pyg.key.get_pressed()[pyg.K_UP]) or (pyg.key.get_pressed()[pyg.K_z])) and (
                        (pyg.key.get_pressed()[pyg.K_RIGHT]) or (pyg.key.get_pressed()[pyg.K_d])):
                    x_Player += xmov2
                    y_Player -= ymov
                    a[1] = 1

                # Diagonale haut-gauche
                if ((pyg.key.get_pressed()[pyg.K_UP]) or (pyg.key.get_pressed()[pyg.K_z])) and (
                        (pyg.key.get_pressed()[pyg.K_LEFT]) or (pyg.key.get_pressed()[pyg.K_q])):
                    x_Player -= xmov2
                    y_Player -= ymov
                    a[1] = 1

                # Diagonale bas-droite
                if ((pyg.key.get_pressed()[pyg.K_DOWN]) or (pyg.key.get_pressed()[pyg.K_s])) and (
                        (pyg.key.get_pressed()[pyg.K_RIGHT]) or (pyg.key.get_pressed()[pyg.K_d])):
                    x_Player += xmov2
                    y_Player += ymov
                    a[1] = -1

                # Diagonale bas-gauche
                if ((pyg.key.get_pressed()[pyg.K_DOWN]) or (pyg.key.get_pressed()[pyg.K_s])) and (
                        (pyg.key.get_pressed()[pyg.K_LEFT]) or (pyg.key.get_pressed()[pyg.K_q])):
                    x_Player -= xmov2
                    y_Player += ymov
                    a[1] = 1

                if a[1] == 0:
                    Player_rect = pyg.Surface.get_rect(Player, width=85, height=30,
                                                       topleft=(x_Player + 28, y_Player + 60))
                elif a[1] > 0:
                    Player_rect = pyg.Surface.get_rect(Player, width=55, height=45,
                                                       topleft=(x_Player + 20, y_Player + 5))
                elif a[1] < 0:
                    Player_rect = pyg.Surface.get_rect(Player, width=55, height=40,
                                                       topleft=(x_Player + 15, y_Player + 30))


                # Changement de l'angle de l'avion selon s'il monte ou descend
                if a[0] == 0:
                    if a[1] > 0:
                        Player = Player_up
                    elif a[1] < 0:
                        Player = Player_down
                elif a[0] < 0:
                    if a[1] == 0:
                        Player = Player_norm
                    elif a[1] > 0:
                        Player = Player_up
                elif a[0] > 0:
                    if a[1] == 0:
                        Player = Player_norm
                    elif a[1] < 0:
                        Player = Player_down

                # On regarde s'il y a collision entre l'avion et l'anneau
                collide = pyg.Rect.colliderect(Player_rect, Ring_rect)
                if collide:
                    point += 1
                    p[0] = p[1]
                    while p[1] == p[0]:
                        p[1] = randint(1, 12)
                    if p[1] >= 1 and p[1] <= 4:
                        y_Ring = 250
                    elif p[1] >= 5 and p[1] <= 8:
                        p[1] -= 4
                        y_Ring = 500
                    else:
                        p[1] -= 8
                        y_Ring = 750
                    if p[1] == 1:
                        x_Ring = 1 / 4 * width + 100
                    elif p[1] == 2:
                        x_Ring = 1 / 2 * width + 250
                    elif p[1] == 3:
                        x_Ring = width + 100
                    else:
                        x_Ring = 5 / 4 * width + 100
                    Ring_rect = pyg.Surface.get_rect(Ring, width=50, height=75, topleft=(x_Ring + 15, y_Ring + 15))

                # L'angle actuel devient l'angle précédent de la prochaine boucle
                a[0] = a[1]


                # Joueur téléporté s'il dépasse les bordures de l'écran
                if not ((x_Player >= -(width // 5)) and (x_Player <= width * 1.8) and (
                        y_Player >= -(height // 10)) and (y_Player <= height // 2)):
                    x_Player, y_Player = 400, 200
                    a = [0, 0]

            seconds = round(30 - ((pyg.time.get_ticks() - start_ticks) / 1000))
            if seconds <= 0:
                pyg.key.set_repeat(1)
                if point >= 20:
                    if menu.gamemode == 1:
                        music.stop()
                        win()
                    else:
                        music.stop()
                        win()
                else:
                    music.stop()
                    loose()

            font = pyg.font.Font('freesansbold.ttf', 64)
            countdown = font.render(str(seconds), True, white, black)
            screen.blit(countdown, (200, height / 60))
            score = font.render(str(point), True, white, black)
            screen.blit(score, (1000, height / 60))
            pyg.display.flip()
            pyg.display.update()

            # Réaffiche l'écran
            screen.blit(fond, (0, 0))
