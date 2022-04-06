from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load("background.jpg"), (700, 500))



mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')


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


    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed


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
            self.rect.y += self.speed
        
class Enemy(GameSprite):
    direction = 'left'
    def update_l_r(self):

        if self.rect.x > 200:
            self.direction = 'left'
        if self.rect.x < 10:
            self.direction = 'right'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

   
    def update_u_d(self):

        if self.rect.y > 300:
            self.direction = 'UP'
        if self.rect.y < 50:
            self.direction = 'DOWN'
        
        
           


class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))

        self.rect = self.image.get_rect()
        self.rect_x = wall_x
        self.rect_y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect_x, self.rect_y))






hero = Player('hero.png', 500, 28, 5)
enemy = Enemy('cyborg.png', 400, 400, 5)
treasure = GameSprite('treasure.png', 200, 400, 0)
enemy1 = Enemy('cyborg.png', 10, 300, 5)

w1 = Wall(139, 72, 137, 100, 20, 500, 10)
w2 = Wall(139, 72, 137, 100, 200, 350, 10)
w3 = Wall(139, 72, 137, 100, 20, 10, 350)
w4 = Wall(139, 72, 137, 600, 20, 10, 350)
w5 = Wall(139, 72, 137, 200, 370, 510, 10)
w6 = Wall(139, 72, 137, 200, 100, 500, 10)


game = True
finish = False
class Enemy(GameSprite):

    def update(self):
        self.rect.y += self.speed


        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0,500)

while game:

    if finish != True:

        window.blit(background,(0,0))
        hero.reset()
        enemy.reset()
        enemy1.reset()

        treasure.reset()
        enemy.update_u_d()
        enemy1.update_l_r()
        hero.update()
    
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()

    if sprite.collide_rect(hero, treasure):
        finish = True
        window.blit(win, (200,200))
        money.play()

    if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, enemy1) or  sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5) or sprite.collide_rect(hero, w6):
        finish = True
        window.blit(lose, (200,200))
        kick.play()


    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(1000)


