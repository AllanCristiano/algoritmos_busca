from insere_vetor_a_estrela import OrdenaAEstrela


class BuscaAEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.atingido = False

    def search(self, atual):
        print("-----------------")
        print(f"Atual: {atual.rotulo}")
        atual.visitado = True

        if atual == self.objetivo:
            self.atingido = True
        else:
            vetor_ordenado = OrdenaAEstrela(len(atual.adjacencias))
            for i in atual.adjacencias:
                if i.vertice.visitado is False:
                    i.vertice.visitado = True
                    vetor_ordenado.insert(i)
            vetor_ordenado.imprime()

            if vetor_ordenado.get_item() is not None:
                self.search(vetor_ordenado.get_item().vertice)
