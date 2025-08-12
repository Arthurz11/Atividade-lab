def contar_ocorrencias(lista, valor):
    """Função que conta quantas vezes um valor aparece na lista"""
    return lista.count(valor)
if __name__ == "__main__":
    entrada_lista = input("Digite números separados por vírgula: ")
    numeros = [int(num.strip()) for num in entrada_lista.split(",")]
    valor_busca = int(input("Digite o número a ser contado: "))
    print("Ocorrências do número:", contar_ocorrencias(numeros, valor_busca))
