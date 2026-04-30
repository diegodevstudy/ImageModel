"""
Módulo para cálculo de estatísticas básicas de uma lista de números.

Este módulo fornece funções para calcular métricas estatísticas como
soma, média aritmética, valor máximo e valor mínimo de um conjunto de
valores numéricos.
"""

from typing import Tuple, List

# Constantes
SEPARATOR_WIDTH = 50
DECIMAL_PLACES = 2


def calculate_list_statistics(numbers: List[float]) -> Tuple[float, float, float, float]:
    """
    Calcula estatísticas básicas de uma lista de números.

    Esta função computa a soma total, média aritmética, valor máximo
    e valor mínimo de um conjunto de números fornecido.

    Args:
        numbers: Lista de números (int ou float) para análise estatística.

    Returns:
        Tupla contendo (sum_total, arithmetic_mean, max_value, min_value) onde:
        - sum_total (float): soma de todos os números
        - arithmetic_mean (float): média aritmética dos números
        - max_value (float): maior valor na lista
        - min_value (float): menor valor na lista

    Raises:
        ValueError: Se a lista está vazia.
        TypeError: Se algum elemento não é numérico.

    Exemplos:
        >>> calculate_list_statistics([10, 20, 30])
        (60, 20.0, 30, 10)
        >>> calculate_list_statistics([5, 15, 25, 35])
        (80, 20.0, 35, 5)
    """
    if not numbers:
        raise ValueError("A lista de números não pode estar vazia.")
    
    # Validar que todos os elementos são numéricos
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError(
            "Todos os elementos devem ser números (int ou float). "
            f"Tipo inválido encontrado: {type(numbers[0]).__name__}"
        )

    # Calcular total usando sum() built-in
    sum_total = sum(numbers)
    
    # Calcular média aritmética
    arithmetic_mean = sum_total / len(numbers)
    
    # Encontrar máximo e mínimo usando funções built-in
    max_value = max(numbers)
    min_value = min(numbers)
    
    return sum_total, arithmetic_mean, max_value, min_value


def display_statistics(
    sum_total: float,
    arithmetic_mean: float,
    max_value: float,
    min_value: float
) -> None:
    """
    Exibe as estatísticas de forma formatada no console.

    Args:
        sum_total: soma de todos os números.
        arithmetic_mean: média aritmética dos números.
        max_value: maior valor encontrado.
        min_value: menor valor encontrado.
    """
    separator = "=" * SEPARATOR_WIDTH
    print(f"\n{separator}")
    print("ESTATÍSTICAS DOS NÚMEROS".center(SEPARATOR_WIDTH))
    print(separator)
    print(f"Total (Soma):        {sum_total:.{DECIMAL_PLACES}f}")
    print(f"Média Aritmética:    {arithmetic_mean:.{DECIMAL_PLACES}f}")
    print(f"Valor Máximo:        {max_value:.{DECIMAL_PLACES}f}")
    print(f"Valor Mínimo:        {min_value:.{DECIMAL_PLACES}f}")
    print(f"{separator}\n")


def main() -> None:
    """Função principal que executa o programa de análise estatística."""
    # Dados de amostra para análise
    sample_numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    
    print(f"Números analisados: {sample_numbers}")
    
    # Calcular estatísticas da lista
    sum_total, arithmetic_mean, max_value, min_value = calculate_list_statistics(
        sample_numbers
    )
    
    # Exibir resultados formatados
    display_statistics(sum_total, arithmetic_mean, max_value, min_value)


if __name__ == "__main__":
    main()