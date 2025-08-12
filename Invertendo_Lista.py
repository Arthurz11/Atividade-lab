def inverter_lista(lista):
    """Função que inverte uma lista"""
    return lista[::-1]
if __name__ == "__main__":
    entrada = input("Digite elementos separados por vírgula: ")
    lista_usuario = [item.strip() for item in entrada.split(",")]
    print("Lista invertida:", inverter_lista(lista_usuario))
