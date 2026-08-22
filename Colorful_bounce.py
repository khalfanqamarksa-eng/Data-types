import pygame
import random
pygame.init()
pygame.display.set_caption('Colorful bounce')
sprite_color_change_event= pygame.USEREVENT +1
background_color_change_event=pygame.USEREVENT+2
#Sprite Colors
blue = pygame.Color ('blue')
red = pygame.Color ('red')
green = pygame.Color ('yellow')

#Background Colors

orange = pygame.Color ('orange')
pink = pygame.Color ('pink')
purple = pygame.Color ('purple')
lightblue = pygame.Color ('lightblue')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(color)

        self.rect=self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1,1])]

    def update(self):
        self.rect.mov_ip(self.velocity)
        boundary_hit= False
        self.velocity[0] = -self.velocity[0]
        boundary_hit = True
        if self.rect.top <=0 or self.rect.bottom >=400:
            self.velocity[1]= -self.velocity[1]
            boundary_hit= True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(background_color_change_event))

    def Color_change(self):
        self.image.fill(random.choice([blue, red, green]))
    def background_color_Change():
        global bg_color
        bg_color = random.choice ([orange, purple, lightblue, pink])

    all_sprites_list=pygame.sprite.Group()
    sprite1= (orange, 20, 20)
    sprite1.rect.x= random.randit(0,480)
    sprite1.rect.y= random.randit(0, 370)
    all_sprites_list.add(sprite1)

    screen = pygame.display.set_mode((500,400))
    bg_color = blue
    screen.fill(bg_color)