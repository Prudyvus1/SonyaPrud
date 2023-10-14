
import pygame as p
import sys
from time import*
p.init()
p.mixer.init()


WIDTH, HEIGHT = 500, 500
FPS = 60
has_played_sound = False
screen = p.display.set_caption('Dino game')
screen = p.display.set_mode((WIDTH, HEIGHT))

clock = p.time.Clock()
score = 0
score_song = 0
jump_sound = p.mixer.Sound('jump.mp3')
score_sound = p.mixer.Sound('score_up.mp3')
lose_sound = p.mixer.Sound('lose.mp3')
class Label():
    
    def __init__(self):
        self.x = 10
        self.y = 10
        self.rect = p.Rect(self.x, self.y, 1,1)

    def set_text(self, text, fsize=12, text_color=(255, 0, 0)):
        self.image = p.font.SysFont('verdana', fsize).render(text, True, text_color)
        
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        


class players:

    images = p.image.load('dino.png')

    def __init__(self):
        self.x = 60
        self.y = 320
        self.photo = p.image.load('dino.png')
        self.image = p.transform.scale(self.photo, (235/4, 218/4))
        self.rect = p.Rect(self.x, self.y, 235/4, 185/4)

    def jump(self):
        keys = p.key.get_pressed()
        
        
        if keys[p.K_SPACE]:
            jump_sound.play()
            for _ in range(30):
                self.rect.y -= 2


    def gravity(self):
        self.rect.y += 1

    def draw(self):
        screen.blit(self.image, self.rect)


class bloks:
    def __init__(self):
        self.x = 560
        self.y = 340
        self.photo = p.image.load('cactus.png')
        self.image = p.transform.scale(self.photo, (32, 40))
        self.rect = p.Rect(self.x, self.y, 32, 40)


    def draw(self):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.rect.x = 560
        
def game():
    WIDTH, HEIGHT = 500, 500
    FPS = 60
    has_played_sound = False
    screen = p.display.set_caption('Dino game')
    screen = p.display.set_mode((WIDTH, HEIGHT))

    clock = p.time.Clock()
    score = 0
    score_song = 0
    jump_sound = p.mixer.Sound('jump.mp3')
    score_sound = p.mixer.Sound('score_up.mp3')
    lose_sound = p.mixer.Sound('lose.mp3')
    score_text = Label()
    score_text.set_text('Счет: '+str (score))

    platform = p.Rect(0, 375, 500, 125)
    player = players()
    block = bloks()
    frame_delay = 80
    frame_delay1 = 200
    last_frame_time = p.time.get_ticks()
    last_frame_time1 = p.time.get_ticks()
    los = False

    while True:
        
        current_time = p.time.get_ticks()
        screen.fill((0,0,0))
        p.draw.rect(screen, (0,255,0), platform)

        block.draw()
        block.move()
    
        player.draw()
        score_text.draw()
        if current_time - last_frame_time >= frame_delay:
            score += 1
            score_song += 1
            score_text.set_text('Счет: ' + str(score))
            last_frame_time = current_time
            if score_song >= 100 and not has_played_sound:
                score_sound.play()
                has_played_sound = True
                score_song = 0

        if current_time - last_frame_time1 >= frame_delay1 and has_played_sound:
            has_played_sound = False
    
            

        if player.rect.colliderect(platform):
            player.jump()


            
        else:
            player.gravity() 



        if player.rect.colliderect(block) and los == False: 
            los = True
        
            lose_sound.play()
            sleep(2)
            break

        for event in p.event.get():
            if event.type == p.QUIT: p.quit(); sys.exit()    

        p.display.flip()
        clock.tick(FPS)
while True:
    game()
