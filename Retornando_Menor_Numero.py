def retornar_menor(lista):
    """Função que retorna o menor número de uma lista"""
    return min(lista)
if __name__ == "__main__":
    entrada = input("Digite números separados por vírgula: ")
    numeros = [float(num.strip()) for num in entrada.split(",")]
    print("Menor número:", retornar_menor(numeros))
