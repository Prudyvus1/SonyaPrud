from behaviors import*


class GUNS(BEHAVIOR):
    def __init__(self):
        super().__init__()
        self.size = (8, 8)
        self.rect = p.Rect(randint(self.size[0], SIZE[0] - self.size[0]),
                           randint(self.size[1], SIZE[1] - self.size[1]),
                           self.size[0],
                           self.size[1]
                           )
        self.color = BEIGE

player = GUNS()