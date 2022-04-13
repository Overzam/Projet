import pygame as pyg
from sys import exit
from random import randint
from menu import base_menu

height = 1920
width = 1080

pyg.init()
pyg.mixer.init()
pyg.font.init()

x_explo = 100
y_explo = 100

screen = pyg.display.set_mode((height, width))

pyg.display.set_caption('boom')

icon = pyg.image.load('img_dylan/imgicon.png')
pyg.display.set_icon(icon)

background = pyg.image.load("img_dylan/fond1.jpg")
background = pyg.transform.scale(background, (height, width))
fond = background.convert()

    
class explo(pyg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        vide = pyg.image.load('img_dylan/transpar.png')
        explo1 = pyg.image.load('img_dylan/explosion-frame-1.png')
        explo1 = pyg.transform.scale(explo1, (x_explo - 5, y_explo - 5))
        explo2 = pyg.image.load('img_dylan/explosion-frame-2.png')
        explo2 = pyg.transform.scale(explo2, (x_explo, y_explo))
        explo3 = pyg.image.load('img_dylan/explosion-frame-3.png')
        explo3 = pyg.transform.scale(explo3, (x_explo, y_explo))
        explo4 = pyg.image.load('img_dylan/explosion-frame-4.png')
        explo4 = pyg.transform.scale(explo4, (x_explo, y_explo))
        explo5 = pyg.image.load('img_dylan/explosion-frame-5.png')
        explo5 = pyg.transform.scale(explo5, (x_explo, y_explo))
        explo6 = pyg.image.load('img_dylan/explosion-frame-6.png')
        explo6 = pyg.transform.scale(explo6, (x_explo, y_explo))
        explo7 = pyg.image.load('img_dylan/explosion-frame-7.png')
        explo7 = pyg.transform.scale(explo7, (x_explo, y_explo))
        explo8 = pyg.image.load('img_dylan/explosion-frame-8.png')
        explo8 = pyg.transform.scale(explo8, (x_explo, y_explo))
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


def despawn():
    global background
    global losescreen
    global xsoldat1
    global xsoldat
    global xtank
    xsoldat1 = -1000
    xsoldat = -1000


def amongus():
    despawn()
    music_drip = pyg.mixer.Sound('son/amongus.wav')
    music_drip.set_volume(1)
    music_drip.play()
    while True:
        bgamong = pyg.image.load('img_dylan/amongus.jpg')
        bgamong = pyg.transform.scale(bgamong, (height, width))
        screen.blit(bgamong, (0, 0))
        pyg.display.update()
        for event in pyg.event.get():
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    music_drip.stop()
                    base_menu()
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()


def win():
    despawn()
    musique_victoire = pyg.mixer.Sound('son/musique_victoire.mp3')
    musique_victoire.set_volume(1)
    musique_victoire.play()
    while True:
        bgjeudylan = pyg.image.load("img_dylan/win.jpg")
        bgjeudylan = pyg.transform.scale(bgjeudylan, (height, width))
        screen.blit(bgjeudylan, (0, 0))
        pyg.display.update()
        for event in pyg.event.get():
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    base_menu()
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()


def loose():
    while True:
        bgloose = pyg.image.load("img_dylan/game_over.jpg")
        bgloose = pyg.transform.scale(bgloose, (height, width))
        screen.blit(bgloose, (0, 0))
        pyg.display.update()
        for event in pyg.event.get():
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    base_menu()
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()


def shake(screen_shake):
    while screen_shake != 0:
        screen_shake -= 1
        render_distance = [0, 0]
        render_distance[0], render_distance[1] = randint(0, 8) - 4, randint(0, 8) - 4
        screen.blit(background, render_distance)



base_menu()
