import pygame
import time

rotation = False
class PlayerJump(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.isAnimated = False
        self.isFall = False
        self.sprites = []
        self.posx = pos_x
        self.posy = pos_y
        self.sprites.append(pygame.image.load("Mario Jump/sprite_0.png").convert())
        self.sprites.append(pygame.image.load("Mario Jump/sprite_1.png").convert())
        self.sprites.append(pygame.image.load("Mario Jump/sprite_2.png").convert())
        self.sprites.append(pygame.image.load("Mario Jump/sprite_3.png").convert())
        self.sprites.append(pygame.image.load("Mario Jump/sprite_4.png").convert())
        self.sprites.append(pygame.image.load("Mario Jump/sprite_5.png").convert())
        self.sprites.append(pygame.image.load("Mario Jump/sprite_6.png").convert())
        self.sprites.append(pygame.image.load("Mario Jump/sprite_7.png").convert())
        self.sprites.append(pygame.image.load("Mario Jump/sprite_8.png").convert())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [pos_x, pos_y]

    def animate(self, value):
        self.isAnimated = value
        self.current_sprite = 0

    def update(self):

        if self.isAnimated:
            self.current_sprite += 0.02
            if(self.current_sprite >= 6):
                self.isFall = True
            if (self.current_sprite >= len(self.sprites)):
                self.current_sprite = 0
                self.isAnimated = False
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
            self.isAnimated = False

pygame.init()
screen = pygame.display.set_mode((1000, 600))
moving_sprites = pygame.sprite.Group()
player = PlayerJump(0, 350)
initial_y = 350
moving_sprites.add(player)
fonte = pygame.font.Font("font_game.ttf", 24)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.animate(True)

    i = 5
    while player.isAnimated:
        player.posy -= 1*i
        i -= 0.23
        player.posx -= 1 * i
        if i < 0:
            i = 0
        if player.isFall:
            while initial_y > player.posy:
                j = 0.2

                print(initial_y)
                print(player.posy)
                player.posy += 1 * j
                j += 0.34
                if j > 2:
                    j = 2
            player.isFall = False
        screen.fill((0, 0, 0))
        screen.blit(player.sprites[int(player.current_sprite)], (player.posx, player.posy))
        moving_sprites.update()
        pygame.display.flip()

    screen.fill((0, 0, 0))
    _text = fonte.render("Press SPACE to Jump",
                         True, (255, 255, 255))
    _text_rect = _text.get_rect()
    _text_rect.center = (500, 100)
    screen.blit(_text, _text_rect)
    screen.blit(player.sprites[int(player.current_sprite)], (player.posx, player.posy))
    moving_sprites.update()
    pygame.display.flip()
    time.sleep(1 / 60)
