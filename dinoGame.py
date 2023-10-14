import pygame as p
from sys import*


p.init()
p.mixer.init()

WIDTH, HEIGHT = 500, 500

p.display.set_caption('Dino game')
sceen = p.display.set_mode((WIDTH, HEIGHT))

FPS = 60
clock = p.time.Clock()

YELLOW = (255, 255, 0)