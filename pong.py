import turtle
import time
import random
import winsound

# draw screen
screen = turtle.Screen()
screen.title("DEE-Pong")
screen.bgcolor("#181818")
screen.bgpic("assets/bg_menu.gif")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)
paddle_1.hideturtle()

# draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)
paddle_2.hideturtle()

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3
ball.hideturtle()

# score
score_1 = 0
score_2 = 0

# pause and quit controls
game_paused = False
game_cycle = True

# buffs controls
buff_timer_paddle1 = 0
buff_timer_paddle2 = 0
nerf_timer_paddle1 = 0
nerf_timer_paddle2 = 0
size_paddle_1 = 50
size_paddle_2 = 50
spawn_locked = True
last_touch = 0

# draw buffs
buff = turtle.Turtle()
buff.speed(0)
buff.penup()
buff.goto(0, -800)
buff.getscreen().register_shape("assets/lucky_block.gif")
buff.shape('assets/lucky_block.gif')
buff.color("#188ea1")
buff.shapesize(stretch_wid=3, stretch_len=3)

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, -260)

# progress bar
progress_player_1 = turtle.Turtle()
progress_player_1.color("#188ea1")
progress_player_1.shape("square")
progress_player_1.penup()
progress_player_1.goto(-142, -274)
progress_player_1.shapesize(stretch_len=0.6, stretch_wid=0.6)
progress_player_1.pendown()
progress_player_1.pensize(3)
progress_player_1.hideturtle()

# progress bar
progress_player_2 = turtle.Turtle()
progress_player_2.color("#a1180e")
progress_player_2.shape("square")
progress_player_2.penup()
progress_player_2.goto(125, -274)
progress_player_2.shapesize(stretch_len=0.6, stretch_wid=0.6)
progress_player_2.pendown()
progress_player_2.right(180)
progress_player_2.pensize(3)
progress_player_2.hideturtle()


# score
def point_score(player_name):
    global spawn_locked
    global last_touch
    last_touch = 0
    spawn_locked = reset_buff()
    global score_1
    global score_2
    ball.goto(0, 0)
    ball_start_random = random.randint(0, 1)
    # random side that balls start to walk
    if ball_start_random == 0:
        ball.dx = 3
    else:
        ball.dx = -3
    if player_name == 1:
        score_1 += 1
        progress_player_1.forward(22)
    else:
        score_2 += 1
        progress_player_2.forward(22)
    hud.clear()
    hud.write("{}   {}".format(score_1, score_2), align="center",
              font=("Press Start 2P", 24, "normal"))
    winsound.PlaySound("assets/point.wav", winsound.SND_ASYNC)


# movement
def move_up_paddles(paddle):
    y = paddle.ycor()
    if y < 250:
        y += 30
        if not (y < 250):
            y = 250
    else:
        y = 250
    paddle.sety(y)


def move_down_paddles(paddle):
    y = paddle.ycor()
    if y > -250:
        y += -30
        if not (y > -250):
            y = -250
    else:
        y = -250
    paddle.sety(y)


def paddle_1_up():
    move_up_paddles(paddle_1)


def paddle_1_down():
    move_down_paddles(paddle_1)


def paddle_2_up():
    move_up_paddles(paddle_2)


def paddle_2_down():
    move_down_paddles(paddle_2)


# reset buff
def reset_buff():
    buff.goto(0, -800)
    buff.sety(-800)
    buff.setx(0)
    return True


# end buff
def end_buff(num_paddle):
    global size_paddle_1
    global size_paddle_2
    if num_paddle == 1:
        paddle_1.shapesize(stretch_wid=5, stretch_len=1)
        size_paddle_1 = 50
    else:
        size_paddle_2 = 50
        paddle_2.shapesize(stretch_wid=5, stretch_len=1)


