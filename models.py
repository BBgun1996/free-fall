import arcade.key
from random import randint

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1
        self.score = 0
        self.background = Background(self, 450, 450)
        self.basket = Basket(self, 450, 450)





    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.score += 1





class Basket(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def random_location(self):
        self.x = randint(100, self.world.width - 1)
        self.y = randint(50, self.world.height - 400)

class Background(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)


