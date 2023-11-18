from config import*

class BEHAVIOR:
    def __init__(self):
        pass

    def draw_rect(self):
        p.draw.rect(SCREEN, self.color, self.rect)

    def draw_img(self):
        SCREEN.blit(self.image, self.rect)
    def move(self):
        keys = p.key.get_pressed()
        if keys[p.K_w]:
            self.rect.y += self.speed
        if keys[p.K_s]:
            self.rect.y -= self.speed
        if keys[p.K_a]:
            self.rect.x += self.speed
        if keys[p.K_d]:
            self.rect.x -= self.speed
