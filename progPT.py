__autor__ = "Jivaldo Da Cruz"

#
# um programa simples para usar umas funções e métodos em potuguês
#

class letras:
    def __init__(self, valor):
        self.valor = valor

    #saber tamanho da letra
    def valoresTotal(self):
        try:
            print(len(self.valor))
            return False
        except TypeError:
            print("Este método não aceita valores do tipo int()")

    #dividir frase/palavra em forma da lista, só separando
    def dividir(self):
        try:
            print((self.valor).split())
        except AttributeError:
            print("Este método não aceita valores do tipo int()")

    #letra maiúscula
    def maiucula(self):
        try:
            print((self.valor).upper())
        except AttributeError:
            print("Este método não aceita valores do tipo int()")
    #letra minuscula
    def minuscula(self):
        try:
            print((self.valor).upper())
        except AttributeError:
            print("Este método não aceita valores do tipo int()")

    #procurar letras
    def procurar(self, procurarLetras):
        try:
            contador = 0
            for x in self.valor:
                print(contador, x, procurarLetras)
                if(x == procurarLetras):
                    contador += 1
            print(f"Foram encontrado {contador} letra/as com {procurarLetras}.")
        except TypeError:
            print("Este método não aceita valores do tipo int()")
    #encontrar cada letra com sua posição
    def posicao(self, posicaoLetras):
        asPosicao = []
        contador = 0
        for x in self.valor:
            if(x == posicaoLetras):
                asPosicao.append(contador)
            contador += 1
        if(asPosicao == []):
            print("Não existe nenhuma letra desse tipo no parâmetro.")
        else:
            print(f"As letras foram encontadas nas posições: {asPosicao}")

class numeros:
    import math
    def __init__(self, num):
        self.num = num
    #os 4 tipos de calculos principal, para funcionar temos que usar uma lista []
    def somar(self, lista = []):
        cont = 0
        soma = 0
        if(lista == []):
            print("A lista está vazia!")
        else:
            while cont < len(lista):
                soma += lista[cont]
                cont += 1
            print(f"A soma é: {soma}")
    def subtrair(self, lista = []):
        try:
            cont = 1
            sub = lista[0]
            while cont < len(lista):
                sub -= lista[cont]
                cont += 1
            print(f"A subtração é: {sub}")
        except IndexError:
            print("A lista está vazia!")
    def dividir(self, lista = []):
        try:
            cont = 1
            div = lista[0]
            while cont < len(lista):
                div /= lista[cont]
                cont += 1
            print(f"A divisão é: {div}")
        except IndexError:
            print("A lista está vazia!")
    def multiplicar(self, lista = []):
        try:
            cont = 1
            mul = lista[0]
            while cont < len(lista):
                mul *= lista[cont]
                cont += 1
            print(f"A multiplicação é: {mul}")
        except IndexError:
            print("A lista está vazia!")
