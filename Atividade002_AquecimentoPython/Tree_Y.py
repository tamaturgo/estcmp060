from turtle import *


# Definindo velocidade da caneta e virando ela para cima 
speed('fastest')
rt(-90)
# Angulo de inclinação entre as ramificações
angulo = 30

def treeY(tamanho, level):

    if level > 0:
        colormode(255)
        # Selecionando a cor verde para o ultimo level
        pencolor(0, 255//level, 0)

        #desenhando a base
        fd(tamanho)
        rt(angulo)

        # Criando ramificações da arvore
        treeY(0.8 * tamanho, level-1)
        pencolor(0, 255//level, 0)

        lt(2 * angulo)
        treeY(0.8 * tamanho, level-1)

        pencolor(0, 255//level, 0)
        rt(angulo)
        fd(-tamanho)


# Interação com o Usuário
lvl = int(input("Digite quantas ramificações sua árvore terá (recomendamos"+
                " no máximo 15 ramificações): "))

# Inicializando a função principal
treeY(50, lvl)