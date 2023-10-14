from dinoGame import*

score = 0

class Label():
  def __init__(self, text,fsize=12, text_color=(255, 0, 0)):
        self.text = text
        self.x = 10
        self.y = 10
        self.rect = p.Rect(self.x, self.y, 64, 32)
        self.image = p.font.SysFont('verdana', fsize).render(self.text, True, text_color)

  def draw(self):
      
      sceen.blit(self.image, (self.rect.x, self.rect.y))


class players:
    def __init__(self):
        self.x = 10
        self.y = 369
        self.image = p.image.load('dino.png')
        self.rect = p.Rect(self.x, self.y, 64, 32)


    def draw(self):
        sceen.blit(self.image, self.rect)


    def jump(self):
        for _ in range(20):
            self.rect.y -= 2
            sceen.fill((0,0,0))
            p.draw.rect(sceen, YELLOW, platform)
            self.draw()
    
    def gravity(self):
        self.rect.y += 1
        sceen.fill((0,0,0))
        p.draw.rect(sceen, YELLOW, platform)
        self.draw()


class bloks:
    def __init__(self):
        self.x = 516
        self.y = 384
        self.image = p.image.load('cactus.png')
        self.rect = p.Rect(self.x, self.y, 16, 16)
        self.speed = 3

    def draw(self):
        sceen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.x -= self.speed
        if self.rect.x < -16:
            self.rect.x = self.x

platform = p.Rect(0, 400, 500, 100)
p.draw.rect(sceen, YELLOW, platform)

cactus_list = [bloks() for _ in range(1)]

player = players()
text_score = Label('Score: '+str(score))

while True:
    keys = p.key.get_pressed()

    player.draw()
    
    if player.rect.colliderect(platform):
        if keys[p.K_SPACE]:
            player.jump()

    else:
        player.gravity()
        
    for cactus in cactus_list:
        cactus.move()
        sceen.fill((0,0,0))
        p.draw.rect(sceen, YELLOW, platform)
        player.draw()
        cactus.draw()
        if player.rect.colliderect(cactus.rect): p.quit(); exit()


    text_score.draw()
    for event in p.event.get():
        if event.type == p.QUIT: p.quit(); exit()
            
    p.display.flip()
    clock.tick(FPS)
