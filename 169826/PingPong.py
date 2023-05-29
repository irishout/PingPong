from pygame import *

mixer.init()
mixer.music.load('BeachMusic.mp3')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, size_x, size_y, speed = 0):
        super().__init__()
        self.image = transform.scale(
            image.load(picture),
            (size_x, size_y)
            )       
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def show(self): 
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def updateL(self, keys_pressed):
        if keys_pressed[K_w] and (self.rect.y - 5) > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and (self.rect.y + 5) < 350:
            self.rect.y += self.speed 
    def updateR(self, keys_pressed):
        if keys_pressed[K_UP] and (self.rect.y - 5) > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and (self.rect.y + 5) < 350:
            self.rect.y += self.speed 

window = display.set_mode((700,500))
background = transform.scale(
    image.load("beach.jpg"),
    (700,500)
)

playerL = Player("weapon.png", 70, 300, 50, 150, 3)
playerR = Player("weapon.png", 600, 300, 50, 150, 3)

ball = GameSprite("tennis.png", 350, 350, 50, 50, 3)

flag_x = 1
flag_y = 1
FPS = 60
clock = time.Clock()
gameon = True
finish = False
while gameon:
    for e in event.get():
        if e.type == QUIT:
            gameon = False

    if not finish:
        window.blit(background,(0,0))
        keys_pressed = key.get_pressed()
        playerL.updateL(keys_pressed)
        playerL.show()
        playerR.updateR(keys_pressed)
        playerR.show()        

        ball.show()

        ball.rect.x += ball.speed * flag_x
        ball.rect.y += ball.speed * flag_y
        if sprite.collide_rect(playerL, ball):
            flag_x *=-1      
        if sprite.collide_rect(playerR, ball):
            flag_x *=-1           
        if ball.rect.y > 450 or ball.rect.y < 0:
            flag_y *=-1 

        if ball.rect.x < 0:
            font.init()
            text = font.Font(None, 90).render('Left player lose', True, (255, 0, 0))
            window.blit(text, (150, 200)) 
            finish = True
        if ball.rect.x > 650:
            font.init()
            text = font.Font(None, 90).render('Right player lose', True, (255, 0, 0))
            window.blit(text, (150, 200))    
            finish = True                  


    display.update()
    clock.tick(FPS)