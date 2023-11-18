from imports import*

SIZE = (1600, 900) # Ширина, Высота

p.display.set_caption('Shooter') # Создание проекта
SCREEN = p.display.set_mode(SIZE) # Создание экрана

FPS = 60

clock = p.time.Clock()

LIME = (204, 255, 0)
GRAY = (128, 128, 128)
BROWN = (128, 64, 48)
BEIGE = (245, 245, 220)