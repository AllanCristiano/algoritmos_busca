
from adjacencia import Adjacencia
from vertice import Vertice


class Grafo:
    porto_uniao = Vertice("Porto União", 203)
    paulo_frontin = Vertice("Paulo Frontin", 172)
    canoinhas = Vertice("Canoinhas", 141)
    tres_barras = Vertice("Três Barras", 131)
    sao_mateus_do_sul = Vertice("São Mateus do Sul", 123)
    irati = Vertice("Irati", 139)
    curitiba = Vertice("Curitiba", 0)
    palmeira = Vertice("Palmeira", 59)
    mafra = Vertice("Mafra", 94)
    campo_largo = Vertice("Campo Largo", 27)
    balsa_nova = Vertice("Balsa Nova", 47)
    lapa = Vertice("Lapa", 74)
    tijuca_do_sul = Vertice("Tijuca do Sul", 56)
    araucaria = Vertice("Araucária", 23)
    sao_jose_dos_pinhais = Vertice("São Jose dos Pinhas", 13)
    contenda = Vertice("Contenda", 39)
    
    # porto uniao adjacencias
    porto_uniao.adcionar_adjacecias(Adjacencia(paulo_frontin, 46))
    porto_uniao.adcionar_adjacecias(Adjacencia(sao_mateus_do_sul, 87))
    canoinhas.adcionar_adjacecias(Adjacencia(canoinhas, 78))
    