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

map_list = []

for _ in range(randint(10, 30)):
    map_list.append(0)

for _ in range(randint(10, 30)):
    map_list.append(1)

class MAPS(BEHAVIOR):
    def __init__(self, obj):
        super().__init__()
        self.index = obj
        self.size = (32, 32)
        if self.index == 0:
            self.size = (32, 32)
            self.image = image[0]
            self.color = GRAY
            self.rect = p.Rect(randint(self.size[0], SIZE[0] - self.size[0]), #X
                               randint(self.size[1], SIZE[1] - self.size[1]), #Y
                               self.size[0], # Ширина
                               self.size[1] # Высота
                               )
        if self.index == 1:
            self.size = (32, 32)
            self.image = image[1]
            self.color = BROWN
            self.rect = p.Rect(randint(self.size[0], SIZE[0] - self.size[0]), #X
                               randint(self.size[1], SIZE[1] - self.size[1]), #Y
                               self.size[0], # Ширина
                               self.size[1] # Высота
                               )


map_obj = []

for obj in map_list:
    map_obj.append(MAPS(obj))

remover_obj = map_obj


new_map_obj = []

for i, x in enumerate(map_obj):
    overlapping = False #Флаг, указывающий, было бы перекрытие
    for j, y in enumerate(remover_obj):
        if i != j and x.rect.colliderect(y.rect):
            print(x, 'Был удален')
            overlapping = True
            break

    if not overlapping:
        new_map_obj.append(x)
map_obj = new_map_obj
