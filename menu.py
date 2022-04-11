import pygame as pyg
from sys import exit


def base_menu():
    from jeu_1 import height, width, screen
    from transition import trans_screen
    from jeu_dylan import jeu
    from menu_mini_jeu import menu_mini
    global score
    global gamemode
    pyg.mouse.set_visible(True)
    black = (0, 0, 0)
    white = (255, 255, 255)
    musique_menu = pyg.mixer.Sound('son/into_the_night.wav')
    musique_menu.set_volume(0.1)
    musique_menu.play()
    score = 0
    bgmenu = pyg.image.load("img_dylan/menu_bg.jpg")
    bgmenu = pyg.transform.scale(bgmenu, (height, width))
    screen.blit(bgmenu, (0, 0))
    play_but = pyg.image.load("img_dylan/play_but.png")
    play_but = pyg.transform.scale(play_but, (height // 5, width // 5)).convert_alpha()
    options_but = pyg.image.load("img_dylan/option_but.png")
    options_but = pyg.transform.scale(options_but, (height // 5, width // 5)).convert_alpha()
    quit_but = pyg.image.load("img_dylan/quit_butt.png")
    quit_but = pyg.transform.scale(quit_but, (height // 5 - 10, width // 5)).convert_alpha()

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

    play_but = button(height // 2 - 200, 200, play_but)
    options_but = button(height // 2 - 200, 500, options_but)
    quit_but = button(height // 2 - 190, 800, quit_but)

    font = pyg.font.Font('freesansbold.ttf', 128)
    titre = "Wario Ware"
    texte = font.render(str(titre), True, white, black)
    screen.blit(texte, (height // 2 - 350, 50))
    pyg.display.update()

    while True:
        if play_but.draw():
            musique_menu.stop()
            gamemode = 0
            trans_screen()
            jeu()
        if options_but.draw():
            musique_menu.stop()
            gamemode = 1
            menu_mini()
        if quit_but.draw():
            pyg.quit()
            exit()

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()

        pyg.display.update()
