marcas_de_roupas =[]
print (marcas_de_roupas)
# uma lista vazia que não retorna nada 

marcas_de_roupas.append("nike")
print(marcas_de_roupas)
marcas_de_roupas.append("adidas")
print(marcas_de_roupas)
# neste caso eu não preciso voltar e incluir no conchete, somente digito .append 
# e ele inclui os item na lista, só incluir um por vez

for num in range (1,4):
    resposta = input("digite uma marca de roupa:  ")
    marcas_de_roupas.append(resposta)

    print(marcas_de_roupas)   