import sys
import os
import pathtest

def usar_memoria(tamanho_em_mb):
    # Converter tamanho de MB para bytes
    tamanho_em_bytes = tamanho_em_mb * 1024 * 1024

    # Definir tamanho da string (10 caracteres)
    tamanho_string = 10

    # Calcular o número de elementos necessários para atingir o tamanho desejado
    num_elementos = tamanho_em_bytes // sys.getsizeof('0' * tamanho_string)

    # Criar uma lista com o tamanho especificado
    lista = ['0' * tamanho_string] * num_elementos

    # Imprimir a quantidade de memória usada pela lista
    print(f"Uso de memória do teste: {sys.getsizeof(lista) / (1024 * 1024):.2f} MB")

    return lista

lista=usar_memoria(7375)
pjctPath=str(os.getcwd())
binPath=pjctPath+'/mem'
print(binPath)
print('')
print("Uso de recursos reconhecido pelo PathTop: ")
pathtest.path_search(binPath)
