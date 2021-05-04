import turtle


# Função Principal
def treeY(tamanho, level):

    if level > 0:
        turtle.colormode(255)
        # Selecionando a cor verde para o ultimo level
        caneta.pencolor(0, 255//level, 0)

        #desenhando a base
        caneta.forward(tamanho)
        caneta.right(angulo)

        # Criando ramificações da arvore
        treeY(0.8 * tamanho, level-1)
        caneta.pencolor(0, 255//level, 0)

        caneta.left(2 * angulo)
        treeY(0.8 * tamanho, level-1)

        caneta.pencolor(0, 255//level, 0)
        caneta.right(angulo)
        caneta.forward(-tamanho)


# Angulo de inclinação entre as ramificações
angulo = 30

# Interação com o Usuário
lvl = int(input("Digite quantas ramificações sua árvore terá (recomendamos"+
                " no máximo 15 ramificações): "))

# Criando e definindo velocidade da caneta e virando ela para cima 
caneta = turtle.Turtle()
caneta.speed('fastest')
caneta.right(-90)

# Inicializando a função principal
treeY(50, lvl)

# Pausar programa ao fim da sua execução
turtle.done()