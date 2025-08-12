def buscar_numero(numero, lista):
    """Função que verifica se um número está na lista"""
    return numero in lista
if __name__ == "__main__":
    entrada_lista = input("Digite números separados por vírgula: ")
    numeros = [int(num.strip()) for num in entrada_lista.split(",")]
    numero_busca = int(input("Digite o número a ser buscado: "))
    print("Número encontrado:", buscar_numero(numero_busca, numeros))
