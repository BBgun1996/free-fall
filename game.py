import arcade
from models import World
 
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
 
class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
 
        self.world = World(width, height) 
        self.background_sprite = ModelSprite('images/background.png', model=self.world.background) 
        self.basket_sprite = ModelSprite('images/basket.png', model=self.world.basket) 


 
    def on_draw(self):
        arcade.start_render()
        self.background_sprite.draw()
        self.basket_sprite.draw()


        arcade.draw_text("level : " + str(self.world.level),
                         20, self.height - 30,
                         arcade.color.BLACK, 12)
        arcade.draw_text("score : " + str(self.world.score),
                         20, self.height - 50,
                         arcade.color.BLACK, 12)



    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
