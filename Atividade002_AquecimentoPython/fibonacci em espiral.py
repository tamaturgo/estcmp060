import turtle
import math


def calc(quantidadeFibo):
    numAnterior = 0
    numAtual = 1
    sqrNumAnterior = 0
    sqrNumAtual = 1
    aux = 0
    
    #Gerando primeiro quadrado
    pen.forward(numAtual * scale)
    pen.left(90)
    pen.forward(numAtual * scale)
    pen.left(90)
    pen.forward(numAtual * scale)
    pen.left(90)
    pen.forward(numAtual * scale)
    #Atualizando a primeira série de Fibonacci
    aux = numAnterior + numAtual
    numAnterior = numAtual
    numAtual = aux  

    #Gerar as outras séries
    for i in range(1, quantidadeFibo):
        pen.backward(numAnterior * scale)
        pen.right(90)
        pen.forward(numAtual * scale)
        pen.left(90)
        pen.forward(numAtual * scale)
        pen.left(90)
        pen.forward(numAtual * scale)
        
        #Atualiza Fibonacci
        aux = numAnterior + numAtual
        numAnterior = numAtual
        numAtual = aux    


    PI_VALUE = math.pi
    
    #Resetar caneta
    pen.penup()
    pen.setposition(scale, 0)
    pen.seth(0)
    pen.pendown()
    pen.pencolor("red")

    #Gerar a espiral que percorre os quadrados
    pen.left(90)
    for i in range(quantidadeFibo):
        print(sqrNumAtual)

        #Calcula o próximmo movimento 
        fdwd = PI_VALUE * sqrNumAtual * scale / 2
        fdwd /= 90

        for j in range(90):
            pen.forward(fdwd)
            pen.left(1)
        
        #Atualiza o fibonacci    
        aux = sqrNumAnterior
        sqrNumAnterior = sqrNumAtual
        sqrNumAtual = aux + sqrNumAtual
        
#Interações com o Usuário
quantidadeFibo = int(input("Digite o número de repetições (Necessário que "+
                           "seja > 1): "))
scale = int(input("Digite a escala de visualização: "))

if(quantidadeFibo > 1):
    #Inicializa a tela e a Função principal
    pen = turtle.Turtle()
    pen.speed(100)
    calc(quantidadeFibo)
else: 
    print("Digite valores maiores que 1.")

#Pause
turtle.done()
