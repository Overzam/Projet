import pygame as pyg
def trans_screen():
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
        seconds = round(3 - ((pyg.time.get_ticks() - start_ticks) / 1000))
        font = pyg.font.Font('freesansbold.ttf', 256)
        countdown = font.render(str(seconds), True, blanc, noir)
        screen.blit(countdown, (height//2 - 50, width / 2 - 50))
        pyg.display.update()
        if seconds <= 0:
            break