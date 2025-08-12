def remover_duplicatas(lista):
    """Função que remove duplicatas de uma lista"""
    return list(set(lista))
if __name__ == "__main__":
    entrada = input("Digite números separados por vírgula: ")
    numeros = [int(num.strip()) for num in entrada.split(",")]
    print("Lista sem duplicatas:", remover_duplicatas(numeros))
