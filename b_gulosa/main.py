from b_gulosa.busca_gulosa import BuscaGulosa
from grafo import Grafo

grafo = Grafo()
buscaGulosa = BuscaGulosa(grafo.curitiba)
buscaGulosa.buscar(grafo.porto_uniao)
