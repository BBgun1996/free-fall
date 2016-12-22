import arcade.key
from random import randint

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def hit(self, other, hit_size_x , hit_size_y):
        return (abs(self.x - other.x) <= hit_size_x) and (abs(self.y - other.y) <= hit_size_y)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1
        self.ball_in_basket = 0
        self.background = Background(self, width/2, height/2)
        self.basket = Basket(self, 450, 450)
        self.ball = Ball(self, 140, 619)

    def animate(self, delta):
        self.ball.animate(delta)
        self.basket.animate(delta)

        if self.ball.y <= 0:
            self.ball.new_ball()

        if self.ball.hit(self.basket, 50, 100):
            self.ball_in_basket += 1

        if self.level == self.ball_in_basket:
            self.basket.random_location()
            self.ball_in_basket = 0
            self.level += 1

        if self.level >= 3:
            self.basket.speed = (self.level - 2)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ball.speed_y = 1
            self.ball.speed_x = randint(1, 120)

class Ball(Model):

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.speed_x = 0
        self.speed_y = 0

    def animate(self, delta):
        self.x += self.speed_x
        self.y -= self.speed_y
        self.speed_y *= 1.5

    def new_ball(self):
        self.speed_y = 0
        self.speed_x = 0
        self.x = 140
        self.y = 619

class Basket(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.speed = 0
        self.move_direction = 1

    def random_location(self):
        self.x = randint(150, self.world.width - 100)
        self.y = randint(50, self.world.height - 400)

    def animate(self, delta):
        if self.move_direction > 0:
            if self.x > (self.world.width - 100):
                self.move_direction = -1
        else:
            if self.x < 150:
                self.move_direction = 1

        self.x += (self.speed * self.move_direction)

class Background(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)


