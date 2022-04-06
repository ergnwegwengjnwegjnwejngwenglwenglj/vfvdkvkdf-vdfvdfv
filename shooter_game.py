from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load("galaxy.jpg"), (700, 500))



mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

clock = time.Clock()

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (75,75))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):

        keys = key.get_pressed()

        if (keys[K_LEFT] or keys[K_a]) and self.rect.x > 5:
            self.rect.x -= self.speed
        
        if (keys[K_RIGHT] or keys[K_d]) and self.rect.x < 620:
            self.rect.x += self.speed

        if (keys[K_UP] or keys[K_w]) and self.rect.y > 10:
            self.rect.y -= self.speed
        
        if (keys[K_DOWN] or keys[K_s]) and self.rect.y < 420:
            self.rect.y += self.spee




hero = Player('rocket.png', 500, 28, 5)

game = True
while game:
    

    

    display.update()
    clock.tick(1000)


