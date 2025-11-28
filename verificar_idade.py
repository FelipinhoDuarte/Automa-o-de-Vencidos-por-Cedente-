def verificar_idade(idade):
    """
    Verifica se a idade é maior do que 18 anos.
    
    Args:
        idade (int): A idade a ser verificada
        
    Returns:
        bool: True se maior de 18, False caso contrário
    """
    if idade > 18:
        return True
    else:
        return False


def main():
    try:
        idade = int(input("Digite a idade: "))
        
        if idade < 0:
            print("Erro: A idade não pode ser negativa!")
            return
        
        if verificar_idade(idade):
            print(f"A idade {idade} é maior do que 18 anos.")
        else:
            print(f"A idade {idade} não é maior do que 18 anos.")
            
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido!")


if __name__ == "__main__":
    main()
