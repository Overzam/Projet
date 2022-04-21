def jeu_ell():
    import pygame as pyg
    from random import randint
    from jeu_1 import height, width, loose, win, explo
    from menu import base_menu
    import menu

    # Intialisation de pygame
    pyg.init()

    #initialisation de la clock
    clock = pyg.time.Clock()

    # Affichage de l'écran
    pyg.display.set_caption("In the Aeroplane Over the Sea")
    screen = pyg.display.set_mode((height, width))
    background = pyg.image.load("img_elliott/elliottbg.jpg")
    background = pyg.transform.scale(background, (height, width))
    fond = background.convert()
    screen.blit(fond, (0, 0))
    pyg.display.flip()

    # On créé un rectangle de la taille de l'écran
    screen_rect = pyg.Surface.get_rect(screen)
    safezone_rect = pyg.Rect.copy(screen_rect)

    # Variables
    angle = [0, 0]  # Tableau d'angles
    position = [1, 1, 1]  # Tableau de positions des anneaux
    xmov, ymov = 10, 4  # Variables des distances x et y parcourues par le joueur en un input
    offset1, offset2, offset3 = 15, 25, 30  # Variables de décalages qui permettront l'ajustement des dimensions des hitboxs
    shrink_height = screen_rect.height // 8  # Avancement/décalage de la zone rouge en hauteur
    shrink_width = screen_rect.width // 10  # """ en largeur
    niveau_de_danger = 0  # Variable qui dicte l'avancement de la zone rouge
    x_explo, y_explo = 100, 100
    start_ticks = pyg.time.get_ticks()
    point = 0
    # Couleurs
    black = (0, 0, 0)
    white = (255, 255, 255)
    orange = (255, 137, 0)  # La zone rouge est en fait orange mais il s'agit d'un secret d'état

    # Definition du joueur
    player = pyg.image.load("img_elliott/avion2.png")
    player = pyg.transform.scale(player, 
                                 (60 * screen_rect.width // 1080, 40 * screen_rect.height // 1080)).convert_alpha()
    player_norm = player
    # Importation des images de l'avatar selon les angles
    player_up = pyg.image.load("img_elliott/avion2_up.png")
    player_up = pyg.transform.scale(player_up,
                                    (60 * screen_rect.width // 1080, 60 * screen_rect.height // 1080)).convert_alpha()
    player_down = pyg.image.load("img_elliott/avion2_down.png")
    player_down = pyg.transform.scale(player_down,
                                      (60 * screen_rect.width // 1080, 60 * screen_rect.height // 1080)).convert_alpha()
    # Coordonnées du joueur au début de la partie
    x_player, y_player = screen_rect.center
    # Hitbox du joueur, on créé un masque au sprite du joueur et on considère ce masque comme un rectanglequi entoure parfaitement le sprite de l'avatar
    player_rect_norm = pyg.mask.Mask.get_rect(pyg.mask.from_surface(player))
    player_rect_tilt = pyg.mask.Mask.get_rect(pyg.mask.from_surface(player_up))
    player_rect_norm.topleft, player_rect_tilt.topleft = (x_player, y_player), (x_player, y_player)
    # Ajustement de la hitbox pour qu'elle soit contenue à l'intérieur du sprite
    pyg.Rect.inflate_ip(player_rect_norm, -offset1, -offset1)
    pyg.Rect.inflate_ip(player_rect_tilt, -offset2, -offset2)
    # L'avatar commence la partie à l'horizontal
    player_rect = player_rect_norm

    # Définition de l'anneau
    ring = pyg.image.load("img_elliott/ring.png")
    ring = pyg.transform.scale(ring, (80 * screen_rect.width // 1080, 120 * screen_rect.height // 1080)).convert_alpha()
    x_ring, y_ring = screen_rect.width // 5, screen_rect.height // 4
    # Hitbox de l'anneau
    ring_rect = pyg.mask.Mask.get_rect(pyg.mask.from_surface(ring))
    ring_rect.topleft = (x_ring, y_ring)
    pyg.Rect.inflate_ip(ring_rect, -offset3, -offset3)  # On ajuste la hitbox de sorte qu'elle soit moins généreuse

    #definition de lexplo
    anim_explo = pyg.sprite.Group()
    explosion = explo(x_player, width - 300)
    anim_explo.add(explosion)
    # Feu qui ne fait pas ramer le jeu
    feu_haut, feu_bas, feu_gauche, feu_droit = pyg.Rect.copy(screen_rect), pyg.Rect.copy(screen_rect), pyg.Rect.copy(
        screen_rect), pyg.Rect.copy(screen_rect)  # On créé les 4 rectangles de la zone rouge
    # On définit les coordonnées du coin haut-droit et la hauteur et la largeur de chaque rectangle
    feu_haut.size, feu_bas.size = (screen_rect.width, shrink_height / 2), (screen_rect.width, shrink_height)
    feu_haut.topleft, feu_bas.topleft = (0, 0), (0, screen_rect.height - shrink_height / 2)
    feu_gauche.size, feu_droit.size = (shrink_width / 2, screen_rect.height), (shrink_width / 2, screen_rect.height)
    feu_gauche.topleft, feu_droit.topleft = (0, 0), (screen_rect.width - shrink_width / 2, 0)

    """
    LES IMAGES DE FEU FONT RAMER PYGAME
    # Définition du feu
    feu = pyg.image.load("img_thomas/feu.png")
    feu_horizontal = pyg.transform.scale(feu, (screen_rect.width, shrink_height+70))
    feu_vertical = pyg.transform.scale(feu, (screen_rect.height, shrink_width+90))
    feu_bas, feu_haut = feu_horizontal, pyg.transform.flip(feu_horizontal, 0, 1)
    feu_droite, feu_gauche = pyg.transform.rotate(feu_vertical, 90), pyg.transform.rotate(feu_vertical, -90)
    x_feu_h, y_feu_h, x_feu_b, y_feu_b, x_feu_g, y_feu_g, x_feu_d, y_feu_d = -100, -100, -100, -100, -100, -100, -100, -100, 
    """

    # Musique
    music = pyg.mixer.Sound('son/synthware.mp3')
    music.set_volume(0.02)
    music.play()

    # Boucle lançant le jeu
    running = True

    while running:

        # Affichage des sprites à l'écran
        screen.blit(player, (x_player, y_player))
        screen.blit(ring, (x_ring, y_ring))
        # Affichage de la zone rouge à l'aide de 4 rectangles
        if niveau_de_danger > 0:
            pyg.draw.rect(screen, orange, feu_haut)
            pyg.draw.rect(screen, orange, feu_bas)
            pyg.draw.rect(screen, orange, feu_gauche)
            pyg.draw.rect(screen, orange, feu_droit)

        """if niveau_de_danger > 0:
            screen.blit(feu_haut, (x_feu_h, y_feu_h))
            screen.blit(feu_bas, (x_feu_b, y_feu_b))
            screen.blit(feu_gauche, (x_feu_g, y_feu_g))
            screen.blit(feu_droite, (x_feu_d, y_feu_d))"""

        """pyg.draw.rect(screen, white, player_rect, 1, 1)
        pyg.draw.rect(screen, white, ring_rect, 1, 1)
        pyg.draw.rect(screen, white, screen_rect, 5, 5)
        pyg.draw.rect(screen, (255, 0, 0), safezone_rect, 5, 5)
        pyg.draw.line(screen, (255, 0, 0), (screen_rect.topleft[0], screen_rect.height // 4), (screen_rect.width, screen_rect.height // 4))
        pyg.draw.line(screen, (255, 0, 0), (screen_rect.topleft[0], screen_rect.height // 2), (screen_rect.width, screen_rect.height // 2))
        pyg.draw.line(screen, (255, 0, 0), (screen_rect.topleft[0], screen_rect.height * 3 // 4), (screen_rect.width, screen_rect.height * 3 // 4))
        pyg.draw.line(screen, (255, 0, 0), (screen_rect.width//5, screen_rect.topleft[1]), (screen_rect.width//5, screen_rect.bottomleft[1]))
        pyg.draw.line(screen, (255, 0, 0), (2*screen_rect.width//5, screen_rect.topleft[1]), (2*screen_rect.width//5, screen_rect.bottomleft[1]))
        pyg.draw.line(screen, (255, 0, 0), (3*screen_rect.width//5, screen_rect.topleft[1]), (3*screen_rect.width//5, screen_rect.bottomleft[1]))
        pyg.draw.line(screen, (255, 0, 0), (4*screen_rect.width//5, screen_rect.topleft[1]), (4*screen_rect.width//5, screen_rect.bottomleft[1]))"""

        pyg.key.set_repeat(10)  # Un input maintenu se répète, permettant un mouvement fluide
        for event in pyg.event.get():
            # Fermeture de fenêtre
            if event.type == pyg.QUIT:
                running = False
                pyg.quit()
            if event.type == pyg.KEYDOWN:

                # Touche échap renvoie au menu principal
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        pyg.key.set_repeat(1)
                        music.stop()
                        base_menu()

                # Déplacements du joueur

                # Droite
                if (pyg.key.get_pressed()[pyg.K_RIGHT]) or (pyg.key.get_pressed()[pyg.K_d]):
                    # Incrémentation des coordonnées de l'avion avec les coordonnées de déplacement
                    # Assignation de l'angle actuel de l'avion selon son mouvement dans la dernière case du tableau d'angles
                    x_player, angle[1] = (x_player + xmov), 0

                # Gauche
                if (pyg.key.get_pressed()[pyg.K_LEFT]) or (pyg.key.get_pressed()[pyg.K_q]):
                    x_player, angle[1] = (x_player - xmov), 0

                # Diagonale haut-droite
                if ((pyg.key.get_pressed()[pyg.K_UP]) or (pyg.key.get_pressed()[pyg.K_z])) and (
                        (pyg.key.get_pressed()[pyg.K_RIGHT]) or (pyg.key.get_pressed()[pyg.K_d])):
                    x_player, y_player, angle[1] = (x_player + xmov / 2), (y_player - ymov), 1

                # Diagonale haut-gauche
                if ((pyg.key.get_pressed()[pyg.K_UP]) or (pyg.key.get_pressed()[pyg.K_z])) and (
                        (pyg.key.get_pressed()[pyg.K_LEFT]) or (pyg.key.get_pressed()[pyg.K_q])):
                    x_player, y_player, angle[1] = (x_player - xmov / 2), (y_player - ymov), 1

                # Diagonale bas-droite
                if ((pyg.key.get_pressed()[pyg.K_DOWN]) or (pyg.key.get_pressed()[pyg.K_s])) and (
                        (pyg.key.get_pressed()[pyg.K_RIGHT]) or (pyg.key.get_pressed()[pyg.K_d])):
                    x_player, y_player, angle[1] = (x_player + xmov / 2), (y_player + ymov), -1

                # Diagonale bas-gauche
                if ((pyg.key.get_pressed()[pyg.K_DOWN]) or (pyg.key.get_pressed()[pyg.K_s])) and (
                        (pyg.key.get_pressed()[pyg.K_LEFT]) or (pyg.key.get_pressed()[pyg.K_q])):
                    x_player, y_player, angle[1] = (x_player - xmov / 2), (y_player + ymov), 1

            # On déplace la hitbox du joueur avec ses coordonnées
            # On ajoute aux coordonnées brutes du joueur le décalage obtenu avec la fonction "pyg.Rect.inflate_ip()" utilisée au début du programme
            player_rect_norm.topleft, player_rect_tilt.topleft = (x_player + offset1 / 2, y_player + offset1 / 2), (
            x_player + offset2 / 2, y_player + offset2 / 2)

            # Changement du sprite et de la hitbox selon l'angle
            if angle[1] == 0:
                player, player_rect = player_norm, player_rect_norm
            elif angle[1] > 0:
                player, player_rect = player_up, player_rect_tilt
            elif angle[1] < 0:
                player, player_rect = player_down, player_rect_tilt
            # L'angle actuel devient l'angle précédent de la prochaine boucle
            angle[0] = angle[1]

            if point == 5 and niveau_de_danger == 0:
                niveau_de_danger += 1
                pyg.Rect.inflate_ip(safezone_rect, -shrink_width, -shrink_height)
            elif point == 20 and niveau_de_danger == 1:
                niveau_de_danger += 1
                pyg.Rect.inflate_ip(safezone_rect, -shrink_width, -shrink_height)
                feu_haut.height, feu_bas.topleft, feu_bas.height = feu_haut.height + shrink_height / 2, (
                0, screen_rect.height - shrink_height), feu_haut.height + shrink_height / 2
                feu_gauche.width, feu_droit.topleft, feu_droit.width = feu_gauche.width + shrink_width / 2, (
                screen_rect.width - shrink_width, 0), feu_gauche.width + shrink_width / 2

            # Le joueur est retéléporté au centre de l'écran et il perd un nombre considérable de points
            inbounds = pyg.Rect.colliderect(player_rect, screen_rect)
            if not inbounds:
                x_player, y_player = screen_rect.center
                angle = [0, 0]
                point -= 25  # Malus

            # On vérifie que le joueur évite bien la zone rouge
            safe = pyg.Rect.colliderect(player_rect, safezone_rect)
            if not safe:
                point -= 1  # Malus chaque tick passé dans la zone rouge
                anim_explo = pyg.sprite.Group()
                explosion = explo(x_player, y_player)
                anim_explo.add(explosion)
                explosion.animate()
                anim_explo.draw(screen)
                anim_explo.update(0.35)

            # On regarde s'il y a collision entre l'avion et l'anneau
            collide = pyg.Rect.colliderect(player_rect, ring_rect)
            # Après la collision, un point au score est rajouté et l'anneau est replacé à un endroit différent
            if collide:
                point += 1
                position[0], position[1] = position[1], position[2]
                # On tire un nombre au sort jusqu'à ce que celui-ci soit différent des deux derniers
                # Cela signifie que l'anneau ne sera jamais replacé au même endroit de suite
                while (position[2] == position[1]) or (position[2] == position[0]):
                    if point < 20:
                        position[2] = randint(1, 12)
                    else:
                        position[2] = randint(1, 8)
                # Assignation de la nouvelle coordonnée y de l'anneau selon le nombre tiré au sort
                if position[2] <= 4:
                    y_ring = screen_rect.height // 4
                elif position[2] > 4 and position[2] <= 8:
                    position[2] -= 4
                    y_ring = screen_rect.height // 2
                else:
                    position[2] -= 8
                    y_ring = screen_rect.height * 3 // 4
                # Assignation de la nouvelle coordonnée x de l'anneau
                x_ring = screen_rect.width * position[2] // 5
                # On remet la hitbox de l'anneau aux nouvelles coordonnées de ce-dernier
                ring_rect.topleft = (x_ring + offset3 / 2, y_ring + offset3 / 2)

            # Condition de victoire
        seconds = round(30 - ((pyg.time.get_ticks() - start_ticks) / 1000))
        if seconds <= 0:
            pyg.key.set_repeat(1)
            if point >= 30:
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
        anim_explo.draw(screen)
        anim_explo.update(0.30)
        pyg.display.update()

        # Réaffiche l'écran
        screen.blit(fond, (0, 0))

        clock.tick(60)
