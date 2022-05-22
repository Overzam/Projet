import pygame as pyg
from sys import exit


def base_menu():
    from jeu_1 import height, width, screen
    from transition import trans_screen_keyboard
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
    quit_but = pyg.transform.scale(quit_but, (height // 4, width // 5)).convert_alpha()
    play_but_hover = pyg.image.load("img_dylan/jouerwhite.png")
    play_but_hover = pyg.transform.scale(play_but_hover, (height // 5, width // 5)).convert_alpha()
    options_but_hover = pyg.image.load("img_dylan/testwhite.png")
    options_but_hover = pyg.transform.scale(options_but_hover, (height // 5, width // 5)).convert_alpha()
    quit_but_hover = pyg.image.load("img_dylan/quitterwhite.png")
    quit_but_hover = pyg.transform.scale(quit_but_hover, (height // 4, width // 5)).convert_alpha()

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
    quit_but = button(height // 2 - 240, 800, quit_but)

    play = pyg.image.load("img_dylan/play_but.png")
    play = pyg.transform.scale(play, (height // 5, width // 5)).convert_alpha()
    options = pyg.image.load("img_dylan/option_but.png")
    options = pyg.transform.scale(options, (height // 5, width // 5)).convert_alpha()
    quit = pyg.image.load("img_dylan/quit_butt.png")
    quit = pyg.transform.scale(quit, (height // 4, width // 5)).convert_alpha()

    font = pyg.font.Font('freesansbold.ttf', 128)
    titre = "Hagini sauce"
    texte = font.render(str(titre), True, white, black)
    screen.blit(texte, (height // 2 - 350, 50))
    pyg.display.update()

    while True:
        mouse = pyg.mouse.get_pos()
        if mouse[0] > height // 2 - 200 and mouse[0] < height // 2 - 200 + height // 5 and mouse[1] > 200 and mouse[1] < 200 + width // 5:
            play_but = button(height // 2 - 200, 200, play_but_hover)
        else:
            play_but = button(height // 2 - 200, 200, play)

        if mouse[0] > height // 2 - 200 and mouse[0] < height // 2 - 200 + height // 5 and mouse[1] > 500 and mouse[1] < 500 + width // 5:
            options_but = button(height // 2 - 200, 500, options_but_hover)
        else:
            options_but = button(height // 2 - 200, 500, options)

        if mouse[0] > height // 2 - 200 and mouse[0] < height // 2 - 200 + height // 5 and mouse[1] > 800 and mouse[1] < 800 + width // 5:
            quit_but = button(height // 2 - 200, 800, quit_but_hover)
        else:
            quit_but = button(height // 2 - 200, 800, quit)

        if play_but.draw():
            musique_menu.stop()
            gamemode = 0
            trans_screen_keyboard()
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
