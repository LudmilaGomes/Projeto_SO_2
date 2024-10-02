# Abrir e ler o arquivo
with open('dados.txt', 'r') as file:
    numeros = file.readlines()

# Converter cada linha em um número inteiro e remove quebras de linha
numeros = [int(numero.strip()) for numero in numeros]


primeiro_numero = numeros[0]
lista = [[numero, -1] for numero in numeros[1:]]

lista_quadro_atual = lista[:primeiro_numero]

falta_quadro = primeiro_numero


for i in range(primeiro_numero):
    lista_quadro_atual[i][1] = i + 1

# Remove os valores que já estão nos quadros
del lista[:primeiro_numero]


for i in range(len(lista)):
    print("Estado atual do quadro:", lista_quadro_atual)

    if lista[i][0] not in [q[0] for q in lista_quadro_atual]:
        print('Mudar quadro')

        menor_valor = min(lista_quadro_atual, key=lambda x: x[1])
        print("Menor valor:", menor_valor)

        maior_valor = max(lista_quadro_atual, key=lambda x: x[1])
        print("Maior valor:", maior_valor)

        lista[i][1] = maior_valor[1] + 1
        print("Atribuindo a lista:", lista[i])

        index_menor_valor = lista_quadro_atual.index(
            menor_valor)
        lista_quadro_atual[index_menor_valor] = lista[i]

        falta_quadro += 1
    else:

        for q in lista_quadro_atual:
            if q[0] == lista[i][0]:
                q[1] = max(lista_quadro_atual, key=lambda x: x[1])[1] + 1
                break

            
            
       
print("LRU ", falta_quadro)
