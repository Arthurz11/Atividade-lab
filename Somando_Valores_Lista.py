def somar_valores(lista):
    """Função que retorna a soma dos valores de uma lista"""
    return sum(lista)
if __name__ == "__main__":
    entrada = input("Digite números separados por vírgula: ")
    numeros = [float(num.strip()) for num in entrada.split(",")]
    print("Soma dos valores:", somar_valores(numeros))
