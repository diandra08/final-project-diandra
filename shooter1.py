from pygame import *

# background music
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

# image
img_back = "galaxy.jpg"
img_hero = "rocket.png"

img_enemy = "ufo.png".#enemy

score = 0
lost = 0

class GameSprite(sprite.Sprite):
    def _init_(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite._init_(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    # method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[k_left] and self.rect.x > 5:
            self.rect.x -= self.rect.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self,rect.x += self,speed

    def fire(self):
        pass

cla
# create a window
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

finish = False

# Main loop
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0))

        ship.update()
        ship.reset()

        display.update()
        time.delay(50