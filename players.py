from behaviors import*
current_dir = os.path.dirname(__file__) #Проложить путь к исполняемому файлу
img_dir = os.path.join(current_dir, '..', 'img')
image_paths = []
for filename in os.listdir(img_dir):
    if filename.endswith('.png'):
        image_path = os.path.join(img_dir, filename)
        image_paths.append(image_path)

images = []
for image_path in image_paths:
    image = p.image.load(image_path)
    images.append(image)


class PLAYERS(BEHAVIOR):
    def __init__(self):
        super().__init__()
        self.size = (32, 32)
        self.rect = p.Rect(randint(self.size[0], SIZE[0] - self.size[0]),
                           randint(self.size[1], SIZE[1] - self.size[1]),
                           self.size[0],
                           self.size[1]
                           )
        self.color = BEIGE
        self.speed = 5
        self.image = image[0]

    def move(self):
        keys = p.key.get_pressed()
        if keys[p.K_w]:
            self.rect.y -= self.speed
        if keys[p.K_s]:
            self.rect.y += self.speed
        if keys[p.K_a]:
            self.rect.x -= self.speed
        if keys[p.K_d]:
            self.rect.x += self.speed

player = PLAYERS()