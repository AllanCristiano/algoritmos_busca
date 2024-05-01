from insere_vetor_gulosa import OrdenaVetor


class BuscaGulosa:
    def __init__(self, obejetivo) -> None:
        self.objetivo = obejetivo
        self.encontrado = False

    def buscar(self, atual):
        print("----------------")
        print(f'Atual: {atual.rotulo}')
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor = OrdenaVetor(len(atual.adjacencias))
            for i in atual.adjacencias:
                if not i.vertice.visitado:
                    i.vertice.visitado = True
                    vetor.insere(i.vertice)
            vetor.imprime()
            if vetor.valores[0] is not None:
                self.buscar(vetor.valores[0])