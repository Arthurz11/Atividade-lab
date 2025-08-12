def percorrer_lista(lista):
    """Função que percorre e imprime todos os elementos de uma lista"""
    for elemento in lista:
        print(elemento)
# Exemplo de uso:
if __name__ == "__main__":
    entrada = input("Digite os elementos da lista separados por vírgula: ")
    lista_usuario = [item.strip() for item in entrada.split(",")]
    percorrer_lista(lista_usuario)
