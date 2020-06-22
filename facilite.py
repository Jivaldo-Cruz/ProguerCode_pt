__autor__ = "Jivaldo Da Cruz"

#
# um programa simples para usar umas funções e métodos já preparada
#

##########################################################################################################
#                                          classe de letras                                              #
##########################################################################################################
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
    #pegar todas palavras com mesma inicias e coloca numa lista
    def iniciasIguais(self, frase):#para melhorar efeito usa uma frase no argumento
        import re
        com = re.findall(r"\bf[a-z]*", frase)
        print(com)
    #retira as mesma palvras juntas e deixa só uma na frase
    def retirarIguais(self, frase):#para melhorar efeito usa uma frase no argumento
        import re
        com = re.sub(r"(\b[a-z]+) \1", r"\1", frase)
        print(com)
##########################################################################################################
#                                          classe de número                                              #
##########################################################################################################
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
    #factiorial de um número
    def factorial(self, num):
        total = 1
        try:
            for x in range(num):
                total *= (num - x)
            print(total)
        except TypeError:
            print("Não aceitamos strings nem floats!")
    #primo e impar
    def primo(self, num):
        print("Os números primos")
        try:
            for x in range(num):
                if(x % 2 == 0):
                    print(x)
        except TypeError:
            print("Obrigatorio números inteiros!")
    def impar(self, num):
        print("Os números impares")
        try:
            for x in range(num):
                if(x % 2 == 0):
                    pass
                else:
                    print(x)
        except TypeError:
            print("Obrigatorio números inteiros!")
    #tipo de número
    def tipoNumero(self, num):
        if(type(num) == type(int())):
            print(f"{num} é do tipo int() -> número inteiros")
        elif(type(num) == type(float())):
            print(f"{num} é de tipo float() -> número de tipo decimal")
        elif(type(num) == type(str())):
            print(f"{num} é do tipo str()(a-z) e não aceitamos letras!")
