import numpy as np


class OrdenaAEstrela:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1

        #   iniciando valores vazios
        self.valores = np.empty(capacidade, dtype=object)

    def insert(self, adjacente):
        if self.ultima_posicao == self.capacidade -1:
            print("Vetor com Capacidade maxima")
            return
        else:
            posicao = 0
            for i in range(self.capacidade+1):
                posicao = i
                if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                    break
                if self.ultima_posicao == i:
                    posicao = i + 1

            x = self.ultima_posicao
            while x >= posicao:
                self.valores[x+1] = self.valores[x]
                x -= 1
            self.valores[posicao] = adjacente
            self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, ' - ',
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_aestrela)


