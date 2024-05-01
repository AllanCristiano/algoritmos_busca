class Vertice:
    def __init__(self, rotulo, distancia_objetivo) -> None:
        self.rotulo = rotulo
        self.distancia_objetivo = distancia_objetivo
        self.visitado = False
        self.adjacencias = []
    
    def adcionar_adjacecias(self, adjacente) -> None:
        self.adjacencias.append(adjacente)
    
    def mostrar_adjacencia(self) -> None:
        for i in self.adjacencias:
            print(f"Rotulo: {i.vertice.rotulo}, Custo: {i.custo}")