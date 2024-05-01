import numpy as np


class OrdenaVetor:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.final = -1

        self.valores = np.empty(self.capacidade, dtype=object)

    def insere(self, vertice) -> None:

        if self.final== self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.final + 1):
            posicao = i
            if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
                break
            if i == self.final:
                posicao = i + 1
        x = self.final
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = vertice
        self.final += 1

    def imprime(self):
        if self.final == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.final + 1):
                print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)
