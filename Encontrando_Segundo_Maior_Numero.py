def encontrar_segundo_maior(lista):
    """Função que retorna o segundo maior número de uma lista"""
    lista_unica = list(set(lista))  # Remove duplicatas
    lista_unica.sort()
    return lista_unica[-2] if len(lista_unica) >= 2 else None
if __name__ == "__main__":
    entrada = input("Digite números separados por vírgula: ")
    numeros = [float(num.strip()) for num in entrada.split(",")]
    print("Segundo maior número:", encontrar_segundo_maior(numeros))
