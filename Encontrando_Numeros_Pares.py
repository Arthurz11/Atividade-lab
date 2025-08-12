def encontrar_pares(lista):
    """Função que retorna uma lista contendo apenas os números pares"""
    return [num for num in lista if num % 2 == 0]
if __name__ == "__main__":
    entrada = input("Digite números separados por vírgula: ")
    numeros = [int(num.strip()) for num in entrada.split(",")]
    print("Números pares:", encontrar_pares(numeros))
