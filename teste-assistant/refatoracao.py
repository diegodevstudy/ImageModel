"""
Módulo para cálculo de estatísticas básicas de uma lista de números.

Este módulo fornece funções para calcular métricas estatísticas como
soma, média, máximo e mínimo de um conjunto de valores numéricos.
"""

from typing import Tuple, List


def calculate_list_statistics(numbers: List[float]) -> Tuple[float, float, float, float]:
    """
    Calcula estatísticas básicas de uma lista de números.

    Esta função computa a soma total, média aritmética, valor máximo
    e valor mínimo de um conjunto de números fornecido.

    Args:
        numbers: Lista de números (int ou float) para análise estatística

    Returns:
        Tupla contendo (total, média, máximo, mínimo)
        - total (float): soma de todos os números
        - média (float): média aritmética dos números
        - máximo (float): maior valor na lista
        - mínimo (float): menor valor na lista

    Raises:
        ValueError: se a lista está vazia
        TypeError: se algum elemento não é numérico

    Exemplo:
        >>> calculate_list_statistics([10, 20, 30])
        (60, 20.0, 30, 10)
    """
    if not numbers:
        raise ValueError("A lista de números não pode estar vazia.")
    
    # Validar que todos os elementos são numéricos
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("Todos os elementos devem ser números (int ou float).")

    # Calcular total usando sum() built-in
    total = sum(numbers)
    
    # Calcular média
    average = total / len(numbers)
    
    # Encontrar máximo e mínimo usando funções built-in
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum


def display_statistics(total: float, average: float, maximum: float, minimum: float) -> None:
    """
    Exibe as estatísticas de forma formatada.

    Args:
        total: soma dos números
        average: média aritmética
        maximum: maior valor
        minimum: menor valor
    """
    print("\n" + "=" * 50)
    print("ESTATÍSTICAS DOS NÚMEROS")
    print("=" * 50)
    print(f"Total (Soma):        {total:.2f}")
    print(f"Média Aritmética:    {average:.2f}")
    print(f"Valor Máximo:        {maximum:.2f}")
    print(f"Valor Mínimo:        {minimum:.2f}")
    print("=" * 50 + "\n")


def main() -> None:
    """Função principal executando o programa."""
    # Dados de amostra
    sample_numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    
    print(f"Números analisados: {sample_numbers}")
    
    # Calcular estatísticas
    total, average, maximum, minimum = calculate_list_statistics(sample_numbers)
    
    # Exibir resultados
    display_statistics(total, average, maximum, minimum)


if __name__ == "__main__":
    main()