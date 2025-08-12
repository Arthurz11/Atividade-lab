def calcular_media(lista):
    """Função que calcula a média dos números de uma lista"""
    return sum(lista) / len(lista) if lista else 0
if __name__ == "__main__":
    entrada = input("Digite números separados por vírgula: ")
    numeros = [float(num.strip()) for num in entrada.split(",")]
    print("Média dos números:", calcular_media(numeros))
