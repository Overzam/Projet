import pygame as pyg
from sys import exit

def menu_mini():
    from jeu_1 import screen, height, width
    from jeu_dylan import jeu
    from jeu_maximilien import jeu_max
    from jeu_thomas import jeu_tomaye
    from menu import base_menu
    from transition import trans_screen_mouse, trans_screen_keyboard
    from jeu_elliott import jeu_ell
    black = (0, 0, 0)
    white = (255, 255, 255)
    bgmenu = pyg.image.load("img_dylan/menu_bg.jpg")
    bgmenu = pyg.transform.scale(bgmenu, (height, width))
    screen.blit(bgmenu, (0, 0))
    jeu1 = pyg.image.load("img_dylan/preview_dylan.png")
    jeu1 = pyg.transform.scale(jeu1, (height // 5, width // 5)).convert_alpha()
    jeu2 = pyg.image.load("img_dylan/preview_max.png")
    jeu2 = pyg.transform.scale(jeu2, (height // 5, width // 5)).convert_alpha()
    jeu3 = pyg.image.load("img_dylan/preview_tomaye.png")
    jeu3 = pyg.transform.scale(jeu3, (height // 5, width // 5)).convert_alpha()
    jeu4 = pyg.image.load("img_dylan/preview_elliott.png")
    jeu4 = pyg.transform.scale(jeu4, (height // 5, width // 5)).convert_alpha()
    font = pyg.font.Font('freesansbold.ttf', 16)

    class button:
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            action = False

            pos = pyg.mouse.get_pos()

            if self.rect.collidepoint(pos):
                for evenement in pyg.event.get():
                    if evenement.type == pyg.MOUSEBUTTONUP and self.clicked == False:
                        self.clicked = True
                        action = True

            screen.blit(self.image, (self.rect.x, self.rect.y))
            return action

    jeu1 = button(height // 4 + 50, 200, jeu1)
    jeu2 = button(height // 2 + 50, 200, jeu2)
    jeu3 = button(height // 4 + 50, 600, jeu3)
    jeu4 = button(height // 2 + 50, 600, jeu4)

    pyg.display.update()

    while True:
        if jeu1.draw():
            trans_screen_keyboard()
            jeu()
        if jeu2.draw():
            trans_screen_mouse()
            jeu_max()
        if jeu3.draw():
            trans_screen_keyboard()
            jeu_tomaye()
        if jeu4.draw():
            trans_screen_keyboard()
            jeu_ell()

        titre_elliott = "L'attaque aérienne"
        texte_jeu_elliott = font.render(str(titre_elliott), True, white, black)
        screen.blit(texte_jeu_elliott, (height // 2 + 150, 570))

        titre_tomaye = "L'attaque sur la France"
        texte_jeu_tomaye = font.render(str(titre_tomaye), True, white, black)
        screen.blit(texte_jeu_tomaye, (height // 4 + 150, 570))

        titre_max = "L'attaque des Bateaux"
        texte_jeu_max = font.render(str(titre_max), True, white, black)
        screen.blit(texte_jeu_max, (height // 2 + 150, 170))

        titre_jeu_dylan = "L'attaque des Parachutistes"
        texte_jeu_dylan = font.render(str(titre_jeu_dylan), True, white, black)
        screen.blit(texte_jeu_dylan, (height // 4 + 150, 170))

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    base_menu()

        pyg.display.update()
