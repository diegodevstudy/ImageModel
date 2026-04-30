"""
Módulo para verificação de números primos.

Este módulo implementa algoritmos eficientes para verificar se um número
é primo, utilizando a otimização Trial Division com incremento de 6.
"""

from typing import List


def is_prime(number: int) -> bool:
    """
    Verifica se um número é primo usando algoritmo Trial Division otimizado.

    Este algoritmo utiliza a propriedade matemática de que todos os números
    primos maiores que 3 são da forma 6k ± 1, reduzindo significativamente
    o número de divisões necessárias.

    Args:
        number: inteiro a ser verificado

    Returns:
        True se o número é primo, False caso contrário

    Raises:
        TypeError: se o argumento não for um inteiro

    Ejemplos:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
    if not isinstance(number, int):
        raise TypeError(f"Esperado int, recebeu {type(number).__name__}")

    # Casos base de números <= 3
    if number <= 1:
        return False
    if number <= 3:
        return True

    # Elimina múltiplos de 2 e 3
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Verifica divisores da forma 6k ± 1 até √number
    divisor = 5
    while divisor * divisor <= number:
        if number % divisor == 0 or number % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


def find_primes_in_range(start: int, end: int) -> List[int]:
    """
    Encontra todos os números primos em um intervalo específico.

    Args:
        start: início do intervalo (inclusive)
        end: fim do intervalo (inclusive)

    Returns:
        Lista contendo todos os números primos encontrados

    Raises:
        ValueError: se start > end
    """
    if start > end:
        raise ValueError(f"start ({start}) não pode ser maior que end ({end})")

    return [num for num in range(start, end + 1) if is_prime(num)]


def get_user_input() -> int:
    """
    Solicita ao usuário um número inteiro via input.

    Returns:
        int: número inteiro fornecido pelo usuário

    Raises:
        ValueError: se o entrada não for um inteiro válido
    """
    while True:
        try:
            user_input = input("\nDigite um número inteiro para verificar se é primo: ")
            number = int(user_input)
            return number
        except ValueError:
            print(f"❌ Erro: '{user_input}' não é um número inteiro válido.")
            print("   Por favor, digite um número inteiro.")


def display_result(number: int) -> None:
    """
    Verifica se um número é primo e exibe o resultado formatado.

    Args:
        number: número inteiro a verificar
    """
    print("\n" + "=" * 60)
    result = is_prime(number)
    
    if number < 0:
        print(f"⚠️  O número {number} é negativo.")
        print("   Números negativos não são considerados primos.")
    elif number == 0 or number == 1:
        print(f"⚠️  O número {number} não é primo.")
        print("   Por definição, apenas números maiores que 1 podem ser primos.")
    elif result:
        print(f"✅ {number} É UM NÚMERO PRIMO!")
        print(f"   {number} só é divisível por 1 e por ele mesmo.")
    else:
        print(f"❌ {number} NÃO É um número primo.")
        print(f"   {number} possui divisores além de 1 e ele mesmo.")
    
    print("=" * 60)


def run_interactive_mode() -> None:
    """
    Executa o programa em modo interativo.
    
    Solicita um número ao usuário e verifica se é primo,
    com opção de continuar testando outros números.
    """
    print("\n" + "*" * 60)
    print(" " * 15 + "VERIFICADOR DE NÚMEROS PRIMOS")
    print("*" * 60)
    
    while True:
        number = get_user_input()
        display_result(number)
        
        while True:
            continue_program = input("\nDeseja testar outro número? (s/n): ").strip().lower()
            if continue_program in ['s', 'sim', 'yes', 'y']:
                break
            elif continue_program in ['n', 'nao', 'não', 'no']:
                print("\n" + "*" * 60)
                print(" " * 20 + "Obrigado por usar o programa!")
                print("*" * 60 + "\n")
                return
            else:
                print("❌ Resposta inválida. Digite 's' para sim ou 'n' para não.")


if __name__ == "__main__":
    run_interactive_mode()