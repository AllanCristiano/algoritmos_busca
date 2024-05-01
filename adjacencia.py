class Adjacencia:
    def __init__(self, vertice, custo) -> None:
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = self.custo + vertice.distancia_objetivo
