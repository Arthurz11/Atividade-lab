def extrair_nomes(lista_objetos):
    """Função que extrai os nomes de uma lista de objetos"""
    return [objeto['nome'] for objeto in lista_objetos]
if __name__ == "__main__":
    entrada = input("Digite os objetos no formato nome:valor separados por vírgula: ")
    lista_objetos = [dict(zip(['nome', 'valor'], item.split(':'))) for item in entrada.split(",")]
    print("Nomes extraídos:", extrair_nomes(lista_objetos))
