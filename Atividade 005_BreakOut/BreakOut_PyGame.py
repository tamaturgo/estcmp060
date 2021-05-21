import pygame
# Bricks Size 4x8 -> 32x64
# Player size 4x16 -> 32x128

# Screen set
pygame.init()
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
screen_bg = pygame.image.load("assets/atari_screen.png")
game_clock = pygame.time.Clock()
game_cycle = True

# Player
player = pygame.image.load("assets/player.png")
player_move_left = False
player_move_right = False
player_x = 640
# Ball
ball = pygame.image.load("assets/ball.png")
ball_dx = 5
ball_dy = 10
ball_x = 640
ball_y = 360

# Game Variables
cols = 13
rows = 6
brick_height = 32
brick_width = 64

brick_list = []
brick_color_list = [(200, 73, 70),(197, 109, 59), (180, 123, 46), (163, 162, 43), (70, 172, 65),
                    (62, 72, 197)]

for row in range(rows):
    for col in range(cols):
        x = 224 + (brick_width * col)
        y = 154 + (brick_height * row)
        block = pygame.Rect(x, y, brick_width, brick_height)
        brick_list.append(block)

pygame.mouse.set_visible(False)

while game_cycle:
    # End Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False

    # Player Movement
    player_XY = pygame.mouse.get_pos()

    player_x = player_XY[0] // 1
        
    
    if player_x > 905:
        player_x = 905
    if player_x < 224:
        player_x = 224

    # Ball Movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Colliders
    if ball_x < 224:
        ball_dx *= -1
    if ball_x > 1040:
        ball_dx *= -1
    if ball_y < 104:
        ball_dy *= -1
    if ball_y > 720:
        # YOU LOSE
        ball_dy *= -1

    # Collider with Player
    if ball_y > 658 and not (ball_y > 700):
        if player_x < ball_x + 150:
            if player_x + 150 > ball_x:
                ball_y = 658
                ball_dy *= -1

    # Screen update
    screen.fill((0, 0, 0))
    screen.blit(screen_bg, (0, 0))
    screen.blit(player, (player_x, 680))
    screen.blit(ball, (ball_x, ball_y))

    color_try = 0
    color_row = 0
    # Bricks
    for block in brick_list:
        # Select Color
        if color_row > 5:
            color_row = 0
        # Draw Bricks
        pygame.draw.rect(screen, brick_color_list[color_row], block)

        # Count color at List
        color_try += 1
        if (color_try // 13) == 1:
            color_row += 1
            color_try = 0

    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
