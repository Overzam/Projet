import pygame as pyg
def trans_screen_keyboard():
    from jeu_1 import height, width, screen, despawn
    despawn()
    start_ticks = pyg.time.get_ticks()
    noir = (0, 0, 0)
    blanc = (200, 200, 200)
    touche = pyg.image.load("img_thomas/fleche.png")
    pyg.transform.scale(touche, (100, 100))
    while True:
        for event in pyg.event.get():
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    pyg.quit()
                    exit()
        bgtrans = pyg.image.load("img_dylan/menu_bg.jpg")
        bgtrans = pyg.transform.scale(bgtrans, (height, width))
        screen.blit(bgtrans, (0, 0))
        screen.blit(touche, (height//2 - 300, width // 10 - 100))
        seconds = round(3 - ((pyg.time.get_ticks() - start_ticks) / 1000))
        font = pyg.font.Font('freesansbold.ttf', 256)
        countdown = font.render(str(seconds), True, blanc, noir)
        screen.blit(countdown, (height//2 - 50, width / 2 - 50))
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

