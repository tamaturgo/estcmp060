import pygame
import time


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.isAnimated = False
        self.sprites = []
        self.posx = pos_x
        self.posy = pos_y
        self.isRunning = False
        self.spriteSpeed = 0.2
        self.moveSpeed = 1
        self.sprites.append(pygame.image.load("Mario Walk/wsprite_0.png").convert())
        self.sprites.append(pygame.image.load("Mario Walk/wsprite_1.png").convert())
        self.sprites.append(pygame.image.load("Mario Walk/wsprite_2.png").convert())
        self.sprites.append(pygame.image.load("Mario Walk/wsprite_3.png").convert())
        self.sprites.append(pygame.image.load("Mario Walk/wsprite_4.png").convert())
        self.sprites.append(pygame.image.load("Mario Walk/wsprite_5.png").convert())
        self.sprites.append(pygame.image.load("Mario Walk/wsprite_6.png").convert())
        self.sprites.append(pygame.image.load("Mario Walk/wsprite_7.png").convert())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def animate(self, value):
        self.isAnimated = value

    def update(self):

        if self.isAnimated:
            self.current_sprite += self.spriteSpeed
            if self.isRunning:
                self.spriteSpeed = 0.34
                self.moveSpeed = 8
            else:
                self.spriteSpeed = 0.2
                self.moveSpeed = 1
            if (self.current_sprite >= len(self.sprites)):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.current_sprite = 4
            self.image = self.sprites[int(self.current_sprite)]


pygame.init()
screen = pygame.display.set_mode((1000, 600))
moving_sprites = pygame.sprite.Group()
player = Player(0, 150)
moving_sprites.add(player)
fonte = pygame.font.Font("font_game.ttf", 24)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.animate(True)
            if event.key == pygame.K_b:
                player.isRunning = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_b:
                player.isRunning = False
            else:
                player.animate(False)


    if player.isAnimated: player.posx += player.moveSpeed

    screen.fill((0, 0, 0))
    _text = fonte.render("Press D to move and B to run",
                                             True, (255,255,255))
    _text_rect = _text.get_rect()
    _text_rect.center = (500, 100)
    screen.blit(_text, _text_rect)
    screen.blit(player.sprites[int(player.current_sprite)], (player.posx, player.posy))
    moving_sprites.update()
    pygame.display.flip()
    time.sleep(1 / 60)
