def encontrar_maior(lista):
    """Função que retorna o maior número de uma lista"""
    return max(lista)
if __name__ == "__main__":
    entrada = input("Digite números separados por vírgula: ")
    numeros = [float(num.strip()) for num in entrada.split(",")]
    print("Maior número:", encontrar_maior(numeros))
