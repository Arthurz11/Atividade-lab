def lista_vazia(lista):
    """Função que verifica se a lista está vazia"""
    return len(lista) == 0
if __name__ == "__main__":
    entrada = input("Digite números separados por vírgula: ")
    numeros = [int(num.strip()) for num in entrada.split(",")]
    print("A lista está vazia:", lista_vazia(numeros))
