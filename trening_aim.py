
from config import*
frame_delay = 800
last_frame_time = p.time.get_ticks()

frame_delay1 = 100
last_frame_time1 = p.time.get_ticks()


class balls:
    def __init__(self):
        self.x,self.y = randint(16,WIDTH-16), randint(16,HEIGHT+16)
        self.rect = p.Rect(self.x, self.y, 32,32)
        self.radius = 16
        self.color = YELLOW
        self.inv = False
        self.bye = 0
    def draw(self):
        #p.draw.rect(sceen, self.color, self.rect)
        p.draw.circle(sceen,(255,0,0),(self.x+16,self.y+16), self.radius)
        
    def resize(self):
        self.radius = 9

ball_list = [balls() for _ in range(1)]
for ball in ball_list:
    ball.draw()
while True:
    current_time = p.time.get_ticks()
    current_time1 = p.time.get_ticks()

    for event in p.event.get():
        if event.type == p.QUIT: p.quit(); exit()
        if event.type == p.MOUSEBUTTONDOWN and p.BUTTON_LEFT:
            
            xy = p.mouse.get_pos()
            
            for ball in ball_list:
                if ball.rect.collidepoint(xy):
                    ball_list.remove(ball)
                ball.resize()
    sceen.fill((0,0,0))
    for ball in ball_list:                
        ball.draw()

    if current_time - last_frame_time >= frame_delay:
        ball_list.append(balls())
        last_frame_time = current_time
    if current_time1 - last_frame_time1 >= frame_delay1:
        for ball in ball_list:
    
            if ball.inv:
                ball.radius +=1
                if ball.radius > 16+6:
                    ball.inv = False
                    ball.bye+=1
                    if ball.bye == 2:
                        ball_list.remove(ball)
            else:
                ball.radius -=1
                if ball.radius < 16-6:
                    ball.inv = True
        last_frame_time1 = current_time1

    p.display.flip()
    clock.tick(FPS)


