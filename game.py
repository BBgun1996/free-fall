import arcade
from models import World
 
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

GAME_SCREEN = 0
GAMEOVER_SCREEN = 1
RESTART_SCREEN = 2
 
class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.world = World(width, height) 

        self.gamescreen_sprite = ModelSprite('images/gamescreen.png', model=self.world.background)
        self.gameover_sprite = ModelSprite('images/gameover.png', model=self.world.background) 
        self.basket_sprite = ModelSprite('images/basket.png', model=self.world.basket)
        self.ball_sprite = ModelSprite('images/ball.png', model=self.world.ball)
        self.cursor_sprite = ModelSprite('images/cursor.png', model=self.world.cursor)

        self.screen_bg = GAME_SCREEN

    def on_draw(self):
        arcade.start_render()
        
        if(self.screen_bg == GAME_SCREEN):
            self.gamescreen_sprite.draw()
            self.basket_sprite.draw()
            self.ball_sprite.draw()
            self.cursor_sprite.draw()

            arcade.draw_text("level : " + str(self.world.level),
                             20, self.height - 30,
                             arcade.color.BLACK, 14)
            arcade.draw_text("life : " + str(self.world.life),
                             20, self.height - 60,
                             arcade.color.BLACK, 12)
            arcade.draw_text("ball : " + str(self.world.ball_in_basket),
                             20, self.height - 80,
                             arcade.color.BLACK, 12)

        if(self.screen_bg == GAMEOVER_SCREEN):
            self.gameover_sprite.draw()
            arcade.draw_text("level " + str(self.world.level),
                             420, 350,
                             arcade.color.BLACK, 15)

            arcade.draw_text("....PRASS ENTER TO RESTART GAME....",
                             20, 20,
                             arcade.color.BLACK, 12)         

        if(self.screen_bg == RESTART_SCREEN):
            self.world.level = 1
            self.world.ball_in_basket = 0

            self.screen_bg = GAME_SCREEN

    def animate(self, delta):
        self.world.animate(delta)

        if self.world.life <= 0:
            self.screen_bg = GAMEOVER_SCREEN
            

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

        if key == arcade.key.ENTER:
            if self.screen_bg == GAMEOVER_SCREEN:
                self.world.life = 5
                self.screen_bg = RESTART_SCREEN
            

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