# buff paddle (size_up)
def call_buff1():
    global size_paddle_1
    global size_paddle_2
    global buff_timer_paddle1
    global buff_timer_paddle2
    # size paddle expand
    if last_touch == 1:
        size_paddle_1 = 80
        paddle_1.shapesize(stretch_wid=8, stretch_len=1)
        buff_timer_paddle1 = 28
    elif last_touch == 2:
        size_paddle_2 = 80
        paddle_2.shapesize(stretch_wid=8, stretch_len=1)
        buff_timer_paddle2 = 28


# nerf paddle (size_down)
def call_nerf1():
    global size_paddle_1
    global size_paddle_2
    global buff_timer_paddle1
    global buff_timer_paddle2
    global nerf_timer_paddle1
    global nerf_timer_paddle2
    # size paddle reduce
    if last_touch == 1:
        size_paddle_1 = 30
        paddle_1.shapesize(stretch_wid=3, stretch_len=1)
        buff_timer_paddle1 = 0.5
        nerf_timer_paddle1 = 20
    elif last_touch == 2:
        size_paddle_2 = 30
        paddle_2.shapesize(stretch_wid=3, stretch_len=1)
        buff_timer_paddle2 = 0.5
        nerf_timer_paddle2 = 20


# Win Game
def end_game(winner):
    global spawn_locked
    global game_paused
    # clear screen
    paddle_2.goto(1800, paddle_2.ycor())
    paddle_1.goto(1800, paddle_1.ycor())
    ball.goto(1800, ball.ycor())
    game_paused = False
    hud.goto(0, -20)
    hud.clear()
    screen.bgpic("assets/victory.gif")
    # winner test
    if winner == 1:
        hud.write("   Player 1 Wins!!\n Press \"r\" to continue",
                  align="center", font=("Press Start 2P", 16, "normal"))
        hud.goto(0, -260)
        hud.write("press \"q\" to quit", align="center",
                  font=("Press Start 2P", 12, "normal"))
    elif winner == 2:
        hud.write("   Player 2 Wins!!\n\nPress \"r\" to continue", align="center",
                  font=("Press Start 2P", 16, "normal"))
        hud.goto(0, -260)
        hud.write("press \"q\" to quit", align="center",
                  font=("Press Start 2P", 12, "normal"))


# start game
def start():
    winsound.PlaySound("assets/coin.wav", winsound.SND_FILENAME)
    global game_paused
    game_paused = True
    screen.bgpic("assets/bg.gif")
    paddle_1.showturtle()
    paddle_2.showturtle()
    ball.showturtle()
    hud.write("0   0", align="center", font=("Press Start 2P", 24, "normal"))
    progress_player_2.showturtle()
    progress_player_1.showturtle()


# quit game
def close_game():
    global game_cycle
    global game_paused
    if not game_paused:
        winsound.PlaySound("assets/loose.wav", winsound.SND_FILENAME)
        game_cycle = False


# reset game
def reset_game():
    global game_paused
    if not game_paused:
        game_paused = True
        global score_2
        score_2 = 0
        global score_1
        score_1 = 0
        ball.dx = -3
        ball.goto(0, 0)
        progress_player_1.goto(-142, -274)
        progress_player_1.clear()
        progress_player_2.goto(125, -274)
        progress_player_2.clear()
        paddle_2.goto(350, paddle_2.ycor())
        paddle_1.goto(-350, paddle_1.ycor())
        hud.goto(0, -260)
        hud.clear()
        hud.write("0   0", align="center",
                  font=("Press Start 2P", 24, "normal"))
        screen.bgpic("assets/bg.gif")


# keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")
screen.onkeypress(reset_game, "r")
screen.onkeypress(start, "p")
screen.onkeypress(close_game, "q")

