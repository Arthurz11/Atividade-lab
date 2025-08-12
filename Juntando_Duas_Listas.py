def juntar_listas(lista1, lista2):
    """Função que junta duas listas"""
    return lista1 + lista2
if __name__ == "__main__":
    entrada_lista1 = input("Digite a primeira lista de elementos separados por vírgula: ")
    lista1 = [item.strip() for item in entrada_lista1.split(",")]
    entrada_lista2 = input("Digite a segunda lista de elementos separados por vírgula: ")
    lista2 = [item.strip() for item in entrada_lista2.split(",")]
    print("Lista combinada:", juntar_listas(lista1, lista2))
