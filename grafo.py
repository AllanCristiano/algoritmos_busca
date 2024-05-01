
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
    porto_uniao.adcionar_adjacecias(Adjacencia(canoinhas, 78))
    
    # paulo frontin adjacencias
    paulo_frontin.adcionar_adjacecias(Adjacencia(porto_uniao, 46))
    paulo_frontin.adcionar_adjacecias(Adjacencia(irati, 75))
    
    # são mateus do sul adjacencias
    sao_mateus_do_sul.adcionar_adjacecias(Adjacencia(porto_uniao, 87))
    sao_mateus_do_sul.adcionar_adjacecias(Adjacencia(tres_barras, 43))
    sao_mateus_do_sul.adcionar_adjacecias(Adjacencia(palmeira, 77))
    sao_mateus_do_sul.adcionar_adjacecias(Adjacencia(lapa, 60))
    sao_mateus_do_sul.adcionar_adjacecias(Adjacencia(irati, 57))
    
    # canoinha adjacencias
    canoinhas.adcionar_adjacecias(Adjacencia(porto_uniao, 78))
    canoinhas.adcionar_adjacecias(Adjacencia(tres_barras, 12))
    canoinhas.adcionar_adjacecias(Adjacencia(mafra, 66))
    
    # irati adjacencias
    irati.adcionar_adjacecias(Adjacencia(paulo_frontin, 75))
    irati.adcionar_adjacecias(Adjacencia(sao_mateus_do_sul, 57))
    irati.adcionar_adjacecias(Adjacencia(palmeira, 75))
    
    # tres barras adjacencias
    tres_barras.adcionar_adjacecias(Adjacencia(canoinhas, 12))
    tres_barras.adcionar_adjacecias(Adjacencia(sao_mateus_do_sul, 43))
    
    # palmeiras adjacencias
    palmeira.adcionar_adjacecias(Adjacencia(irati, 75))
    palmeira.adcionar_adjacecias(Adjacencia(sao_mateus_do_sul, 77))
    palmeira.adcionar_adjacecias(Adjacencia(campo_largo, 29))
    
    # lapa adjacencias
    lapa.adcionar_adjacecias(Adjacencia(sao_mateus_do_sul, 60))
    lapa.adcionar_adjacecias(Adjacencia(contenda, 26))
    lapa.adcionar_adjacecias(Adjacencia(mafra, 57))
    
    
    # mafra adjacencias
    mafra.adcionar_adjacecias(Adjacencia(canoinhas, 66))
    mafra.adcionar_adjacecias(Adjacencia(lapa, 57))
    mafra.adcionar_adjacecias(Adjacencia(tijuca_do_sul, 99))
    
    # campo largo 
    campo_largo.adcionar_adjacecias(Adjacencia(palmeira, 55))
    campo_largo.adcionar_adjacecias(Adjacencia(balsa_nova, 22))
    campo_largo.adcionar_adjacecias(Adjacencia(curitiba, 29))
    
    # contenda
    contenda.adcionar_adjacecias(Adjacencia(lapa, 26))
    contenda.adcionar_adjacecias(Adjacencia(balsa_nova, 19))
    contenda.adcionar_adjacecias(Adjacencia(araucaria, 18))
        
    # tijuca do sul
    tijuca_do_sul.adcionar_adjacecias(Adjacencia(mafra, 99))
    tijuca_do_sul.adcionar_adjacecias(Adjacencia(sao_jose_dos_pinhais, 49))#
    
    # balsa nova
    balsa_nova.adcionar_adjacecias(Adjacencia(contenda, 19))
    balsa_nova.adcionar_adjacecias(Adjacencia(campo_largo, 22))
    balsa_nova.adcionar_adjacecias(Adjacencia(curitiba, 51))
    
    # araucaria
    araucaria.adcionar_adjacecias(Adjacencia(contenda, 18))
    araucaria.adcionar_adjacecias(Adjacencia(curitiba, 37))
    
    # sao jose dos pinhais
    sao_jose_dos_pinhais.adcionar_adjacecias(Adjacencia(tijuca_do_sul, 49))
    sao_jose_dos_pinhais.adcionar_adjacecias(Adjacencia(curitiba, 15))
    
    # curitiba    
    curitiba.adcionar_adjacecias(Adjacencia(campo_largo, 29))
    curitiba.adcionar_adjacecias(Adjacencia(balsa_nova, 51))
    curitiba.adcionar_adjacecias(Adjacencia(araucaria, 37))
    curitiba.adcionar_adjacecias(Adjacencia(sao_jose_dos_pinhais, 15))