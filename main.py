from behaviors import*
from MAP.script.maps import*
from Player.script.players import*
'''''
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

'''

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()

        SCREEN.fill(LIME)

        for obj in map_obj:
            obj.draw_rect()
            obj.move()
        player.move()
        player.draw_rect()


    p.display.flip()
    clock.tick(FPS)