# start the game_cycle
while game_cycle:
    fps = 1 / 60
    time.sleep(fps)
    screen.update()
    # timer buff paddle 1
    buff_timer_paddle1 -= 0.0009
    if buff_timer_paddle1 < 0:
        buff_timer_paddle1 = 1
        end_buff(1)

    # timer buff paddle 2
    buff_timer_paddle2 -= 0.0009
    if buff_timer_paddle2 < 0:
        buff_timer_paddle2 = 1
        end_buff(2)

    # time nerf paddle 1
    nerf_timer_paddle1 -= 0.0009
    if nerf_timer_paddle1 < 0:
        nerf_timer_paddle1 = 1
        end_buff(1)

    # timer nerf paddle 2
    nerf_timer_paddle2 -= 0.0009
    if nerf_timer_paddle2 < 0:
        nerf_timer_paddle2 = 1
        end_buff(2)

    # buff random
    buffTry = random.randint(0, 1000)
    if buffTry == 150 and spawn_locked and not (last_touch == 0):
        # Select the buff
        buffX = random.randint(-200, 200)
        buffY = random.randint(-200, 200)
        buff.setx(buffX)
        buff.sety(buffY)
        buff.goto(buffX, buffY)
        spawn_locked = False

    if game_paused:
        # ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # collision with the upper wall
        if ball.ycor() > 290:
            winsound.PlaySound("assets/bounce.wav", winsound.SND_ASYNC)
            ball.sety(290)
            ball.dy *= -1

        # collision with lower wall
        if ball.ycor() < -290:
            winsound.PlaySound("assets/bounce.wav", winsound.SND_ASYNC)
            ball.sety(-290)
            ball.dy *= -1

        # collision with right wall
        if ball.xcor() > 390:
            point_score(1)

        # collision with left wall
        if ball.xcor() < -390:
            point_score(2)

        # collision with the paddle 1
        if (ball.xcor() < -330 and not (ball.xcor() < -340)) and paddle_1.ycor()\
                + size_paddle_1 > ball.ycor() > paddle_1.ycor() - size_paddle_1:
            ball.goto(-330, ball.ycor())
            ball.dx *= -1.1
            last_touch = 1
            winsound.PlaySound("assets/bounce.wav", winsound.SND_ASYNC)
        elif paddle_1.ycor() + size_paddle_1 > ball.ycor() > \
                paddle_1.ycor() - size_paddle_1 and ball.xcor() < -330:
            ball.dx *= -1.1
            ball.dy *= -1
            last_touch = 1
            if ball.xcor() < -345:
                ball.dx *= -1

        # collision with the paddle 2
        if (ball.xcor() > 330 and not (ball.xcor() > 340)) and paddle_2.ycor()\
                + size_paddle_2 > ball.ycor() > paddle_2.ycor() - size_paddle_2:
            ball.goto(330, ball.ycor())
            ball.dx *= -1.1
            last_touch = 2
            winsound.PlaySound("assets/bounce.wav", winsound.SND_ASYNC)
        elif paddle_2.ycor() + size_paddle_2 > ball.ycor() > \
                paddle_2.ycor() - size_paddle_2 and ball.xcor() > 330:
            ball.dx *= -1.1
            ball.dy *= -1
            last_touch = 2
            winsound.PlaySound("assets/bounce.wav", winsound.SND_ASYNC)
            if ball.xcor() > 345:
                ball.dx *= -1

        if 10 >= ball.dx >= -10:
            ball.color("#FFFFFF")
        else:
            ball.color("#FFFF89")
            if ball.dx > 12 or ball.dx < -12:
                ball.color("#FF9900")
                if ball.dx > 15 or ball.dx < -15:
                    ball.color("#FF2300")
                elif ball.dx >= 15 or ball.dx <= -15:
                    ball.dx = 15
        # collision with buff
        if (ball.xcor() + 30 >= buff.xcor() >= ball.xcor() - 30) and \
                (ball.ycor() + 30 >= buff.ycor() >= ball.ycor() - 30):
            spawn_locked = reset_buff()

            rand_buff = random.randint(0, 1)
            if rand_buff == 0 or rand_buff == 1:
                if rand_buff == 0:
                    winsound.PlaySound("assets/coin.wav", winsound.SND_ASYNC)
                    call_buff1()
                else:
                    winsound.PlaySound("assets/loose.wav", winsound.SND_ASYNC)
                    call_nerf1()

        # end game
        if score_1 >= 5 or score_2 >= 5:
            if score_1 >= 5:
                end_game(1)
            else:
                end_game(2)
