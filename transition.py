import pygame as pyg
def trans_screen_keyboard():
    from jeu_1 import height, width, screen, despawn
    despawn()
    start_ticks = pyg.time.get_ticks()
    noir = (0, 0, 0)
    blanc = (200, 200, 200)
    touche_bas = pyg.image.load("img_dylan/fleche-bas.png").convert_alpha()
    touche_bas = pyg.transform.scale(touche_bas, (100, 100))
    touche_droite = pyg.image.load("img_dylan/fleche-droite.png").convert_alpha()
    touche_droite = pyg.transform.scale(touche_droite, (100, 100))
    touche_gauche = pyg.image.load("img_dylan/fleche-gauche.png").convert_alpha()
    touche_gauche = pyg.transform.scale(touche_gauche, (100, 100))
    touche_haut = pyg.image.load("img_dylan/fleche-haut.png").convert_alpha()
    touche_haut = pyg.transform.scale(touche_haut, (100, 100))
    while True:
        for event in pyg.event.get():
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    pyg.quit()
                    exit()
        bgtrans = pyg.image.load("img_dylan/menu_bg.jpg")
        bgtrans = pyg.transform.scale(bgtrans, (height, width))
        screen.blit(bgtrans, (0, 0))
        screen.blit(touche_bas, (height//2 - 50, width // 8))
        screen.blit(touche_haut, (height // 2 - 50, width // 8 - 100))
        screen.blit(touche_droite, (height // 2 + 50, width // 8))
        screen.blit(touche_gauche, (height // 2 - 150, width // 8 ))
        seconds = round(3 - ((pyg.time.get_ticks() - start_ticks) / 1000))
        font = pyg.font.Font('freesansbold.ttf', 256)
        countdown = font.render(str(seconds), True, blanc, noir)
        screen.blit(countdown, (height //2 - 50, width / 2 - 50))
        pyg.display.update()
        if seconds <= 0:
            break

def trans_screen_mouse():
    from jeu_1 import height, width, screen, despawn
    despawn()
    start_ticks = pyg.time.get_ticks()
    noir = (0, 0, 0)
    blanc = (200, 200, 200)
    while True:
        for event in pyg.event.get():
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    pyg.quit()
                    exit()
        bgtrans = pyg.image.load("img_dylan/menu_bg.jpg")
        bgtrans = pyg.transform.scale(bgtrans, (height, width))
        screen.blit(bgtrans, (0, 0))
        touche = pyg.image.load("img_dylan/mouse.png")
        screen.blit(touche, (height//2 - 400, width // 10))
        seconds = round(3 - ((pyg.time.get_ticks() - start_ticks) / 1000))
        font = pyg.font.Font('freesansbold.ttf', 256)
        countdown = font.render(str(seconds), True, blanc, noir)
        screen.blit(countdown, (height//2 - 50, width / 2 - 50))
        pyg.display.update()
        if seconds <= 0:
            break

