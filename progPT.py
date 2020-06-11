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
    def __init__(self, num):
        self.num = num
    #terá mais atualizações em breve
