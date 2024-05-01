import numpy as np

class OrdenaVetor:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.final = -1
        
        self.valores = np.empty(capacidade, dtype=object)
        
    def insere(self, adjacente) -> None:
        if self.final == self.capacidade -1:
            print("Capacidade maxima")
            return
        
        posicao = 0         
        for i in range(self.capacide + 1):
            posicao = i
            if posicao == self.final:
                posicao = i + 1
        
        x = self.final
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        
        self.valores[posicao] = adjacente
        self.final += 1
        
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)