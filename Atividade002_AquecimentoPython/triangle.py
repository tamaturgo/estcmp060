import turtle

# Criando Tela e Caneta
tela = turtle.Screen()
tela.bgcolor('light green')
caneta = turtle.Turtle()

def triangle(posX, posY):    
    # Movendo a caneta para a posição do click
    caneta.penup()
    caneta.goto(posX, posY)
    caneta.pendown()

    # Desenhando Trinagulo
    for i in range(3):
        caneta.forward(100)
        caneta.left(120)
        caneta.forward(100)

# Identifica o evento do click do mouse
turtle.onscreenclick(triangle, 1,)
turtle.listen()

# Pausa o programa.
turtle.done()
